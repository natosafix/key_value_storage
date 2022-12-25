from chaining_dictionary import ChainingDictionary

def main():
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


if __name__ == '__main__':
    main()


