import DCcode, random

def ffunction(x):
	de = DCcode.decode(x)
	#Dummy fitness function 
	result = random.uniform(1,10)
	#--------------------------
	return result

if __name__ == "__main__":
	print(ffunction(5))