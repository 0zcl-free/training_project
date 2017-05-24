old_dict = {     #字典！
    "#1": 8,
    "#2": 4,
    "#4": 2
}

new_dict = {
    "#1": 4,
    "#2": 4,
    "#3": 2
}
old_dict.keys()
old_set = set(old_dict.keys())
new_set = set(new_dict.keys())
print("Old_dict and New_dict".center(50,'_'))
print(old_set)
print(new_set)

dellet = old_set.difference(new_set)
print("Should del %s" % dellet)

add = new_set.difference(old_set)
print("Should del %s" % add)

update = old_set.intersection(new_set)
print("Should update %s" % update)