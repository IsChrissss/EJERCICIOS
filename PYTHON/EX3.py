def fact_dict(num):
    fact_dict = {}
    for i in range(1, num + 1):
        fact_dict[i] = i * i
    return fact_dict

num = int(input("Introduce a number: "))

print((fact_dict(num)))
print((fact_dict(6)))
