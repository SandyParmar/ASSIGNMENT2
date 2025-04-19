def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break


number = inputNumber("Enter a number :")
print(number)

if number % 2 == 0:
    print(str(number) + " is an even number.")
else:
    print(str(number) + " is an odd number.")