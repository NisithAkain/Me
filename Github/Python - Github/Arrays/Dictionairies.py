#Dictionairies syntax
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])#returns "Ford"
print(len(thisdict))#returns the amount of iteams in a list 

#Acessing iteam
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]#returns the key "Mustang"

#Changing/adding iteams
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"]="1019"
print(thisdict["year"])
thisdict["creator"] ="Dr.Bobensein" # makes new key

#Pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)# returns ["brand":"Ford","year":1964]




