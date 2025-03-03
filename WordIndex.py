#WordIndex.py
#Name: April Lastra 
#Date: 03/02/2025
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary

  # Read through the file line by line 
  line_number = 0 
  for line in textFile: 
    line_number += 1 
    word_list = line.strip().split()

    for word in word_list:
      word = word.lower().strip(".,!?()[]{}\"'")

      # Add word to dictionary if not present
      if word in words: 
        words[word].append(line_number)
      else:
        words[word] = [line_number]

# Print the word index 
for word in sorted(words.keys()):
  print(f"{word}: {words[word]}")

if __name__ == '__main__':
  main()
