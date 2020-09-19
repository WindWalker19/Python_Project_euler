# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def lpf(num):
	div = 2
  
	while(num != 0):
		if(num % div !=0):
			div = div + 1
		else:
			maxpf = num
			num = num/div
			if(num == 1):
				break;
	
	return maxpf


print(lpf(600851475143))
