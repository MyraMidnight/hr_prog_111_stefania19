n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter = 0
collection = [1,2,3,6]

while counter <= n :
  #placeholder for the printed number
  x = 0
  if n > 3 :
    #if the number is larger than 3, it shall create the larger numbers
    for i in range(counter) :
      #add together the last three numbers in collection
      x = collection[-1] + collection[-2] + collection[-3]
      #push the new sum to the collection
      collection.append(x)
  counter += 1

for i in range(n) :
  print(collection[i])