#DiceRoll.py
#Name: april lastra 
#Date: 03/02/2025
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]

  #Define the number of rolls 
  num_rolls = 10000 

  # Roll the dice num_rolls times 
  for _ in range(num_rolls):
    #Create two dice values ranging from 1 - 6 each
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
  
  #find the sum total of the two dice
  total = die1 + die2
  
  # Store count at the correct index 
  rolls[total - 2] += 1

  #print statictics for dice rolls
  print("Sum | Count | Percentage")
  print("_________________________")
  for i in range(11): 
    total = i + 2 
    count = rolls[i]
    percentage = (count / num_rolls) * 100
    print(f"{total:3} | {count:6} | {percentage:6.2f}%")


if __name__ == '__main__':
  main()
