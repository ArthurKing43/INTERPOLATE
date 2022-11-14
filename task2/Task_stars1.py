def converter(data): # функция перевода даты юлианской в григорианскую
    q = 2400000 + float(data)
    a = q + 32044
    b = abs((4 * a + 3) // 146097)
    c = a - abs(146097 * b // 4)
    d = abs((4 * c + 3) // 1461)
    e = c - abs(1461 * d // 4)
    m = abs((5 * e + 2) // 153)
    day = e - abs((153 * m + 2) // 5) + 1
    month = m + 3 - 12 * abs(m // 10)
    year = 100 * b + d - 4800 + abs(m // 10)
    hour = day % 1 * 24 + 12
    minute = hour % 1 * 60
    second = minute % 1 * 60
    return (f"{int(day // 1)}:{int(month // 1)}:{int(year // 1)} {int(hour // 1)}:{int(minute // 1)}:{int(second // 1)}    {data}     ")


n = open('task2_data.dat', 'r')
first_list = n.readlines()
second_list = []
names_list = []
filter_list = []
del first_list[0]
for elem in first_list:
    c = elem.split('    ')
    c[3] = c[3][0:len(c[3])-1]     #удаляет скрытый \n в конце
    second_list.append(c)
for row in second_list:
    names_list.append(row[0])
all_Names_list = set(names_list)
print(all_Names_list)
for name in all_Names_list:
    for row in second_list:
        if name == row[0]:
            filter_list.append(row[2])
    Filt = set(filter_list)
    Filt_1 = "".join(Filt) #сделает строчку
    Filt = Filt_1.split() #удалит пробелы и вернет список
    print(f" {name} : {Filt} ")
    filter_list.clear()
    Filt.clear()

# Сортируем наш файлик по возрастанию дат
hdj_unsorted_list =[]
hdj_sorted_list = []
sorted_list_of_all_information = []
for row in second_list:
    hdj_unsorted_list.append(float(row[1]))
hdj_sorted_list = sorted(hdj_unsorted_list)
for el in hdj_sorted_list:
    for i in hdj_unsorted_list:
        if el == i:
            num = hdj_unsorted_list.index(i)
            c = second_list[num]
            sorted_list_of_all_information.append(c)

user_name = input(f"В каталоге предсталвены следующие звёзды:{all_Names_list}. Введите интересующую вас звезду: ")

l = True #Проверка звезды на принадлежность к списку
while l == True:
    for name in all_Names_list:
        if user_name == name:
            l = False
            break
    if l == True:
        user_name = input("Данные не верны, попробуйте ещё раз:")
all_filters_list_with_space = []
for row in sorted_list_of_all_information:
    all_filters_list_with_space.append(row[2])
all_filters_list_str = "".join(all_filters_list_with_space)
all_filters_list = all_filters_list_str.split()

for name in all_Names_list: #Создание списка фильтров для выбранной звезды
    for row in sorted_list_of_all_information:
        if user_name == row[0]:
            filter_list.append(row[2])
    Filt = set(filter_list)
    Filt_1 = "".join(Filt)  # сделает строчку
    filters_for_chosen_star = Filt_1.split()  # удалит пробелы и вернет список


user_filters = input(f"Для звезды {user_name} предсталены следующие фильры: {filters_for_chosen_star}. Выберите желаемые фильтры через пробел: ")
filt_user_name_list = user_filters.split()
star_inf = open(f"{user_name} ---- {filt_user_name_list}.dat", "w")
star_inf.write(f"JrD                    JD 24...        ")

# Сортируем список звездных величин
all_mag_list_unsorted = []
for row in sorted_list_of_all_information:
    all_mag_list_unsorted.append(row[3])
Mag_1 = "".join(all_mag_list_unsorted)
all_mag_list = Mag_1.split()

#Распределяет звездные величины по столбцам в зависимости от принадлежности к фильтру
for k in filt_user_name_list:
        star_inf.write(f"  {k}         ")
star_inf.write("      \n")
for i in range(0,len(all_filters_list)):
    if user_name == sorted_list_of_all_information[i][0]:
        for fil in filt_user_name_list:
            if fil == all_filters_list[i]:
                star_inf.write(converter(sorted_list_of_all_information[i][1]))
                for fil in filt_user_name_list:
                    if fil == all_filters_list[i]:
                        star_inf.write(f"  {all_mag_list[i]}     ")
                    else:
                        star_inf.write("  ---      ")
                star_inf.write("\n")
star_inf.close()








