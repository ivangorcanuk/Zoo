# Программа поддреживает различные виды живых существ, и выводит информацию и различные отчеты
# о них пользователю. Каждое животное зоопарка имеет свою кличку, которую ему дают при добавлении
# сотрудники зоопарка. Также при поступлении каждое существо взвешивают и нумеруют, так что вес и номер
# также запоминается. При выселении, вся информация о существа удаляется из программы зоопарка. Все
# животные зоопарка делятся по различным группам на основании которых надо будет предоставлять статистику:
# хищники(с указание основной жертвы)
# нехищные(с указанием основноко типа пищи)
# наземные(с указанием где обитают лес\горы\степи и прочее)
# подводные(тип водоема проживания: речка, море, океан)
# крылатые(улетает ли на зимовку да\нет)
#
# В зоопарке содержатся следущие животные и информация о них
# 1. Попугаи
# 2. Выдры
# 3. Волки
# 4. Зайцы
# 5. Косули
# 6. Бизоны
# 7. Страусы
# 8. Дельфины
# 9. Тигры
# 10.Осьминоги
# 11.Журавли
# 12.Щуки
# 13.Зебры
# 14.Голуби
#
# Составить программу, которая помогла бы сотрудникам добавлять животных этих видов в ваш зоопарк,
# а также составляла бы статиску по количеству животных каждой группы, содержащихся на данный момент.
# Информация о животных должна сохраняться, чтобы при перезапуске программы работу можно было продолжать.
# Кроме этого, програма должна уметь отображать следубщий виды отчетов:
# 1. Топ 3 самых легких существа зоопарка
# 2. Топ 5 самых больших хищника
# 3. Сипсок имен нехищных существа
# 4. Список подводных существ по мере убывания их веса
# 5. Список наземных животных с именем каджого и местом обитания
from working_files import WorkingFiles, WorkingMethods
from animal_type import Ground, Underwater, Winged
listAnimal = WorkingFiles().reading()
# for name in listAnimal:
#     print(name.number, name.nickname, name.typeAnimal, name.predator,name.weight, name.dwells, name.climate, name.clasAnimal, name.migratory)

input('Добро пожаловать в зоопарк')

while True:
    menu = input('Выберите действие: 1) добавить животное\n'
                 '                   2) удалить животное\n'
                 '                   3) посмотреть животных\n')

    if menu == '1':
        typeAnimal = input('Выберите класс животного: 1) наземные\n'
                           '                          2) подводные\n'
                           '                          3) крылатые\n')
        clasAnimal = input('Дайте имя животному:\n')
        dwells = str()
        migratory = str()
        number = '47'

        if typeAnimal == 'наземные':
            dwells = input('Укажите среду обитания данного подвида: 1) леса\n'
                           '                                        2) горы\n'
                           '                                        3) степи\n')
        elif typeAnimal == 'подводные':
            dwells = input('Укажите среду обитания данного подвида: 1) реки\n'
                           '                                        2) моря\n'
                           '                                        3) океан\n')
        elif typeAnimal == 'крылатые':
            dwells = input('Укажите среду обитания данного подвида: 1) леса\n'
                           '                                        2) горы\n'
                           '                                        3) степи\n'
                           '                                        4) реки\n'
                           '                                        5) моря\n'
                           '                                        6) океан\n')
            migratory = input('Являются ли миграционными: 1) да\n'
                              '                           2) нет\n')

        climate = input('Укажите климатические условия: 1) теплый\n'
                        '                               2) холодный\n'
                        '                               3) умеренный\n')

        predator = input('Явлиется ли зверь хищником: 1) да\n'
                         '                            2) нет\n')

        weight = float(input('Укажите вес животного:\n'))

        nickname = input('Придумайте кличку для нового жителя зоопарка:\n')

        obj = WorkingMethods().registrationAnimal(number, nickname, typeAnimal, predator, weight, dwells, climate, clasAnimal, migratory)
        listAnimal.append(obj)

    if menu == '3':
        menu1 = input('Выберите действие: 1) просмотреть список всех животных\n'
                      '                   2) выбрать класс животного (наземный, подводный, крылатый)\n'
                      '                   3) просмотреть хищников (травоядный)\n'
                      '                   4) просмотреть рейтинг\n')

        if menu1 == '1':
            for name in listAnimal:
                print(name.number, name.nickname, name.typeAnimal, name.predator,
                      name.weight, name.dwells, name.climate, name.clasAnimal, name.migratory)

        elif menu1 == '2':
            menu1_2 = input('Выбрать класс животного: 1) наземный\n'
                            '                         2) подводный\n'
                            '                         3) крылатый\n')

            if menu1_2 == '1':
                for ground in listAnimal:
                    if ground.typeAnimal == 'наземный':
                        print(ground.number, ground.clasAnimal, ground.nickname)
            elif menu1_2 == '2':
                for underwater in listAnimal:
                    if underwater.typeAnimal == 'подводный':
                        print(underwater.number, underwater.clasAnimal, underwater.nickname)
            elif menu1_2 == '3':
                for winged in listAnimal:
                    if winged.typeAnimal == 'крылатый':
                        print(winged.number, winged.clasAnimal, winged.nickname)

        elif menu1 == '3':
            menu1_2 = input('Выберите тип: 1) хищник\n'
                            '              2) травоядный\n')
