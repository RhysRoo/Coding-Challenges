# def multiply(n):
#     output = n * 5
#     if output > 100:
#         return n * 5 ** 3
#     elif n == 10:
#         return n * 5 ** 2
#     return output

#chatgpt solution :( - Learning and comparing my code ^^^^

# def multiply(n):
#     # Calculating the number of digits in n
#     num_digits = len(str(abs(n)))

#     # Multiplying n by 5 raised to the number of digits
#     return n * (5 ** num_digits)

#codewars solution

def multiply(n):
  return n*5**len(str(abs(n))) 


if __name__ == '__main__':
    print(multiply(4))