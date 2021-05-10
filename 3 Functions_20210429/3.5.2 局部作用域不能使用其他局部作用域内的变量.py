# the egg in beaf() will be returned not the egg in pork()
def beaf():
	egg = 1
	pork()
	print(egg)
	
def pork():
	egg = 2
	
beaf()
