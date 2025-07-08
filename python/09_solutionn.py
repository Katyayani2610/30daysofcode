#list uniqueness checker : check if all elements in a list are unique if duplicate is found exit the loop andprint the duplicate
items=["apple", "mango"," banana", "orange"," apple"]
unique_item = set()
for item in items:
    if item in unique_item:
        print(f"Duplicate found: {item}")
        break
    unique_item.add(item)
