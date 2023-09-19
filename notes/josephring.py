def jose(total, step):
    ls1 = [i for i in range(1, total + 1)]
    ls2 = []
    num = 1
    while len(ls1) > 1:
        this_one = ls1.pop(0)
        if num == step:
            ls2.append(this_one)
            num = 1
        else:
            num += 1
            ls1.append(this_one)
    return ls1[0]

print(jose(55, 4))
