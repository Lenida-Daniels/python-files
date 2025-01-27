
name=input("enter your name")#basic input() function
print(name)
age=int(input("enter age"))#converting to int since an input always returns string
print(age)
print(type(age))


#error handling
try:
    # Code that might raise an error
    num = int(input("Enter a number: "))
    print(f"You entered: {num+1}")
except ValueError:
    # Handles the exception
    print("Invalid input. Please enter a number.")

password = input("Enter your password (8+ characters): ")
choice = input("""Choose an option:
1. Start
2. Help
3. Exit
Enter your choice: """)



#input a list
#you can't convert the whole string into an integer
#so, you first split the string into list of individual strings
#then convert each string into an integer or any desired data type
numbers=input("enter numbers separated by spaces:").split()

print(numbers)
#convert to integer
numbers = [int(num) for num in numbers]
print(numbers)  # Example: [1, 2, 3]
#convert to float
numbers=[float(num)for num in numbers]
print(numbers)

#using input with a loop
while True:
    response=input("Type 'exit' to quit").lower()#lower() converts a string into lower case except num,special characters and punctuations.
    if response == 'exit':
        print("goodbye!")
        break
    else:
        print(f"you entered:{response}")


#for multiple inputs
x,y=map(int,input("enter two nums separated by a space:").split())
print(f"the sum is:{x+y}")


"""
limitations of input()
#blocking - program waits until the user provides input
#security - avoid using input() for sensitive information in production
#so for sensitive input use the getpass module
"""
from getpass import getpass

password = getpass("Enter your password: ")
print("Password received.")













