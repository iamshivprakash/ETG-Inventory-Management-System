import json


def add_new_products(file):
    print("How many products do you want to add?")
    n = int(input())
    for i in range(n):
        print("Enter Product ID:")
        p_id = input()
        print("Enter Product Name:")
        p_name = input()
        print("Enter Product Price:")
        price = int(input())
        print("Enter Product mfg(d:m:yy):")
        mfg_date = input()
        print("Enter Product exp(d:m:yy):")
        exp_date = input()
        print("Enter Product Description:")
        desc = input()
        print("How many quantity do you want to add?")
        qty = int(input())
        values = {"Name of Product": p_name, "Price": price, "MFG Date": mfg_date, "EXP Date": exp_date,
                  "Description": desc, "Stock": qty}
        file[p_id] = values
    record = json.dumps(file)
    record=record.replace('},','},\n')
    fdw = open('record.json', 'w')
    fdw.write(record)
    fdw.close()


def add_existing_products(file):
    print("Enter Product ID:")
    p_id=input()
    print("Enter Quantity")
    a_qty=int(input())
    qty=file[p_id]["Stock"]
    update_qty=qty+a_qty
    file[p_id]["Stock"]=update_qty
    update=json.dumps(file)
    update=update.replace('},','},\n')
    fde=open('record.json','w')
    fde.write(update)
    fde.close()
    view_products(file)


def view_products(file):
    print("Product ID".ljust(20, ' '), end=" ")
    for product_id in file:
        item = file[product_id]
        for key in item:
            if key == "Description":
                continue
            elif key!="Stock":
                print(key.ljust(20, ' '), end=" ")
            else:
                print(key.ljust(20, ' '))
        break
    for product_id in file:
        print(str(product_id).ljust(20, ' '),end=" ")
        item = file[product_id]
        for key in item:
            if key=="Description":
                continue
            elif key!="Stock":
                print(f"{str(item[key]).ljust(20, ' ')}", end=" ")
            else:
                print(f"{str(item[key]).ljust(20, ' ')}")
    print()


def view_sells():
    sd=open('sells.json','r')
    sells_data=sd.read()
    sells_data=json.loads(sells_data)
    print("Order ID:".ljust(18,' '),end=" ")
    print("Customer Name:".ljust(18, ' '), end=" ")
    print("Customer Address:".ljust(18, ' '), end=" ")
    print("Product ID:".ljust(18, ' '), end=" ")
    print("Product Name:".ljust(18, ' '), end=" ")
    print("Billing Amount:".ljust(18, ' '))
    for order_id in sells_data:
        print(str(order_id).ljust(18,' '),end=" ")
        print(sells_data[order_id]["Customer Name"].ljust(18, ' '),end=" ")
        print(sells_data[order_id]["Address"].ljust(18, ' '),end=" ")
        print(sells_data[order_id]["Product ID"].ljust(18, ' '),end=" ")
        print(sells_data[order_id]["Product Name"].ljust(18, ' '),end=" ")
        print(str(sells_data[order_id]["Billing Amount"]).ljust(18, ' '))
    sd.close()


fd = open('record.json', 'r')
data = fd.read()
data = json.loads(data)
fd.close()
store_name="-------------Welcome To G-ONE STORE---------------"
store_name.rjust(30,'-')
print(store_name)
print("Type (a) to add products\nType (s) to see sells record\nType (v) to view products .")
choice=input()
if choice.lower()=="a":
    print("Type (n) to add new products\nType (e) to add existing products.")
    add_choice=input()
    if add_choice.lower()=="n":
        add_new_products(data)
        print("Product/s added successfully.\n")
        view_products(data)
    else:
        view_products(data)
        add_existing_products(data)
        print("Product/s quantity updated successfully.\n")
        view_products(data)
elif choice.lower()=="v":
    view_products(data)
else:
    view_sells()

