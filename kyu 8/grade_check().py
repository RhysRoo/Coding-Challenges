def final_grade(exam, projects):
    
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 or projects > 5 and projects < 10:
        return 90
    elif exam > 50 or projects > 2 and projects < 5:
        return 75
    else:
        return 0

if __name__ == "__main__":
    print(final_grade(55, 20))
