MAX_VALUE = 10000

def main():
    fib_0 = 0
    fib_1 = 1

    print(fib_0, fib_1, end=" ")

    while True:
        next_fib = fib_0 + fib_1
        if next_fib >= MAX_VALUE:
            break

        print(next_fib, end=" ")

        fib_0 = fib_1
        fib_1 = next_fib

if __name__ == '__main__':
    main()
