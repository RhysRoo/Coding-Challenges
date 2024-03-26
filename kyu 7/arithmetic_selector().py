#My Solution

# def arithmetic(a, b, operator):
#     if operator == "add":
#         return a + b
#     elif operator == "subtract":
#         return a - b
#     elif operator == "multiply":
#         return a * b
#     else:
#         return a / b

#Codewars Solution

def arithmetic(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]

if __name__ == "__main__":
    print(arithmetic(100, 2, "add"))
