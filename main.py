from chaining_dictionary import ChainingDictionary

def main():
    a = {2: 3, 'b': [1, 2], [1]: 2}
    print(a.__str__())
    dict = ChainingDictionary()
    dict.__add__('a', 1)
    dict.__add__('b', 2)
    dict.__add__(2, 3)
    items = []
    for i in dict.items():
        items.append(i)
    print(items)
    dict.__add__(9, 3)
    items = []
    for i in dict.items():
        items.append(i)
    print(items)
    print(dict[2])
    dict[2] = 4
    print(dict[2])
    print(dict.__str__())


if __name__ == '__main__':
    main()


