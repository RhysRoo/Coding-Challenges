# def set_alarm(employed, vacation):
#
#     if employed and vacation:
#         return False
#     elif employed and not vacation:
#         return True
#     elif not employed or vacation:
#         return False
#     elif not employed and vacation:
#         return False

#codewars solution & my solution above ^^^^
def set_alarm(employed, vacation):
    return employed and not vacation
    

if __name__ == '__main__':
    print(set_alarm(True, True))
    print(set_alarm(False, True))
    print(set_alarm(False, False))
    print(set_alarm(True, False))