from chaining_dictionary import ChainingDictionary

def main():
    dictionaty = ChainingDictionary()
    dictionaty.add('a', 1)
    dictionaty.add('b', 2)
    dictionaty.add(2, 3)
    items = []
    for i in dictionaty.items():
        items.append(i)
    print(items)
    dictionaty.add(9, 3)
    items = []
    for i in dictionaty.items():
        items.append(i)
    print(items)
    print(dictionaty[2])
    dictionaty[2] = 4
    print(dictionaty[2])
    print(dictionaty.__str__())


if __name__ == '__main__':
    main()


