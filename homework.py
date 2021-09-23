def showCart(cart):
    print(f"Your cart contains: {cart}")

def addCart(cart, add):
    print(f"{add} has been added to your list!")
    return cart.append(add.lower().strip())

def deleteCart(cart, delete):
    print(f"{delete} has been removed!")
    return cart.remove(delete.lower())    

def shoppingCart():
    myShoppingCart = []
    user_input = input("Do you want to Show, Add, Delete, Clear or Quit?: ")

    while user_input.lower().strip() != 'quit':
        if user_input.lower().strip() == 'show':
            showCart(myShoppingCart)
            user_input = input("Do you want to Show, Add, Delete, Clear or Quit?: ")
        elif user_input.lower().strip() == 'add':
            add_item = input("What would you like to add? ")
            addCart(myShoppingCart, add_item) 
            user_input = input("Do you want to Show, Add, Delete, Clear or Quit?: ")    
        elif user_input.lower().strip() == 'delete':
            remove_item = input("What would you like to remove? ")
            deleteCart(myShoppingCart, remove_item) 
            user_input = input("Do you want to Show, Add, Delete, Clear or Quit?: ")  
        elif user_input.lower().strip() == 'clear':
            print("Your cart is now empty!")
            myShoppingCart = []
            user_input = input("Do you want to Show, Add, Delete, Clear or Quit?: ") 
        else:
            print("Huh?")
            user_input = input("Do you want to Show, Add, Delete, Clear or Quit?: ")  

shoppingCart()
print("Thank you for shopping with us!")

