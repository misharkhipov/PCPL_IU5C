class Language:
    """Язык программирования"""
    def __init__(self, id, name, creator):
        self.id = id
        self.name = name
        self.creator = creator

class Library:
    """Библиотека"""
    def __init__(self, id, name, language_id):
        self.id = id
        self.name = name
        self.language_id = language_id

#Списки объектов классов с тестовыми данными
languages = [
    Language(1, 'Python', 'Guido van Rossum'),
    Language(2, 'Java', 'James Gosling'),
    Language(3, 'JavaScript', 'Brendan Eich'),
    #Добавьте другие языки здесь
]

libraries = [
    Library(1, 'NumPy', 1),
    Library(2, 'Pandas', 1),
    Library(3, 'Spring', 2),
    Library(4, 'React', 3),
    #Добавьте другие библиотеки здесь
]

#Создайте связующую таблицу между языками и библиотеками
language_libraries = [
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    # Добавьте связи между языками и библиотеками здесь
]

def main():
    """Основная функция"""
    
    #Соединение данных один-ко-многим
    one_to_many = [(l.name, lb.name) for l in languages for lb in libraries if l.id == lb.language_id]
    
    #Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, lb.name) for l_id, lb_id in language_libraries for l in languages for lb in libraries if l.id == l_id and lb.id == lb_id]
    
    many_to_many = sorted(many_to_many_temp, key=lambda x: x[0])
    
    #Задание Г1
    print('Задание Г1 - выводит языки программирования и связанные с ними библиотеки.')
    for lang in languages:
        lib_list = [lb.name for lb in libraries if lb.language_id == lang.id]
        print(f'{lang.name}: {lib_list}')

    #Задание Г2
    print('\nЗадание Г2 - выводит языки программирования с максимальным количеством библиотек, отсортированные по количеству библиотек.')
    lib_counts = [len([lb.name for lb in libraries if lb.language_id == lang.id]) for lang in languages]
    if lib_counts:
        max_lib_count = max(lib_counts)
        sorted_languages = [lang for lang in languages if len([lb.name for lb in libraries if lb.language_id == lang.id]) == max_lib_count]
        for lang in sorted_languages:
            lib_list = [lb.name for lb in libraries if lb.language_id == lang.id]
            print(f'{lang.name}: {lib_list}')

    #Задание Г3
    print('\nЗадание Г3 - выводит список связанных языков программирования и библиотек, отсортированный по языкам.')
    for i in many_to_many:
        print(i)

if __name__ == '__main__':
    main()
