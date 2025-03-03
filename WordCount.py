#WordCount.py
#Name: April Lastra 
#Date: 03/02/2025
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')

try: 
  #open the file for reading 
  with open("gettysberg.txt", 'r') as textFile:
    # Initialize counters
    line_count = 0
    word_count = 0 
    char_count = 0 

    # Read through the file line by line 
    for line in textFile: 
      line_count += 1
      word_count += len(line.split())
      char_count += len(line)

  # Print the statistics 
  print(f"Lines: {line_count}")
  print(f"Words: {word_count}")
  print(f"characters: {char_count}")
  

  

if __name__ == '__main__':
  main()
