def combo(a, b):
    if a == 0 or b == 0:
        return a + b
    elif a % 10 == b % 10:
        return combo(a // 10, b // 10) * 10 + a % 10  
    else:
        return  min(combo(a // 10, b) * 10 + a % 10,
                    combo(a, b // 10) * 10 + b % 10)

print('combo:',combo(531, 432))
