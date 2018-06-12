
import random

def begin():
  num = -1
  gen = random.randint(1,101)
  while num != gen:
    num = input("Guess a number! ")
    print "You guessed ", num
    if(num == gen):
      print "Correct!"
      break
    elif (num < gen):
      print "Too low!"
    else:
      print "Too high!"

begin();

