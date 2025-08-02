grocery =[]
list_set = set()
total = 0

def add_items():
    item = input ("Enter a name: ").strip().title()
    if item in list_set:
        print("Item already exist.")
        return
    price = float(input("Enter Price: "))
    items = {
        "item" : item,
        "price" : price,
        "done" : False
    }
    grocery.append(items)
    list_set.add(item)
    print(f"Added: {item} : {price}")

def show_items():
    if not grocery:
        print("No items found!")
        return
    print("\n--All items--")
    for idx, items in enumerate(grocery, start=1):
        status = "Done!" if items["done"] else "Not Yet"
        print(f"{idx}. {items['item']} : {items['price']} [{status}]")
    print("-------------")

def total_cost():
    if not grocery:
        print ("No items to count!")
        return
    total = 0
    print("\n-- Total Cost--")
    for item in grocery:
        print(f"{item['item']} - $ {item['price']}")
        total += item['price']
    print("--------------")
    print(f"Total: ${total:.2f}")
    print("--------------")

def total_budget():
    if not grocery:
        print ("No items total compare!")
        return
    total = 0
    for item in grocery:
        total += item['price']
    budget = float(input("Enter your budget: "))

    if total == budget:
        print("You are exactly on budget!")
    elif total > budget:
        print(f"You are over budget by $ {total- budget:.2f}")
    else:
        print(f"You are under budget by $ {budget - total:.2f}")

def complete_item():
    show_items()
    num = input("Enter the item that is complete: ").title().strip()
    for item in grocery:
        if item['item'] == num:
            item["done"] = True
            print(f"Marked {num} as done")
            return
    print("Item not found!")
    print("--------------")    


    

    
    

        
        