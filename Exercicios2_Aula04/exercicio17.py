def multiplos():
    result = []

    for num in range(1, 1001):
        if num % 5 == 0:
            if num % 3 != 0:
                result.append(num)

    return result

mult = multiplos()  
print(mult)