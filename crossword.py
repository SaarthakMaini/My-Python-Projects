import math
words=["apple","banana","coconut"]
score=10
word=words[math.randint(0,len(words))]
hidden_characters=[*word]
number_of_tries_left=10
while number_of_tries_left > 0:
    inputed_character=input("Guess the character:")
    if(inputed_character in hidden_characters):
        print("You guessed correctly!")
    else:
        print("Wrong! Score deducted by one")
        score--
    
    number_of_tries_left--

def display(hidden_characters,)
