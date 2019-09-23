def exponents(base_numb, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_numb
    return result

print(exponents(2, 9))