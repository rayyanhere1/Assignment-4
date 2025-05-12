def add_three_copies(data_list, data):
    for i in range(3):
        data_list.append(data)
    

def main():
    message = input("Enter a message to copy: ")
    data_list = []

    print("\nList before:", data_list)
    add_three_copies(data_list, message)
    print("List after:", data_list)

if __name__ == '__main__':
    main()
