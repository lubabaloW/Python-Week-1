[2,3,4,5]
def multiply(*numbers):
    total =1
    for number in numbers:
      total *= numbers
    return total

    print(multiply(2,3,4,5))