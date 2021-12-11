from replit import clear
from art import logo 
#Calculator
#add
def add(n1,n2):
  return n1+n2
#Substract
def subtract(n1,n2):
  return n1-n2
#Multiply
def multiply(n1,n2):
  return n1*n2
#Divide
def divide(n1,n2):
  return(n1/n2)

#creating an operation dictionary:
operations={
'+': add,
'-': subtract,
'*': multiply,
'/': divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for operation in operations:
    print(operation)
  #check= input(f"Type 'y' to continue calculating with {answer} or 'n' to exit \n").lower()
  should_continue= True
  while should_continue: 
    operation_symbol= input("Pick an operation  ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer= calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    check= input(f"Type 'y' to continue calculating with {answer} or 'n' to exit \n").lower()
    if check =='y':
      num1= answer
    else:
      should_continue= False
      clear()
      calculator() #recursive func


calculator()
