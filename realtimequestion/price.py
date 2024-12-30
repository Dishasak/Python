# def display_menu(products):
#     p



def add_items(products):
    name= input("enter the name of the product")
    if name in products:
        print("name already present")
    else:
        price= input(f"enter the price for the {name}")
        products[name] = price
        print("product details entered")
        
        
        
def retrive_items(products): #searching
        name = input("enter productname to view details ")
        if name in products:
            print(f"{name}: {product[price]}")
        else:
            print("product not found")
            
            
            
def view_all_items(products):
    if products:
        print("display all the items")
        for k,v in products.items():
            print(f"{k}:{v}")
    else:
        print("no items present in the cart")











def main():
    products={}
    print("welcome to the shop")
    while True:
        print ("1.additems\n2.view items\n3.retrive the details")
        choice = input("enter your choice: ")
        
        if choice =='1':
            add_items(products) #adding the item and their price
        elif choice == '2':
            retrive_items(products) #by name getting its price
        elif choice == '3':
            view_all_items(products) #displaying all the details of the item
        else:
            print("invalid choice")
            
            
            
if __name__ == "__main__":
    main()
