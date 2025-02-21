#initialize an empty shopping cart as a list 
shopping_cart=[]

def add_to_cart(item, price):
    shopping_cart.append({"item": item, "price": price})
    print(f"{item} added to cart.")

#example usage
add_to_cart("product 1", 10.99)
add_to_cart("product 2", 5.99)

#display current cart contents 
print("Current Cart")
for item in shopping_cart:
    print(f"{item['item']}: ${item['price']}")

#calculate and display total price
total_price = sum(item["price"])
for item in shopping_cart:
 print(f"Total Price: ${total_price}")
