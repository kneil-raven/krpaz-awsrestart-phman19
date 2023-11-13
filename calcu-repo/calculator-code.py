def add(x, y):
  return x + y


def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  if y == 0:
    return "Error! Division by zero!!!"
  return x / y


# calculator menu operators
# insert q in this list if you want to add QUIT operation
menuOperators = ('+', '-', '*', '/') 



def calculator():
  while True:
    print('=============================')
    print('Please choose an operator:')
    print('+ - Addition')
    print('- - Subtraction')
    print('* - Multiplication')
    print('/ - Division')
    # print('q - Quit')
    print('=============================')

    operatorInput = input('Enter operator: ')
    # print('nirun after nainput ang operator')
    # if operatorInput == 'q':
    #   print('You selected QUIT. BYEBYE!!')
    #   break

    if operatorInput in menuOperators:
      try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
      except ValueError:
        print('Invalid input. Please try again.')
        continue

      if operatorInput == '+':
        print(add(num1, num2))
      elif operatorInput == '-':
        print(subtract(num1, num2))
      elif operatorInput == '*':
        print(multiply(num1, num2))
      elif operatorInput == '/':
        if num2 == 0:
          print('Error! Division by zero!!!')
        else:
          print(divide(num1, num2))

      computeAgain = input('Do you want to compute again? (y/n): ').lower()
      if computeAgain == 'n':
        print('You selected NO. STOP COMPUTING!')
        break

    else:
      print(f'{operatorInput} is not valid! Try again!')


calculator()
