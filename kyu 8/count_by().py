# def count_by(x, n):
#     seq = []
#     for i in range(x, n * x + 1, x):
#         seq.append(i)   
#     return seq

#codewars solution, my solution is above ^^^
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

if __name__ == '__main__':
    print(count_by(2, 5))

