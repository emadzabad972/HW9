# .1 רשימות חלק ב'-
# a. ייצר רשימה ריקה של מספרים עשרוניים של טמפרטור ות
# b. קלוט מהמשתמש טמפרטורות עד אשר ייקלט המספר מינוס .999 כל טמפרטורה
# שנקלטה הוסף לרשימה. לא נוסיף טמפרטורה גדולה מ 50 או קטנה ממינוס 50
# c. הוסף את רשימת הטמפרטורות הבאה בסוף הרשימה הנוכחית: ],18.5 ,39.1 -20.0[
# )רמז extend )
# d. מה ההבדל בין extend לבין פעולת ) +( בין רשימות : לדוגמא [4,5,6]+[1,2,3]?
# e. הדפס את הטמפרטורה: הגבוהה ביותר )רמז max), הנמוכה ביותר )רמז min )
# f. בדוק אם הטמפרטורה 18.5 ברשימה )רמז in). אם כן הדפס True אחרת False
# g. ספור כמה פעמים חוזרת הטמפרטורה -20.0 )רמז count)
# h. הדפס את ממוצע הטמפרטורות באמצעות sum ו- len
# i. הדפס כל טמפרטורה בשורה נפרדת ) רמז: each for )
# j. מצא את האינדקס של הטמפרטורה 39.1 )רמז index )
# k. הסר את הטמפרטורה באינד קס 0 )רמז del )
# l. הסר את הטמפרטורה בכל אינדקס זוגי )רמז :2 del )
# m. הסר את טמפרטורה 18.5 )רמז remove ). מדוע כדאי לבדוק אם קיים לפני remove?
# n. שלוף את הטמפרטורה האחרונה ברשימה לתוך תא זיכרון בשם last_temp( רמז pop )
# o. שכפל את הרשימה באמצעות copy, מיין את הרשימה החדשה שיצרת
# p. שכפל את הרשימה שוב באמצעות copy, מיין את הרשימה החדשה שיצרת בסדר הפוך

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
