def square_sum(numbers):
    sqNums = []
    for i in numbers:
        sqNums.append(i ** 2)

    return(sum(sqNums))

if __name__ == __name__:
    print(square_sum([1,2,6]))