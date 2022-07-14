# My README

This fork should allow us to run inference using the fashionpedia project.
Because this code base is all weird, we need to be a little careful about how we use it.

## Environment
Let's use Anaconda to prepare an old Python:
```bash
conda create -n tpu python=3.7
conda activate tpu
```
Then install a couple of (very old, of course) dependencies:
```bash
pip install tensorflow-gpu==1.15.0 protobuf==3.20.0 numpy==1.19.0 
```
Next, navigate to the `detection` directory:
```bash
cd path/to/tpu/models/official/detection
```
In that directory, we have placed `inference_fashion.py`.
That file does odd things to PYTHONPATH such that all the imports _should_ work.
Download model weights:
```bash
curl https://storage.googleapis.com/cloud-tpu-checkpoints/detection/projects/fashionpedia/fashionpedia-spinenet-143.tar.gz --output fashionpedia-spinenet-143.tar.gz
tar -xf fashionpedia-spinenet-143.tar.gz
```
Finally, perform inference:
```bash
python inference_fashion.py --model="attribute_mask_rcnn" --image_size="640" --checkpoint_path="fashionpedia-spinenet-143/model.ckpt" --label_map_file="projects/fashionpedia/dataset/fashionpedia_label_map.csv" --image_file_pattern="path/to/sized-images.tar" --output_html="out.html" --max_boxes_to_draw=8 --min_score_threshold=0.05 --config_file="projects/fashionpedia/configs/yaml/spinenet143_amrcnn.yaml" --output_file="output.npy"
```










# Cloud TPUs #

This repository is a collection of reference models and tools used with
[Cloud TPUs](https://cloud.google.com/tpu/).

The fastest way to get started training a model on a Cloud TPU is by following
the tutorial. Click the button below to launch the tutorial using Google Cloud
Shell.

[![Open in Cloud Shell](http://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/open?git_repo=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftpu&page=shell&tutorial=tools%2Fctpu%2Ftutorial.md)

_Note:_ This repository is a public mirror, pull requests will not be accepted.
Please file an issue if you have a feature or bug request.

## Running Models

To run models in the `models` subdirectory, you may need to add the top-level
`/models` folder to the Python path with the command:

```
export PYTHONPATH="$PYTHONPATH:/path/to/models"
```
