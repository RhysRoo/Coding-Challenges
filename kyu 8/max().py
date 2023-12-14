# def combat(health, damage):
#     if (health - damage) <= 0:
#         return 0
#     else:
#         return  health - damage
    
def combat(health, damage):
    return max(0, health-damage)
    
if __name__ == "__main__":
    print(combat(100, 20))