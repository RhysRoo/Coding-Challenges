# def sum_str(a, b):
#     if a == '' and b == '':
#         return '0'
#     elif a == '':
#         return str(b)
#     elif b == '':
#         return str(a)
    
#     return str(int(a)+int(b))

def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))

if __name__ == '__main__':

    print(sum_str('6','4'))
