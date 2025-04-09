def main():
    print("Welcome to Mad Libs! Let's start a funny coding story! \n")

    language = input("Enter Your favourite programming language :")
    Developer = input("Enter your name :")
    Bug = input("Enter a bug name or issue :")
    solution = input("Enter a solution to fix the bug :") 
    

    story = f"Once upon a time, Their was a {Developer} who was coding in {language}, everything was going perfectly fine but suddenly a {Bug} appeared "\
            f"{Developer} tried to solve it but the bug won't go away, so he tried to {solution} " \
            f"and finally, it perfectly worked! 🚀 "
    

    print("Here's your story!📝 \n")
    print(story)

    print("\nThanks for playing Programming Mad Libs! Keep coding! 💻🎉")
    
if __name__ == '__main__' :
        main()




