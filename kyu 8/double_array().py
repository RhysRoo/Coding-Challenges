# def maps(a):
#     numList = []
#     for i in a:
#         numList.append(i * 2)
        
#     return(numList)

# codewars solution:

def maps(a):
    return [i*2 for i in a]

if __name__ == '__main__':
    print(maps([9, 5, 15]))