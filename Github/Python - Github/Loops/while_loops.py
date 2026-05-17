#while loop
i = 1
while i < 6:
  print(i)
  i += 1
#returns 1,2,3,4,5

#Break statement 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#returns 1,2

#Continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#continuses to the next iterration 