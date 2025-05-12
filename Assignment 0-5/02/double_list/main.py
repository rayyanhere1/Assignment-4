def numbers_list(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[1]
    return numbers    

numbers = [1,2,3,4]
double_numbers = numbers_list(numbers)
print("Doubled list", double_numbers)