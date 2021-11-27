'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

number = int(input("Enter a number: "))

second_number = int(input("Enter another number: "))

third_number = int(input("Enter a third number: "))

if number < second_number and (number < third_number or number == third_number):
  print("The smallest number is ", number) 

elif second_number < number and (second_number < third_number or second_number == third_number):
  print("The smallest number is", second_number)

elif third_number < number and (third_number < second_number or third_number == second_number): 
  print("The smallest number is", third_number)  

elif number < third_number and (number < second_number or number == second_number):
  print("The smallest number is", number)

elif number == second_number == third_number:
  print("The smallest number is", number)





