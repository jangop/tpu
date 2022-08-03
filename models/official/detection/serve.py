from multiprocessing.connection import Listener

from inference_fashion import argv_main


def serve():
    address = ("localhost", 6969)
    with Listener(address, authkey=b"pepper") as listener:
        while True:
            with listener.accept() as connection:
                data = connection.recv()

                print(f"Received:/n{data}")

                argv = sum([[f"--{key}", value] for key, value in data.items()], [])

                print(f"arguments:/n{argv}")

                try:
                    argv_main(argv)
                except Exception as exception:
                    connection.send(str(exception))
                    raise
                else:
                    connection.send("OK")


if __name__ == "__main__":
    serve()
