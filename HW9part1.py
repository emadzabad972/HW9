# start

list1: list[float] = []
while True:
    temperature: float = float(input('whats the temperature? '))
    if temperature == -999:
        break
    if not -50 <= temperature <= 50:
        print('not in range! try again ')
        continue
    list1.append(temperature)
print()
print(list1)
list1.extend([18.5, 39.1, -20.0])
print()
print('after extending: ', list1)
print()
# המשפט למטה הוא תשובה לחלק D מהשאלה.
print(
    'the difference between the extend function and "+" is that in the extend it changes the existing list ; while "+" creates a whole new list.')
print()
print(f'the highest temperature is : {max(list1)} and the lowest temperature is : {min(list1)}')
print()
print('is temperature 18.5 in the list? ', 18.5 in list1)
print()
print('how many times was the temperature -20.0 in the list:', list1.count(-20.0))
print()
print(f'the average of the temperatures is: ', sum(list1) / len(list1))
print()
for temperature in list1:
    print(temperature)
print()
print(f'whats the index for the value 39.1? ', list1.index(39.1))
del list1[0]
print('after deleting index 0 : ', list1)
del list1[1::2]
print('after deleting every even number :', list1)
for temperature in list1:
    if temperature == 18.5:
        list1.remove(temperature)
print('after removing the number 18.5 from the list: ', list1)
print('its better to check if the number exists before using the remove function because if the number doesnt exist the code will crash')
print()
last_temp = list1.pop()
print('the last temperature is: ', last_temp)
save_list = list1.copy()
list1.sort()
print('after sorting the list from lowest to highest: ', list1)
save_list2 = list1
list1.sort(reverse=True)
print('after sorting the list from highest to lowest :', list1)
