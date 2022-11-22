name=input("Enter your name:")
print(f"Hello {name}! Welcome to the guessing game!")
import random
play="Yes"
while play == "Yes":
    words=["guessing","apple","python","hello"]
    index=random.randint(0,len(words)-1)
    word=words[index]
    #can do random.sample(population,k)
    indexes= random.sample(range(0,len(word)),3)
    guesses= ""
    for i in indexes:
        guesses+=word[i]
    chances=10
    while chances>0:
        won=True
        for ch in word:
            if(ch in guesses):
                print(ch,end=" ")
            else:
                print("_",end=" ")
                won=False

        if won:
            print("\nYou Won!")
            print(f"Your score is {chances*10}")
            break

        #Take a guess from the user

        guess=input("\nGuess a character:")
        guesses += guess

        if guess not in word:
            chances-=1
            print("\nWrong Answer!")
            print(f"You have {chances} chances left!")

            if chances == 0:
                print("You Lose!")
                break

def play_again():
    global play
    play=input("Do you want to play again:")
    if play=="Yes":
        global chances,word,guesses
        chances=10
        index=random.randint(0,len(words))
        word=words[index]
        indexes=random.sample(range(0,len(word)),3)
        guesses=""
        for i in indexes:
            guesses+=word[i]
