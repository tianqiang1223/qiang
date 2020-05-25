# -*- coding: utf-8 -*-
'''
Created on Monday, May 25, 2020 20:55

@author: tianqiang
'''
import os 
import cv2
import numpy as np
def main():
	dir = '/home/tianqiang/images/train/' 
	files = os.listdir(dir)
	print(files)
	print(len(files))
	print('[*] start...')
	mean = 0
	sigma_max = 2 #0-30
	for sig in range(sigma_max):
		for i in range(len(files)):
			filepath = dir + files[i]
			image = cv2.imread(filepath)  #需要文件的绝对路径
			image = cv2.resize(image, (32,32), interpolation = cv2.INTER_CUBIC)  #基于4x4像素邻域的3次插值法
			row, col, ch = image.shape
			sigma = sig
			Gauss = np.random.normal(mean, sigma, (row, col, ch))
			Gauss = Gauss.reshape(row, col, ch)
			noisy = image + Gauss
			noisy = np.clip(noisy, 0, 255)    #限制最大最小值
			noisy = noisy.astype('uint8')
			cv2.imwrite('/home/tianqiang/images/train_noisy/%d.%d.png' %(sigma, i), noisy)
	print('[*] OK...')
	return files

if __name__ == '__main__':
	main()
