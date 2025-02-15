def invest(amount, rate, years):
    years = years + 1
    for i  in range(1, years):
        foyda = amount + rate * amount  # The formula to calculate the foyda
        amount = foyda # New amount will be equal to foyda of each year
        print(f"year {i}: ${round(foyda, 2)}") # print foyda

invest(100, .05, 4)