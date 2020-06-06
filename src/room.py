# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = None, n_to = None, s_to = None, e_to = None, w_to = None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        if items is None:
            self.items = []
        else:
            self.items = items


    def items_in_room(self):
        if self.items == []:
            print('Sorry, this room has no items')
        else: 
            print('This room contains these items:')
            for item in self.items:
                print(f'{item.name}, {item.description}')
                # print(item.description)
    