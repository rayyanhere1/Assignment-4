def main():
    f = bool(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5.0/9.0

    print(f"Temperature in celcius is : {c}" )

if __name__ == "__main__":
    main()
