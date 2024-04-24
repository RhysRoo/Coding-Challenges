# def update_light(current):
#     lights = ['red', 'yellow', 'green']
    
#     if current == 'green':
#         return lights[1]
#     elif current == 'yellow':
#         return lights[0]
#     elif current == 'red':
#         return lights[2]

# codewars solution & my solution above ^^^

def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]
    
if __name__ == '__main__':
    print(update_light('green'))
    print(update_light('yellow'))
    print(update_light('red'))