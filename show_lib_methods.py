from pipe import *

'''
###
traverse
Рекурсивно раскрывает коллекции в одну. Применима только к iterable.
###
map
Классическая map функция
###
where
Возвращает элементы, для которых выполнилось условие
###
take
Возвращает первые (если коллекция упорядочена) n элементов коллекции
###
skip
Пропускает n первых (если коллекция упорядочена) элементов коллекции и возвращает остальные
###
dedup
Возвращает уникальные элементы, применяя к ним функцию key, если такая указана
###
reverse
Меняет последовательность элементов на обрутную
###
t
Добавляет элемент к коллекции
###
permutations
Возвращает все возможные комбинации элементов
###
'''

def show_traverse():
    mixed_collection_1 = [1, 2, (3, 4), [10, 20, [22, [42]]]]
    mixed_collection_2 = (2, set((4, 5)), {202:200})

    result = (mixed_collection_1, mixed_collection_2) | traverse

    print('\n###### treverse ######\ninput:\n{}\n{}\noutput:'.format(mixed_collection_1,mixed_collection_2))
    print(list(result))

def show_map():
    numbers = range(10)

    result = numbers | map(lambda x: x**2 if x%2==0 else x**3)
    
    print('\n###### map ######\ninput:\n{}\noutput:'.format(list(numbers)))
    print(list(result))

def show_where():
    numbers = range(10)

    result = numbers | where(lambda x: x<=3)
    
    print('\n###### where ######\ninput:\n{}\noutput:'.format(list(numbers)))
    print(list(result))

def show_take():
    char_set = set(('a', 'b', 'c', 'd', 'e'))

    result = char_set | take(4)
    
    print('\n###### take ######\ninput:\n{}\noutput:'.format(char_set))
    print(list(result))

def show_skip():
    char_set = set(('a', 'b', 'c', 'd', 'e'))

    result = char_set | skip(3)
    
    print('\n###### skip ######\ninput:\n{}\noutput:'.format(char_set))
    print(list(result))

def show_dedup():
    numbers = [1, 2, 3, 4, 4, 5, 5, 6, 6, 4, 3, 5, 1]

    result = numbers | dedup

    print('\n###### dedup ######\ninput:\n{}\noutput:'.format(numbers))
    print(list(result))

def show_reverse():
    char_tuple = ('a', 'b', 'c', 'd', 'e')

    result = char_tuple | reverse

    print('\n###### reverse ######\ninput:\n{}\noutput:'.format(char_tuple))
    print(list(result)) 

def show_t():
    elements_tuple = (1,2, range(10), 'abcde', [6,5,4,3])
    additional_element_1 = {'a': 20, 'd': 30}
    additional_element_2 = 6000

    result = elements_tuple | t(additional_element_1) | t(additional_element_2)

    print('\n###### t ######\ninput:\n{}\n{}\n{}\noutput:'.format(elements_tuple, additional_element_1, additional_element_2))
    print(list(result))

def show_permutations():
    string = 'ABCD'

    result = string | permutations

    print('\n###### permutations ######\ninput:\n{}\noutput:'.format(string))
    print(list(result))


if __name__ == '__main__':
    show_traverse()
    show_map()
    show_where()
    show_take()
    show_skip()
    show_dedup()
    show_reverse()
    show_t()
    show_permutations()