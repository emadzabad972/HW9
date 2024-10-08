# start
numbers = []
while True:
    number: int = int(input('type a number: '))
    if number == -999:
        break
    if not 0 <= number <= 10:
        print('number not in range!')
        continue
    numbers.append(number)

    print('statistics: ', end="")
    for i in range(11):
        counts: int = numbers.count(i)
        if counts >= 1:
            print(f" [ {i} ]: {counts}", end=" ")
    print()


