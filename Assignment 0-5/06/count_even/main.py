def count_even():
    lst = []
    
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        lst.append(int(user_input))
    
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    
    print("Number of even numbers:", even_count)

def main():
    count_even()

if __name__ == "__main__":
    main()
