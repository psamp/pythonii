##
#  This program reads a sequence of values and prints them, marking the largest value.
#

# Create an empty list.
values = []

# Read the input values.
print("Please enter values, Q to quit:")
userInput = input("")
while userInput.upper() != "Q" :
   values.append(float(userInput))
   userInput = input("")
   
# Find the largest value.
largest = values[0]
for i in range(1, len(values)) :
   if values[i] > largest :
      largest = values[i]

# Find the smallest value.
smallest = values[0]
for i in range(1, len(values)) :
   if values[i] < smallest :
      smallest = values[i]      
      
# Print all values, marking the largest and smallest.
for element in values :
   print(element, end="")
   if element == largest :
      print(" <== largest value", end="")
   if element == smallest :
      print(" <== smallest value", end="")
   print()
