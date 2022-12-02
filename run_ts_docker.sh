#!/bin/bash

docker run -it --rm --runtime=nvidia -v $PWD:/tf -p 8888:8888  tensorflow/tensorflow:2.9.0-gpu-jupyter-v2

