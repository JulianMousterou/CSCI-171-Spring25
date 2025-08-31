def stock_holder():
    stocks = []   
    print("Input the stocks for each day in ascending order.")

    while len(stocks)<=4:
        stockinput = float(input())
        stocks.append(stockinput)
       
       
 

    print("Which day would you like to find the price of?")

    daypick = int(input())

    print(stocks[daypick-1])




stock_holder()

