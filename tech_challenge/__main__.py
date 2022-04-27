# __main__.py
from .flat_list import FlatList

nested_list = [1, [2, [3, [4, 5]]]]

if __name__ == '__main__':
    print('Nested list: ', nested_list)
    print()
    flatlist = FlatList()
    flatlist.list = nested_list
    final_flat_list = flatlist.list
    print('Flatten list: ', final_flat_list)