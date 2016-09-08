#computer vision 
from math import atan2

nums = open("sheetmusic1ppm", 'r').read().split()
#print(nums)

zero = nums.pop(0)
one = int(nums.pop(0))
two = int(nums.pop(0))
twofiftyfive = int(nums.pop(0))
ex = []

def grayscale():
	i = 0
	while (i < ((one)*(two)*3)):
		avg = '%.0f' % ((int(nums[i]) * 0.2989) + (int(nums[i+1]) * 0.5870) + (int(nums[i+2]) * 0.1140))
		ex.append(avg)
		ex.append(avg)
		ex.append(avg)
		i = i + 3
		
grayscale()
out = open("sheetmusic1gray.ppm", 'w')

out.write(zero + "\n")
s = str(one) + " " + str(two)
out.write(s + "\n")
out.write(str(twofiftyfive) + "\n")
s = ""
for i in range(0, len(ex)):
	s += str(ex[i]) + " "
out.write(s)
