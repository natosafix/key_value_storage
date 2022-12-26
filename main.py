import gc

from chaining_dictionary import ChainingDictionary
from datetime import datetime


def main():
    iteration_count = 1000000
    gc.collect()
    chaining_dictionary = ChainingDictionary()
    start_time = datetime.now()
    for i in range(iteration_count):
        chaining_dictionary.add(i, i)
    print(f'ChainingDictionary method add worked '
          f'{(datetime.now() - start_time).total_seconds()} seconds')
    gc.collect()

    chaining_dictionary = ChainingDictionary()
    start_time = datetime.now()
    for i in range(iteration_count):
        chaining_dictionary[i] = i
    print(f'ChainingDictionary indexer add worked '
          f'{(datetime.now() - start_time).total_seconds()} seconds')
    gc.collect()

    dictionary = {}
    start_time = datetime.now()
    for i in range(iteration_count):
        dictionary[i] = i
    print(f'Python Dictionary indexer add worked '
          f'{(datetime.now() - start_time).total_seconds()} seconds')
    gc.collect()

    chaining_dictionary = ChainingDictionary()
    for i in range(iteration_count):
        chaining_dictionary.add(i, i)
    start_time = datetime.now()
    for i in range(iteration_count):
        chaining_dictionary[i]
    print(f'ChainingDictionary indexer get worked '
          f'{(datetime.now() - start_time).total_seconds()} seconds')
    gc.collect()

    dictionary = {}
    for i in range(iteration_count):
        dictionary[i] = i
    start_time = datetime.now()
    for i in range(iteration_count):
        dictionary[i]
    print(f'Python Dictionary indexer get worked '
          f'{(datetime.now() - start_time).total_seconds()} seconds')


if __name__ == '__main__':
    main()


