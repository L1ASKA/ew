import timeit
from itertools import combinations
"Задание состоит из двух частей."
"1 часть – написать программу в соответствии со своим вариантом задания."
"Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение."
"2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум"
"одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения."
"IT-предприятие набирает сотрудников:"
" 2 тимлида, 2 проджек-менеджера, 2 синьера,"
" Сформировать все возможные варианты заполнения вакантных мест, если имеются 7 претендентов."
positions = {
    'team_leads': 2,
    'project_managers': 2,
    'seniors': 2
}

# Пример фиксированных приоритетов
prioritet = {
    'Иванов': 8,
    'Сидоров': 7,
    'Ушмаров': 9,
    'Жегалин': 6,
    'Васильева': 8,
    'Антипова': 7,
    'Илюшина': 9
}

# Пример специализаций
specializations = {
    'Иванов': ['leadership', 'project_management'],  # Тимлид, проджект-менеджер
    'Сидоров': ['programming', 'project_management'],  # Программист, проджект-менеджер
    'Ушмаров': ['programming', 'leadership'],  # Программист, тимлид
    'Жегалин': ['testing', 'leadership'],  # Тестировщик, тимлид
    'Васильева': ['programming', 'project_management'],  # Программист, проджект-менеджер
    'Антипова': ['project_management', 'leadership'],  # Проджект-менеджер, тимлид
    'Илюшина': ['programming', 'leadership']  # Программист, тимлид
}


def generate_combinations(specialists, position_counts):
    if len(specialists) < sum(position_counts.values()):
        print("Недостаточно специалистов для заполнения всех позиций.")
        return []

    team_leads = combinations(specialists, position_counts['team_leads'])
    project_managers = combinations(specialists, position_counts['project_managers'])
    seniors = combinations(specialists, position_counts['seniors'])

    all_combinations = []

    for leads in team_leads:
        remaining_after_leads = [s for s in specialists if s not in leads]
        for managers in combinations(remaining_after_leads, position_counts['project_managers']):
            remaining_after_managers = [s for s in remaining_after_leads if s not in managers]
            for senior in combinations(remaining_after_managers, position_counts['seniors']):
                all_combinations.append({
                    'team_leads': leads,
                    'project_managers': managers,
                    'seniors': senior
                })

    return all_combinations


def func(specialists, position_counts):
    all_combinations = []

    for leads in combinations(specialists, position_counts['team_leads']):
        remaining_after_leads = [s for s in specialists if s not in leads]

        for managers in combinations(remaining_after_leads, position_counts['project_managers']):
            remaining_after_managers = [s for s in remaining_after_leads if s not in managers]

            for seniors in combinations(remaining_after_managers, position_counts['seniors']):
                all_combinations.append({
                    'team_leads': leads,
                    'project_managers': managers,
                    'seniors': seniors
                })

    return all_combinations


def res_first_ch(specialists):
    print(f'\n1 часть задания. Программа без усложнения и без целевой функции.\n\nВсевозможные варианты заполнения вакантных мест:')

    start_time = timeit.default_timer()
    variants = generate_combinations(specialists, positions)

    for variant in variants:
        print(f'Тимлиды: {variant["team_leads"]}, Проджект-менеджеры: {variant["project_managers"]}, '
              f'Синьоры: {variant["seniors"]}')

    time_a = timeit.default_timer() - start_time
    print(f'\nКоличество комбинаций: {len(variants)}')
    print(f'Время выполнения программы: {time_a:.6f} секунд')

    start_time = timeit.default_timer()
    print('\nФункциональный метод')
    variants = func(specialists, positions)

    for variant in variants:
        print(f'Тимлиды: {variant["team_leads"]}, Проджект-менеджеры: {variant["project_managers"]}, '
              f'Синьоры: {variant["seniors"]}')

    time_f = timeit.default_timer() - start_time
    print(f'\nКоличество комбинаций: {len(variants)}')
    print(f'Время выполнения программы: {time_f:.6f} секунд')


def targ_with_constraints(specialists):
    max_priority = 0
    best_combination = None
    count = 0

    print('\nВсевозможные подходящие комбинации специалистов:\n')

    for leads in combinations(specialists, positions['team_leads']):
        if not all('leadership' in specializations[lead] for lead in leads):  # Ограничение для тимлидов
            continue
        remaining_after_leads = [s for s in specialists if s not in leads]

        for managers in combinations(remaining_after_leads, positions['project_managers']):
            if not all('project_management' in specializations[manager] for manager in managers):  # Ограничение для проджект-менеджеров
                continue
            remaining_after_managers = [s for s in remaining_after_leads if s not in managers]

            for seniors in combinations(remaining_after_managers, positions['seniors']):
                if not all('programming' in specializations[senior] for senior in seniors):  # Ограничение для синьоров
                    continue
                count += 1
                combination = [*leads, *managers, *seniors]
                total_priority = sum(prioritet[specialist] for specialist in combination)
                if total_priority > max_priority:
                    max_priority = total_priority
                    best_combination = combination
                print(f'Комбинация: {combination}, Приоритет: {total_priority}')

    print(f'\nОптимальная комбинация: {best_combination}, Максимальный приоритет: {max_priority}')
    print(f'Количество подходящих комбинаций: {count}')
    return count


# Основная программа
print('Фамилии 7 претендентов: ')
specialists = ['Иванов', 'Сидоров', 'Ушмаров', 'Жегалин', 'Васильева', 'Антипова', 'Илюшина']
print(specialists)

while True:
    choice = input(
        'Выберите, какую часть программы вы хотите выполнить: \n"1" - 1 часть\n"2" - 2 часть\n"3" - выход:\n')
    if choice == '1':
        res_first_ch(specialists)
    elif choice == '2':
        print('\n2 часть задания. Программа с усложнением и с целевой функцией.\n')
        count = targ_with_constraints(specialists)
        print(f'Количество комбинаций: {count}')
    elif choice == '3':
        break
    else:
        print('Вы ввели некорректные данные. Попробуйте снова.')
