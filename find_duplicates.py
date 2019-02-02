def find_duplicates(items1, items2):
    list=[]
    for number in items2:
        if number in items1:
            list.append(number)
    return list
print(find_duplicates([7,2,5],[2,4,7,8]))
