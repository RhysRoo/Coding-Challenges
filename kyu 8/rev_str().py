def reverseStr(n):
    empty = []
    for i in range(n):
        empty.append(n - i)
    return empty

if __name__ == '__main__':
    print(reverseStr(10))