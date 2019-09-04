def is_grp_of_member(data,n):
    for x in data:
        if n == x:
            return True
    return False
print(is_grp_of_member((1,5,8,3),3))
print(is_grp_of_member((1,5,8,3),-1))

