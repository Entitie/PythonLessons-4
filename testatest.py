def modify(lst):
    lst.append('new')
    return lst


my_list = [1, 2, 3]
mod_list = modify(my_list)

print('mod_lst =', mod_list)
print('my_list =', my_list)
