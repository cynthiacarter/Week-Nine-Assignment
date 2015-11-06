# Week Nine
# By Cynthia Carter and Marisa Gross
# A program that finds the anagrams
# CS 125 fall 2015 

# Defined sortString converted Str to a list.
def sortString(aString):
    aList = list(aString)
    # Sorted list and converted list back into a str
    aList.sort()
    # Returned Str
    return ("".join(aList))
# Define fillVWords function
def fillVWords(fileName, aDict):
    # fileName read it
    file = open(fileName , "r")
    # Go through each line of the file one by one
    for line in file:
       # Removes leading and tailing charactors, and makes the words all lowercase
        word = line.strip().lower()
        # If the first letter of the word starts with V then add the key (sortString(word)) and the value (word) to the dictionary
        if word [0] == "v":
            aDict [sortString(word)] = word
# Define main function
def main():
    # Declare aDict, fileName, and fillVWords function
    aDict = dict()
    fileName = "wordList.txt"
    fillVWords(fileName , aDict)
    # Open file and read it
    file = open("quizwords.txt", "r")
    # Go line by line and strip qw.txt of , tab , return, new line
    for line in file:
        word = line.strip(",\t\n \r").lower()
        print(word, aDict [sortString(word)])

main()