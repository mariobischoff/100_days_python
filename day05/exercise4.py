for number in range(1, 101):
  print_string = ""
  if number % 3 == 0:
    print_string += "Fizz"
  if number % 5 == 0:
    print_string += "Buzz"
  print(print_string or number)