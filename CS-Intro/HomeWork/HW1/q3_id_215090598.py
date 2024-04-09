price = float(input("enter the furniture price: "))
weight = float(input("enter the furniture weight: "))
floor = int(input("enter your floor number: "))
distance = float(input("enter your distance from the shop: "))
tip = price * 0.1
transport = floor * weight + 5 * distance
final_price = transport + tip + price
print(f"the final price is: {final_price} ILS")
