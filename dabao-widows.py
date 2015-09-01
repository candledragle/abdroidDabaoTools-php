#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import os
import shutil
import sys
channal_list=['qq','baidu','qihu','wandoujia','anzhi','leshi','jiuyi','huawei','xioami','anzhuo']
#channal_list=['anzhuo']
#获取脚本路径
rootPath = sys.path[0]
def dabao():
	for channal_name in channal_list:
		qudaoName=rootPath+'\TatuQuan_Android_{0}Release_1.0.5_b150810.apk'.format(channal_name)
		shutil.copy(rootPath+'\TatuQuan_Android_officialRelease_1.0.5_b150810.apk','TatuQuan_Android_{0}Release_1.0.5_b150810.apk'.format(channal_name))
		zipped = zipfile.ZipFile(os.path.basename(qudaoName) ,'a', zipfile.ZIP_DEFLATED) 
		print(os.path.basename(qudaoName))
		empty_channel_file = "META-INF\\tqchannel_{channel}".format(channel=channal_name)
		zipped.write('channal', empty_channel_file)
		zipped.close()

dabao()

