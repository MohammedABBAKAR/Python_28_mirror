# Mirror Array
# Given an integer list, transform it into a mirror.

# Examples
# mirror([0, 2, 4, 6]) ➞ [0, 2, 4, 6, 4, 2, 0]

# mirror([1, 2, 3, 4, 5]) ➞ [1, 2, 3, 4, 5, 4, 3, 2, 1]

# mirror([3, 5, 6, 7, 8]) ➞ [3, 5, 6, 7, 8, 7, 6, 5, 3]



# ////////////////////////////////////////////////////////////////////


def mirror(lst):
    lst2 = lst
    lst2.reverse()
    return  lst.extend(lst2)
print(mirror([3, 5, 6, 7, 8]))


def mirror(lst):
    
    lst2 = list(reversed(lst)) 


print(mirror([3, 5, 6, 7, 8])) 



# ////////////////////////////////////////////////////////////////////




def mirror(lst):
    
    mirrored_list = lst.copy()  
    
    for item in reversed(lst):
        mirrored_list.append(item)
    
    return mirrored_list
print(mirror([3, 5, 6, 7, 8])) 
# ////////////////////////////////////////////////////////////////////