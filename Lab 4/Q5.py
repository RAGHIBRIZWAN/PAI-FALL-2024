class Restaurant:
    menu_items = []
    book_table = []
    customer_orders = []
    check = True
    yes = True
    while(yes):
        def add_item_to_menu(self):
        a = int(input('Enter the menu items: '))
        menu_items.append(a)
        print('Item added successfully!')
        
    def book_tables(self):
        while(check):
            a = int(input('Enter the table number you want to book: '))
            if(!find(a)):
            book_table.append(a)
            print('Your table is booked!')
            check = False
        else:
            print('Sorry! Table is already booked!')
        
    def customer_order(self):
        a = int(input('Enter the number of items: '))
        for i in range(a):
            b = str(input('Enter the name of meal: '))
            for j in range(len(menu_items)):
                if(b == menu_items[j]):
                    customer_orders.append(b)
                    print(f"{b} is available")
                    break
                else:
                    print(f"{b} is not available")
                    
                    
