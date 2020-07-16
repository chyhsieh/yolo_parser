# yolo_parser
## darknet

1. useful trouble shooting for using darknet with GPU:

http://sisyphus2018deeplearning.blogspot.com/2018/10/ubuntudarknet.html

2. use `make` but result in `chmod...` -> make clean; make

3. darknet command for analyzing video with output txt file

`./darknet detector demo ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights [video_path] -i 0 -thresh 0.25 -dont_show -ext_output > [outputfile].txt`

4. remember to download weights

## parser

`python3 yolo_parser.py [txt file path]`
