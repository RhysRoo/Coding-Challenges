def between(a,b):
    array = []
    for i in range(a , b + 1 ):
        array.append(i)
        
    return array

if __name__ == "__main__":
    print(between(1,4))
    print(between(-2,2))
    print(between(1,1))
    print(between(1,2))
    print(between(1,3))
    print(between(1,5))