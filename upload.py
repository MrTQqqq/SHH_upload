#!/usr/bin/python
# -*- coding: UTF-8 -*-

import paramiko 
import os
import datetime
import os.path
import hashlib

remote_config = {'hostname':'172.16.80.39', 'username':'root', 'port':22,'password':'123456'}


def upload_file(local_dir, remote_dir):
	try:
		print("start connect")
		myHash = hashlib.md5()
		t = paramiko.Transport(remote_config['hostname'], remote_config['port'])
		t.connect(username = remote_config['username'], password = remote_config['password'])

		sftp = paramiko.SFTPClient.from_transport(t)
		print("connected")
		for root, dirs, files in os.walk(local_dir):
			print('[%s] [%s] [%s] ' % (root, dirs, files))  

			for file in files:
				local_file = os.path.join(root, file)
				a = local_file.replace(local_dir, '').replace('\\','/').lstrip('/')
				remote_file = os.path.join(remote_dir, a)

				try:
					sftp.put(local_file, remote_file)
				except Exception as e:
					sftp.mkdir(os.path.split(remote_file)[0])
					sftp.put(local_file, remote_file)
					print('upload %s to remote %s ' % (local_file, remote_file))
			for name in dirs:
				local_path = os.path.join(root, name)
				a = local_path.replace(local_dir, '').replace('\\', '')
				remote_path = os.path.join(remote_dir, a)
				try:
					sftp.mkdir(remote_path)
				except Exception as e:
					print("error")

		print("upload success")
		r.close()

	except Exception as e:
		print("upload fail")




def print_file_name(local_dir):
	for root, dirs, files in os.walk(local_dir):
		for file in files:
			print(file)



if __name__ == '__main__':
	upload_file(r'C:\\Users\\ADMIN\\Desktop\\py', '/root/py/')












