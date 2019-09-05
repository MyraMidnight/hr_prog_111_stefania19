n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter = 0


while counter < n :
  #placeholder for the printed number
  x = 0
  x_range = []
  #run through the range and add the numbers: 0 + 1 + 2 ... and then print the final number
  for i in range(counter) :
    x += range(counter)[-1]
  print(x, end=", ")
  counter += 1