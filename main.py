import csv


def add_item(name, price, qty):
    global s
    with open('grocery_store.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, price, qty])

def update_price(name, price):
    items = []
    with open('grocery_store.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row == []:
                continue
            if row[0] == name:
                row[1] = price
            items.append(row)
    with open('grocery_store.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item in items:
            writer.writerow(item)

def search_item(name):
    with open('grocery_store.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row == []:
                continue
            if row[0] == name:
                print(row[0], ':', row[1], ':', row[2])
                return
        print('Item not found')

def display_items():
    print('Name ', ' Price', ' Quantity')
    print('-'*50)
    with open('grocery_store.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row == []:
                continue
            print(row[0], ':', row[1], 'Rs',':', row[2])
    print('-'*50)

def bill(name):

    shopping_cart = []
    lst = []
    with open('grocery_store.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row == []:
                continue
            shopping_cart = list(row)
            
            if shopping_cart[0] == name:
                
                qnt = int(row[2])-1
                row[2] = str(qnt)

                
                total_price = 0
                print('\nShopping cart:')
                print('Name\tPrice')
                print(shopping_cart[0], ':', shopping_cart[1])
                
                total_price += int(shopping_cart[1])
                tax = total_price * 0.1
                total_price += tax
                print('Tax:', tax)
                print('Total price:', total_price, '( 10% tax included)')
                print('Are you sure to purchase?')
                inp = input('(Y/N) :')

                if inp.upper().strip() == 'Y':
                    print('Thank You for your purchase. Visit next time.')

                elif inp.upper().strip() == 'N':
                    print('Canceling payment... \n Done!')

                else:
                    print('Wrong Input')
                break


        else:
            print('Item not found')
            return

    


c = 'y'
while c == 'y':
    print('\nMenu:')
    print('1. Add a new item to the store')
    print('2. Update the price of an item')
    print('3. Search for an item')
    print('4. Display the list of items')
    print('5. Add an item to the shopping cart and buy')
    print('6. Exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        name = input('Enter the name of the item: ')
        price = input('Enter the price of the item: ')
        qty = input('Enter Initial Quantity:')
        add_item(name, price, qty)

    elif choice == '2':
        name = input('Enter the name of the item: ')
        price = input('Enter the new price of the item: ')
        update_price(name, price)
    elif choice == '3':
        name = input('Enter the name of the item: ')
        search_item(name)
    elif choice == '4':
        display_items()
    elif choice == '5':
        name = input('Enter the name of the item: ')
        bill(name)
    elif choice == '6':
        break
    else:
        print('Invalid input')
