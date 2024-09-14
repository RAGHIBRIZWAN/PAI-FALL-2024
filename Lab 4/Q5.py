class Restaurant:
    menu_items = []
    book_table = {}
    customer_orders = {}
    check = False

    def add_item_to_menu(self,item):
        self.menu_items.append(item)
        
    def book_tables(self,tableNum):
        while(self.check):
            if self.book_table['Table' + str(tableNum) == 'Booked']:
                print('Sorry! Table is already booked!')
        else:
                self.book_table['Table' + str(tableNum)] = 'Booked'
                print('Your table is booked!')
                check = False
        
    def customer_order(self,meal,quantity):
        self.customer_orders[meal] = quantity

    def show_Menu(self):
         print(f"Menu: {self.menu_items}")
        
    def show_Booked_Tables(self):
         print(f"Booked Tables: {self.book_table}")

    def show_Customer_Order(self):
         print(f"Customer Order: {self.customer_orders}")

cust1 = Restaurant()
cust1.add_item_to_menu('Biryani')                    
cust1.add_item_to_menu('Zarda')                    
cust1.add_item_to_menu('Korma')                    
cust1.add_item_to_menu('Roti')
cust1.add_item_to_menu('Pizza')
cust1.add_item_to_menu('Burger')
cust1.book_tables(1)

cust1.customer_order('Biryani',2)
cust1.customer_order('Korma',2)
cust1.customer_order('Roti',10)

cust1.show_Menu()
cust1.show_Booked_Tables()
cust1.show_Customer_Order()
