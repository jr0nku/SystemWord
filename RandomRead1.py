#----- RandomRead1.py -----
#*****************************************
#
#	Random Read 1 Sentence Ver 1.0
#
#	programmed by kaneko  Sep.12 2019
#
#*****************************************
import random

FileName = 'SystemWord.txt'

#===== read file =====
n = 0
f = open(FileName, "r")
line = [f.readline()]
while line[n]:
	n = n + 1
	line.append(f.readline())
f.close()

#===== print all sentence =====
#for i in range(0, n):
#	print(line[i])
#print(n)

#===== print one sentence =====
print(random.choice(line))

