A = [0, 54, 110, 29, 555, 34, -59, 22]
SizeA = len(A)

Temp_Sort = []


#Store 1st in Array as biggest
B = A[0]

#For loops to compare subsequent number in array with biggest values
Def FindBiggest(a,b):
for num in range(1,SizeA):
    if(A[num] < B):
       B=A[num]
#	elif(A[num] < B):
#		B=A[num]
    print("Current Biggest = %d\n"%B)

print("Final Biggest number is %d" %B)
#input()

# A = [0, 54]
# print(A)

# if(A[0] > A[1]):
	# B=A[0], A[1]
# elif(A[1] > A[0]):
	# B=A[1], A[0]

# print(B)
# input()