def divisible_by_2(my_list=[]):
    n = []
    for i in my_list:
        if i % 2 == 0:
            n.append(1)
        else:
            n.append(0)
    return n
