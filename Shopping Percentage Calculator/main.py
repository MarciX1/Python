import random

def currencyConverter():

    chooseCurrency = input("Which currency are you going to use? Choose *USD*, *EUR*, *HUF* ")

    if (chooseCurrency == "USD"):
        currency = "USD"
        amounts = [110, 85, 55, 30]
    elif (chooseCurrency == "EUR"):
        currency = "EUR"
        amounts = [105, 80, 50, 25]
    elif (chooseCurrency == "HUF"):
        currency = "HUF"
        amounts = [40000, 30000, 20000, 10000]
    else: 
        currency = "USD"
        amounts = [110, 85, 55, 30]

    calcPrice(currency, amounts)

def calcPrice(currency, amounts):

    list = []
    coupons = []
    for n in range(4):
        percentages = random.randint(1, 50)
        coupons += [percentages]
    coupons.sort(reverse=True)
    newCoupons = []

    for coupon in coupons:
        newPercentage = 100 - coupon
        newCoupons += [newPercentage]

    for x in range(10):
        prices = int(input("Item price: "))
        list += [prices]

    sumList = sum(list)

    if not coupons:
        print(f"You don't have any coupon, so your items in your cart will cost: {sumList} {currency}")
    else: 
        
        if (sumList >= amounts[0]):
            newPrice = round((sumList / 100)*newCoupons[0])
            saved = sumList - newPrice
            print(f"Old price: {sumList} {currency}, Discounted price: {newPrice} {currency}. You saved: {saved} {currency}")
            coupons.remove(coupons[0])
            print(f"Your remaining coupons: {coupons}")
        elif (sumList >= amounts[1]):
            newPrice = round((sumList / 100)*newCoupons[1])
            saved = sumList - newPrice
            print(f"Old price: {sumList} {currency}, Discounted price: {newPrice} {currency}. You saved: {saved} {currency}")
            coupons.remove(coupons[1])
            print(f"Your remaining coupons: {coupons}")
        elif (sumList >= amounts[2]):
            newPrice = round((sumList / 100)*newCoupons[2])
            saved = sumList - newPrice
            print(f"Old price: {sumList} {currency}, Discounted price: {newPrice} {currency}. You saved: {saved} {currency}")
            coupons.remove(coupons[2])
            print(f"Your remaining coupons: {coupons}")
        elif (sumList >= amounts[3]):
            newPrice = round((sumList / 100)*newCoupons[3])
            saved = sumList - newPrice
            print(f"Old price: {sumList} {currency}, Discounted price: {newPrice} {currency}. You saved: {saved} {currency}")
            coupons.remove(coupons[3])
            print(f"Your remaining coupons: {coupons}")
        else: 
            print(f"You can't use your coupon, so your items in your cart will cost: {sumList} {currency}")
    
currencyConverter()
