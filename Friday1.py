def duplicates(names):
    new_list = []
    for x in names:
        if x not in new_list:
            new_list.append(x)
    print(new_list)
    return

test = ["Alex","John","Mary","Steve","John", "Steve"]

duplicates(test)