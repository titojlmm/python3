import random

correct = 0
for iteration in range(0, 10):
  # Generate a new random number
  k = random.randint(10000, 1000000)

  # Read the user's choice
  print("Prime or Not: Is the number ", k, " prime? (yes or no)")
  answer = input()
  # Is the number K prime?
  for n in range(1, int(k/2)):
    # Divide K by all numbers < K/2
    if k % n == 0:
      # If the remainder is 0 then n divides evenly into K: not prime
      isprime = "no"
      break
  else:
    isprime = "yes"  # Loop not exited: it is prime

  if isprime == answer:
    print("You are correct!")
    correct = correct + 1
  else:
    print("You are incorrect.")

print("You gave ", correct, " answers out of 10.")
