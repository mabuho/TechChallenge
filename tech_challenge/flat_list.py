#main.py

''' Converts a nested list to a flat list '''

class FlatList(object):
    def __init__(self):
        self.final_list = []
        self.nested_list = []
        
    def __flat_list(self, nested_list):
        if self.__is_instance_of_list(nested_list):
            flat_list = []
            # Iterate all the elements in the nested_list
            for e in nested_list:
                # Evaluate if the type of the element is list
                if isinstance(e, list):
                    # Extend the flat list by adding contents of this element (list)
                    flat_list.extend(self.__flat_list(e))
                else:
                    # Append the elemengt to the list
                    flat_list.append(e)

            return flat_list

    def __is_instance_of_list(self, nested_list):
        if nested_list is None:
            raise Exception('Input should not be null.')
        if not isinstance(nested_list, list):
            raise TypeError('Input should be a list.')

        return True

    #getter for list
    @property
    def list(self):
        return self.__flat_list(self.nested_list)
    
    #setter for list
    @list.setter
    def list(self, list):
        if self.__is_instance_of_list(list):
            print('Flattening list... \n')
            self.nested_list = list

    
    