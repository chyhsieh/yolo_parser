import csv
import re
import pandas as pd
import sys
rx_dict = {
	'file' : re.compile(r'video file: (?P<file>.*)\.mp4'),
	'stream' : re.compile(r'Video stream: (?P<stream>[0-9]* x [0-9]*)'),
	'obj' : re.compile(r'((?P<obj>([a-zA-Z]|\s)*):\s(?P<prob>[0-9]*)%)+(\s)*\(left_x:(\s)*(?P<left_x>[0-9]*)(\s)*top_y:(\s)*(?P<top_y>[0-9]*)(\s)*width:(\s)*(?P<width>[0-9]*)(\s)*height:(\s)*(?P<height>[0-9]*)\)'),
	'num' : re.compile(r'Objects:\s'),
}

def _parse_line(line):
	for key, rx in rx_dict.items():
		match = rx.search(line)
		if match:
			return key, match
	return None, None

def _parse_file(filepath):
	data = []
	num = 0
	with open(filepath, 'r') as file_object:
		line = file_object.readline()
		while line:
			key, match = _parse_line(line)
			if key == 'file':
				#file = match.group('file')
				File = match.group('file')
			if key == 'stream':
				stream = match.group('stream')
			if key == 'num':
				num = num+1
			if key == 'obj':
				left_x = match.group('left_x')
				top_y = match.group('top_y')
				width = match.group('width')
				height = match.group('height')
				obj_list = []
				obj_list = line.split('%')
				obj_list.pop()
				#pattern = re.compile(r'(?P<obj>[a-zA-Z]*):\s(?P<prob>[0-9]*))')
				for i in range(0, len(obj_list)):
					pattern = re.match(r'(\s)*(?P<obj>([a-zA-Z]|\s)*):\s(?P<prob>[0-9]*)', obj_list[i])
					#print(obj_list[i])
					obj = pattern.group('obj')
					prob = pattern.group('prob')
					row = {
						'File':File,
						'Stream':stream,
						'Frame_num': num,
						'Object':obj,
						'Probibility:':prob,
						'left_x':left_x,
						'top_y':top_y,
						'width':width,
						'height':height,
					}
					data.append(row)
				#obj = match.group('obj')
				#prob = match.group('prob')
			line = file_object.readline()
		data = pd.DataFrame(data)
		#data.set_index(['File','Stream','FPS', 'Object', 'Probibility', 'left_x', 'top_y', 'width', 'height'], inplace=True)
		#data = data.groupby(level=data.index.names).first()
	return data

if __name__=='__main__':
	filepath = sys.argv[1]
	data=_parse_file(filepath)
	output = filepath.split('\\').pop().split('/').pop().rsplit('.', 1)[0]+'.csv'
	data.to_csv(output, index=0)
	#print(data)
