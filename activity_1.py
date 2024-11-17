word = input("enter your word: ")
ch = input("enter the letter you want to see: ")
i =0
count= 0
while (i<len(word)):
    if (word[i]== ch):
        count = count + 1
    i=i+1

print(f"the letter {ch} has come in the word {word} {count} times")
