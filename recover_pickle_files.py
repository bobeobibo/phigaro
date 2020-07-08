import os

def recover(path):
	if os.path.isdir(path):
		for file in os.listdir(path):
			recover(path+'/'+file)
	else:
		with open(path, 'rb') as f:
			content = f.read()
		with open(path, 'wb') as f:
			f.write(content.replace(b'\r\n', b'\n'))

path = 'phigaro'
recover(path)