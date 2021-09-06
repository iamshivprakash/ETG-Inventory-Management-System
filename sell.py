import json


def view_products(record):
    print("Product ID".ljust(20, ' '), end=" ")
    print("Name of Product".ljust(20, ' '), end=" ")
    print("Price".ljust(20, ' '), end=" ")
    print("Expiry Date".ljust(20, ' '), end=" ")
    print("Available Stock".ljust(20, ' '))

    for product_id in record:
        print(str(product_id).ljust(20, ' '), end=" ")
        print(record[product_id]["Name of Product"].ljust(20, ' '), end=" ")
        print(str(record[product_id]["Price"]).ljust(20, ' '), end=" ")
        print(str(record[product_id]["EXP Date"]).ljust(20, ' '), end=" ")
        print(str(record[product_id]["Stock"]).ljust(20, ' '))


def buy_more():
    print("Enter Product ID to buy a product:")
    upid = input()
    print("Enter Number of Quantity:")
    uqty = int(input())
    generate_bill(uname, ucity, upid, uqty, data)


def generate_bill(name, city, p_id, qty, record):
    print("------------G-ONE STORE----------")
    print("-----Electronic Bill-----".rjust(30, ' '))
    p_name = record[p_id]["Name of Product"]
    p_price = record[p_id]["Price"]
    # record[p_id]["EXP Date"]
    original_stock = record[p_id]["Stock"]
    print("Customer Name:".ljust(20, ' '), name)
    print("Customer Address:".ljust(20, ' '), city)
    print("Product Name:".ljust(20, ' '), p_name)
    print("Product Price:".ljust(20, ' '), p_price)
    print("Product Quantity:".ljust(20, ' '), qty)
    print("".rjust(35, '-'))
    print("Billing Amount:".ljust(20, ' '), p_price * qty)
    print("".rjust(35, '-'))
    # *****************Updating record.json**************
    record[p_id]["Stock"] = original_stock - qty
    # print(record)
    update = json.dumps(record)
    update = update.replace('},', '},\n')
    fdw = open('record.json', 'w')
    fdw.write(update)
    fdw.close()
    # ****************** record.json updated **************
    # ****************** Adding sells to sell.json *********
    sd=open('sells.json','r')
    sells_record=sd.read()
    sells_record=json.loads(sells_record)
    no_of_sells_made=len(sells_record)
    sd.close()
    # print(no_of_sells_made)
    sells_values={"Customer Name":name,"Address":city,"Product ID":p_id,
                  "Product Name":p_name,"Billing Amount":p_price*qty}
    sells_record[1000+no_of_sells_made]=sells_values
    update_sells=json.dumps(sells_record)
    update_sells=update_sells.replace('},','},\n')
    # print(update_sells)
    sdu=open('sells.json','w')
    sdu.write(update_sells)
    sdu.close()

    # ****************** Added sells to sell.json **********
    print("Do you want to buy something more:(Y/N).")
    choice = input()
    if choice == "Y" or choice == "y":
        view_products(record)
        buy_more()
    else:
        print("Thank you for shopping with us")


fd = open('record.json', 'r')
data = fd.read()
data = json.loads(data)
fd.close()

view_products(data)
print("Enter your Details to buy a product:")
print("Your Name:")
uname = input()
print("Your City Name:")
ucity = input()
buy_more()
