import csv
from unicodedata import name

action = ''
result = True
'''items = [{'name':['Milk','Sugar','Flour','Coffe','Tea']}, {'quantity':[1,2,3,4,5]},{'unit':['ml','mg','mg','mg','lll']},{'unit_price':[1,2,3,4,5]}]'''

class Product:
    def __init__(self, id, name, quantity, unit, unit_price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit =  unit
        self.unit_price = unit_price

products =  [Product(id=1, name='Milk', quantity=1, unit='ml', unit_price=1), Product(id=2, name='Coffe', quantity=11, unit='ml', unit_price=3), Product(id=3, name='Sugar', quantity=1, unit='kg', unit_price=33), Product(id=4, name='Flour', quantity=12, unit='kg', unit_price=23)]
sold_items = []
    
#func that exports shop resouces status to the .csv file
def export_file_to_csv():
    with open('magazyn.csv', 'w', newline='') as csvfile:
        fieldnames = ['id','name','quantity','unit','unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for product in products:
            writer.writerow({'id':product.id, 'name':product.name, 'quantity':product.quantity, 'unit':product.unit, 'unit_price':product.unit_price})
        print('Successfully exported data to magazyn.csv.')

#func that imports shop resouces status from the .csv file
def import_items_from_csv(products=[]):
    with open('magazyn.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        products.clear()
        for row in reader:
            products.append(Product(id=row['id'], name=row['name'], quantity=int(row['quantity']), unit=row['unit'], unit_price=int(row['unit_price'])))
        #print('Successfully loaded data from magazyn.csv.')
        return products

#adding new items to shop func
def add_item(name='', quantity ='', unit='', unit_price=''):
    print('Adding to warehouse...')
    id = len(products) + 1
    products.append(Product(id=id, name=name, quantity=quantity, unit=unit, unit_price=unit_price))

    print('Successfully added to warehouse. The current status is: ')
    return products

#func that sums up the items that were sold
def sold_items_summary(id, name, quantity,unit,unit_price):
    sold_items.append(Product(id=id ,name=name, quantity=quantity, unit=unit, unit_price=unit_price))
 
#costs calculation func
def get_costs():
    list_of_costs = [product.quantity * product.unit_price for product in products]
    sum_of_costs = sum(list_of_costs)
    return sum_of_costs

#income calculation func
def get_income():
    list_of_income = [product.quantity * product.unit_price for product in sold_items]
    sum_of_income = sum(list_of_income)
    return sum_of_income

#revenue calculation func
def show_revenue():
    print('Revenue breakdown (PLN)')
    print(f'Income:', get_income())
    print(f'Costs:', get_costs())
    print('------------')
    print(f'Revenue:', get_income() - get_costs(),' PLN')

#selling items func
def sell_item(name, quantity_to_sell):
    name = name.capitalize()  
    i = len(products)
    id = len(products) + 1

    for product in products:
        if name != product.name:
            i -= 1
            if i == 0:
                print('There is no such product in the shop.')
        else:
            
            if product.quantity >= quantity_to_sell:
                product.quantity = product.quantity - quantity_to_sell
                print('Successfully sold', quantity_to_sell, 'of ', name)
                sold_items_summary(id, name, quantity_to_sell,unit = product.unit, unit_price = product.unit_price)
                get_items()
            else:
                buy_all = 'yes'
                if buy_all == 'yes':
                    product.quantity = product.quantity - quantity_to_sell
                    if product.quantity < 0:
                        quantity_to_sell = quantity_to_sell + product.quantity
                        product.quantity = 0
                        sold_items_summary(id, name, quantity_to_sell,unit = product.unit, unit_price = product.unit_price)
                else:
                    print('You can choose another item or different quantity. ')

#func that shows current shop resurces status 
def get_items():
    print('Name\tQuantity\tUnit\tUnit Price (PLN)')
    print('----\t--------\t----\t----------------')
    
    for item in products:
        print(item.name,'\t',item.quantity, '\t       ',item.unit,'\t',item.unit_price)

#function that triggers actions
def to_do(action):  
    if action == 'show':
        get_items()
    elif action == 'add':
        add_item()
    elif action == 'sell':
        sell_item()
    elif action == 'show rev':
        show_revenue()
    elif action == 'save':
        export_file_to_csv()
    elif action == 'load':
        import_items_from_csv(products)
    elif action == 'exit':
        return True
    else:
        return False


""" #main program logic
while to_do(action) != True:
    action = str(input('What would you like to do? ')) """