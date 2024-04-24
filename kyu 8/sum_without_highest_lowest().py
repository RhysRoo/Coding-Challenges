# def sum_array(arr):
#     if arr == None:
#         return 0
#     elif len(arr) > 2:
#         med = sum(arr) - max(arr) - min(arr)
#         return med
#     else:
#         return 0

# codewars solution & my solution above ^^^

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

if __name__ == '__main__':
    print(sum_array([None]))
    print(sum_array([3, 5, 1]))