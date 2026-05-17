#Lists syntax
thislist = ["apple","banana","orange","cherry"]
print(type(thislist)) #returns the type 
print(len(thislist))# returns the amount of iteams in list 

#Acess iteams 
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # returns banana, apple is index "0"
print(thislist[0:2])# returns apple and banana

#Change list iteams
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #returns ["apple", "blackurrant", "banana", "cherry"]
print(thislist[0:2]) # "apple", "banana"

#Insert iteams 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #["apple","banana","watermelon","cherry"]

#Append iteams
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)#returns ["apple","banana","cherry","orange"]

#Extend List 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.exend(tropical)
print(thislist) # returns ["apple", "banana", "cherry","mango", "pineapple", "papaya"]

#Remove specific iteam 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)#reaturns ["apple","cherry"]

#pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)# [apple,cherry]

