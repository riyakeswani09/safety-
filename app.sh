#!/bin/bash

FILE="$1"

cd yolo && rm -rf ./runs/detect && python traffic-monitor.py --source "$0" --weights 'runs/train/exp/weights/best.pt'  --save-crop && cd .. && python ./main.py 