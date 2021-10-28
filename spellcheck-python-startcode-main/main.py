# SpellCheck Assignment - Ganesh Baral

import re, time


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    
    for i in range(len(aliceWords)):
      aliceWords[i] = aliceWords[i].lower()

    loop = True  
    # Begin Loop
    while loop:
        print("\nMAIN MENU")
        print("1. Spell Check a Word (Linear Search)")
        print("2. Spell Check a Word (Binary Search)")
        print("3. Spell Check Alice in Wonderland (Linear Search)")
        print("4. Spell Check Alice in Wonderland (Binary Search)")
        print("5. Exit")

        # User Input
        option = input("Enter menu selection (1-5): ")

        # Outputs 

        # Option 1
        if option == "1": 
            userInput = input("Enter a word to search for in the dictionary: ")
            userInput = userInput.lower()
            beginTimer = time.time()
            position = linearSearch(dictionary, userInput)
            if position == -1:
                print(userInput + " NOT found in the dictionary")
                endTimer = time.time()
                print("Time Elapsed: " + str((endTimer - beginTimer)) + " seconds")
            else:
                print(userInput + " is IN the dictionary at position " + str(position))
                endTimer = time.time()
                print("Time Elapsed: " + str((endTimer - beginTimer)) + " seconds")
        
        # Option 2    
        elif option == "2":
            userInput = input("Enter a word to search for in the dictionary: ")
            userInput = userInput.lower()
            beginTimer = time.time()
            position = binarySearch(dictionary, userInput)
            if position == -1:
                print(userInput + " NOT found in the dictionary")
                endTimer = time.time()
                print("Time Elapsed: " + str((endTimer - beginTimer)) + " seconds")   
            else:
                print(userInput + " is IN the dictionary at position " + str(position))
                endTimer = time.time()
                print("Time Elapsed: " + str((endTimer - beginTimer)) + " seconds")

        # Option 3    
        elif option == "3": 
            number = 0
            beginTimer = time.time()
            for word in aliceWords:
                position = linearSearch(dictionary, word)
                if (position == -1 ): number += 1
            endTimer = time.time()
            print("Number of words NOT found in dictionary: " + str(number) + " \nTime Elapsed: " + str((endTimer - beginTimer)) + " seconds")

        # Option 4
        elif option == "4":
            number = 0
            beginTimer = time.time()
            for word in aliceWords:
                position = binarySearch(dictionary, word)
                if (position == -1 ): number += 1
            endTimer = time.time()
            print("Number of words NOT found in dictionary: " + str(number) + " \nTime Elapsed: " + str((endTimer - beginTimer)) + " seconds")
            
        # Option 5 and End Loop
        elif option == "5":
            print("Bye!")
            loop = False
        else: 
            print("Pick a number through 1 to 5 next time")
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


#Linear Search
def linearSearch(anArray, item):
  for i in range(len(anArray)):
    if anArray[i] == item:
      return i
    
  return -1
#end linearSearch()

#Binary Search
def binarySearch(anArray, item):
  lowerIndex = 0
  upperIndex = len(anArray) - 1

  while lowerIndex <= upperIndex:
    middleIndex = (lowerIndex + upperIndex) // 2

    if item == anArray[middleIndex]:
      return middleIndex
    elif item < anArray[middleIndex]:
      upperIndex = middleIndex - 1
    else:
      lowerIndex = middleIndex + 1

  return -1
#end binarySearch()

# Call main() to begin program
main()