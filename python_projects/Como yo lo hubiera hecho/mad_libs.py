#concatenate strings 
paragraph = "Barcelona is the most famous futball team of _______"
print(paragraph)
input_word= input("Write a word that fill the blank space to complete the sentence: ")
print(paragraph.replace("_______", input_word))