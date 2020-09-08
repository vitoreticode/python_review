# Remove items from list1 that are present in list2
for item in list1:
    if item in list2:
        list2.remove(item)

# Transfer items from list1 to list2
while len(list1) > len(list2):
    item_to_transfer = list1.pop()
    list2.append(item_to_transfer)
    