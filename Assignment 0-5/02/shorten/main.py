MAX_LENGTH = 3  

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def main():
    lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']  # Example list
    print(f"Original list: {lst}")
    shorten(lst)
    print(f"List after shortening: {lst}")

if __name__ == '__main__':
    main()
