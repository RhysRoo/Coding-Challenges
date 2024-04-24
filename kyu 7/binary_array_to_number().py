def binary_array_to_number(arr):
    num = arr
    bin = []
    length = 0
    for x in num:
        bin.append(x)
        
    if bin[0] == 1:
            length += 8
    if bin[1] == 1:
            length += 4
    if bin[2] == 1:
            length += 2
    if bin[3] == 1:
            length += 1
            
    return length

if __name__ == "__main__":
    print(binary_array_to_number([0,0,0,1]))
    print(binary_array_to_number([0,0,1,0]))
    print(binary_array_to_number([1,1,1,1]))
    print(binary_array_to_number([0,1,1,0]))

