import os,sys, platform

os.system('chmod 777 h32.cpython-310.so')
os.system('chmod 777 h64.cpython-310.so')
bit = platform.architecture()[0]
if bit == '64bit':
	import h64
	h64.fbClone()
if bit == '32bit':
	import h32
	h32.fbClone()
else :
	print('your mobile not supported this tool ')
