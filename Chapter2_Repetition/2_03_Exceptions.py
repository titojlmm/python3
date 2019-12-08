try:
  print("Input the first term of the division: ")
  a = float(input())
  print("Input the second term of the division: ")
  b = float(input())
  c = a / b
except ValueError:
  # Si alguno de los términos de la operación no es un número.
  c = 0
except ZeroDivisionError:
  # Si se intenta dividir por cero. Es decir, b=0.
  c = 1000000
print("Result: ", c)
