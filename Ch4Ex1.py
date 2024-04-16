"""
Chapter 4, Exercise 1
Student Name: Alejandro Cabrera
Purpose: Read in a sentence from keyboard and compute the average word length
"""
#Prompt the user for a sentence
sentence = input("Please enter a sentence: ")

#split the sentence into a list of words
listOfWords = sentence.split()

#compute the total number of words
numOfWords = len(listOfWords)

#compute the total length of the words in the list
lengthOfWords = 0

for word in listOfWords:
    lengthOfWords += len(word)

#compute and display the average length
print("The average word length is",lengthOfWords/numOfWords)
