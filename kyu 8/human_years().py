def human_years_cat_years_dog_years(human_years):
    
    cat_years = 0
    dog_years = 0
    
    for i in range(human_years + 1): 
        if i == 1:
            cat_years += 15
            dog_years += 15
        elif i == 2:
            cat_years += 9
            dog_years += 9
        elif i > 2:
            cat_years += 4
            dog_years += 5
    
    return (f'Human Years: {human_years}, Cat Years: {cat_years}, Dog Years: {dog_years}')

if __name__ == '__main__':
     print(human_years_cat_years_dog_years(21))