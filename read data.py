# -*- coding: utf-8 -*-
'''
Created on Tuesday, May 26, 2020 10:33
@author: tianqiang
'''

import random

def load_data():
	train_data = []
	train_label = []
	with open('/home/tianqiang/images/path_label.txt', 'r') as f:
		lines = f.readlines()
		random.shuffle(lines)
		for line in lines:
			line = line.split( )
			data = line[0]
			label = line[1]
			train_data.append(data)
			train_label.append(label)
	return train_data, train_label
