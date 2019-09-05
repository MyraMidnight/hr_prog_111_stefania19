
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0
while num_int > 0 :
  #update max_int if input is larger
  if num_int > max_int:
    max_int = num_int
  #ask again for input as long as input is larger than 0
  num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line

