def usdcny(usd):  
    return "{:.2f} Chinese Yuan".format(float(usd * 6.75))

#code wars solution
# def usdcny(usd):
#     return f"{(usd * 6.75):.2f} Chinese Yuan"

if __name__ == "__main__":
    print(usdcny(15))