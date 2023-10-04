import random

def currencyConverter():

    chooseCurrency = input("Which currency are you going to use? Choose *USD*, *EUR*, *HUF* ")

    match chooseCurrency:
        case "USD":
            currency = "USD"
            amounts = [110, 85, 55, 30]
        case "EUR":
            currency = "EUR"
            amounts = [105, 80, 50, 25]
        case "HUF":
            currency = "HUF"
            amounts = [40000, 30000, 20000, 10000]
        case _:
            currency = "USD"
            amounts = [110, 85, 55, 30]

    calcPrice(currency, amounts)

def calcPrice(currency, amounts):

    coupons = []
    for n in range(4):
        percentages = random.randint(1, 50)
        coupons += [percentages]
    coupons.sort(reverse=True)
    print(coupons)
    newCoupons = []

    for coupon in coupons:
        newPercentage = 100 - coupon
        newCoupons += [newPercentage]

    list = []
    for x in range(int(input("Number of item: "))):
        prices = int(input(f"Item price ({currency}): "))
        list += [prices]

    sumList = sum(list)

    if not coupons:
        print(f"You don't have any coupon, so your items in your cart will cost: {sumList} {currency}")
    else: 
        
        # Végig megy annyiszor, amennyi item van az amountsba és, ha pl: sumlist nagyobb, mint az amounts 0. indexe, akkor a loop befejeződik.
        # Ha kisebb, akkor addig megy tovább még a sumlist nem nagyobb és, ha nagyobb lesz, akkor befejeződik.
        # Ha egyik se volt nagyobb, akkor kiírja az eredeti összeget.  
        
        for i in range(len(amounts)):
            if sumList >= amounts[i]:
                newPrice = round((sumList / 100) * newCoupons[i])
                saved = sumList - newPrice
                print(f"Old price: {sumList} {currency}, Discounted price: {newPrice} {currency}. You saved: {saved} {currency}")
                coupons.pop(i)
                print(f"Your remaining coupons: {coupons}")
                discountedList = []
                for item in list:
                    discountedItem = format((item/100)*newCoupons[i], ".2f")
                    discountedList += [f"{discountedItem} {currency}"]
                print(discountedList)
                break

        else: 
            print(f"You can't use your coupon, so your items in your cart will cost: {sumList} {currency}")
            print(f"Your remaining coupons: {coupons}")

    
currencyConverter()