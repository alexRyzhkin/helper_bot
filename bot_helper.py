# создаем словарь с задачами
schedule = {}

# вводим имя пользователя
name = input('What is you name?')

# выводим приветствие
print(f'''Привет, {name} Я твой бот-помощник.''')

# список задач
print('''
Я буду хранить данные о твоих задачах на день. 
Для упраления мной, используй такие команды:
1. Мои задачи
2. Задачи по одному из коллег
3. Добавить новую задачу
4. Добавить нового коллегу
5. Завершить работу''')

# начинаем бесконечный цикл
while True:
    # команда от пользователя
    command = int(input('Введите команду:'))

    # проверка условий
    if command == 1:
        # вывести все задачи
        print(f'Список дел на сегодня:')
        for name, tasks in schedule.items():
            print(f'''{name} {tasks}''')

    elif command == 2:
        # вывести задачи по одному коллеге
        name = input('Имя сотрудника:')
        print(f'''Список дел по сотруднику {name}''')
        for task in schedule[name]:
            print(task)

    elif command == 3:
        # добавить новую задачу
        name = input('Имя сотрудника:')
        task = input('Новая задача:')
        schedule[name].append(task)
        print('Список дел на сегодня:')
        for name, tasks in schedule.items():
            print(f'''{name} 
            {tasks}''')

    elif command == 4:
        # добавить нового пользователя
        name = input('enter new name of a person: ')
        schedule[name] = []
        print(f'''My businnes today: ''')
        for name, tasks in schedule.items():
            print(f'''{name}
            {tasks}''')

    elif command == 5:
        print('End of programm')
        # прирываем работу цикла
        break




