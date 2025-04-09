PROMPT: str = "Hey there! What would you like me to do? 😊 "
JOKE: str = """😂 Here's a hilarious joke for you!  

A programmer's wife tells him:  
"Go to the store and buy a loaf of bread. If they have eggs, buy a dozen."  

He comes back with **13 loaves of bread.**  

She asks, "Why on earth did you buy 13 loaves of bread?"  

He replies: **"Because they had eggs!"** 🤦‍♂️😂"""

SORRY: str = "Oops! I’m a joke bot 🤖, and all I do is tell jokes! Try typing 'Joke'. 😁"

def main():
    user_input = input(PROMPT).strip()  
    if user_input.lower() == "joke":   
        print("\n" + JOKE)              
    else:
        print("\n" + SORRY)            

if __name__ == "__main__":
    main()
