n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter = 0
collection = []

while counter <= n :
  #placeholder for the printed number
  x = 0
  if n > 3 :
    #add the last three numbers from range to x
    for i in range(counter, 0 , -1) :
      print(i, end=", ") # + range(counter)[i-2] + range(counter)[i-3]
  print()
  counter += 1