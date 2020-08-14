
count = 0

while count < 10:
    print(count)
    count += 1



count_externo = 0
count_intenro = 0

while count_externo < 10:
    while count_intenro < 6:
        print(count_externo, count_intenro)
        count_intenro += 1

        if count_intenro >= 3:
            break

    count_externo += 1
    count_intenro = 0