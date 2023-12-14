def basic_op(operator, value1, value2):   
    return {
            '+': value1+value2,
            '-': value1-value2,
            '*': value1*value2,
            '/': value1/value2
        }[operator]

if __name__ == '__main__':
    val = basic_op('+', 2, 2)
    print(val)
