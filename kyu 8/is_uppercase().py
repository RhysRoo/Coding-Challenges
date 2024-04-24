# def is_uppercase(inp):
#     if inp == inp.upper():
#         return True
#     else:
#         return False
    
# codewars solution & my solution above ^^^

def is_uppercase(inp):
    return inp.upper()==inp    

if __name__ == "__main__":
    print(is_uppercase("c"))