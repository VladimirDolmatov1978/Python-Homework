# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму двух чисел : ")) 
p = int(input("Введите произведение  двух чисел : ")) 

for x in range(1000):
    x = 1
    y = s - x
    while x <= s // 2:
        if   x * y == p:  
            print ( x , y)
            exit ()
                       
        else:
            x += 1
            y = s - x

print(f'  {(x , y)}')
