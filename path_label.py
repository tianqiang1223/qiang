# -*- coding: utf-8 -*-
'''
Created on Monday, May 25, 2020 12:05

@author: tianqiang
'''

import os

def main():
	dir = '/home/tianqiang/images/train_noisy'
	files = os.listdir(dir)   #返回指定的文件夹包含的文件或文件夹的名字的列表
	files.sort()
	f = open ('/home/tianqiang/images/path_label.txt','w',encoding='utf-8') 
	print('[*] start...')
	for file in files:
		fileType = file.split('.')
		file_label = fileType[0]
		filepath = dir+'/'+file
		name = filepath + ' ' + file_label + '\n'
		f.write(name)
	f.close() 
	print('[*] OK...')		
if __name__ == '__main__':
	main()
