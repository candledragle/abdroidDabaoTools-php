#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import os
import shutil
channal_list=['qw','qe','qr','qt']
def dabao():
	for channal_name in channal_list:
		qudaoName='./{0}.apk'.format(channal_name)
		shutil.copy('./app.apk',qudaoName)
		zipped = zipfile.ZipFile(os.path.basename(qudaoName) ,'a', zipfile.ZIP_DEFLATED) 
		empty_channel_file = "META-INF/mtchannel_{channel}".format(channel=channal_name)
		zipped.write('channal', empty_channel_file)
		zipped.close()

dabao()

