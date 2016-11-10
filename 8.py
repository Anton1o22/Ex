def primo(x):
	for i in range (2, x/2):
		if x % i == 0:
			return False
	return True
for primo in range (2, 100):
	if primo == True:
		print "Es primo"