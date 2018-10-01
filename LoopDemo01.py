#loops are structures used to repeat sectuins of code.
#They are useful if you have to do the same thing more than once
#or you can establish a pattern

#Example 1:
print("0")
print("1")
print("2")
print("3")
print("4")
print("************")

#This is counted loop. I want you to think about
#count, check, change
# i = 0, 0 < 5, True - run loop
# i = 1, 0 < 5, True - run loop
# i = 2, 0 < 5, True - run loop
# i = 3, 0 < 5, True - run loop
# i = 4, 0 < 5, True - run loop
# i = 5, 0 < 5, False - exit and move on

for i in range(4,11,2):
	#Anything tabbed is considered the loop block
	print(i)

print("*************BackWards***************")
for i in range(10,-1,-1):
	print(i)




print("*****Printing String Characters******")
str= "Monkey"


#Always indicate the length of a word using the function len
for i in range (len(str)-1,-1,-1):
	print(str[i])



print("***Print every second letter in str start at index***")

for i in range (0, len(str), 2):
	print(str[i])
