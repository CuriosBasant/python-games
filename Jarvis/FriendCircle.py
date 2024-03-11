# import random

class Friend_Circle:
    def __init__(self):
        self.friends = []
        self.total = -1

    def create(self, size):
        for position in range(65, size + 65):
            self.friends.append(Friend(chr(position)))

    def get_friend_position_named(self, name):
        return self.friends[ord(name) - 65]


class Friend:
    circle = []
    total = -1

    def __init__(self, name, is_facing_inwards):
        self.name = name
        self._is_facing_inwards = None
        self.on_left = None
        self.on_opposite = None
        self.on_right = None

    @property
    def is_facing_inwards(self):
        return self._is_facing_inwards

    @attribute.setter
    def is_facing_inwards(self, value):
        if self._is_facing_inwards == value:
            return
        self._is_facing_inwards = value

        temp = self.on_left
        self.on_left = self.on_right
        self.on_right = temp

    def invert_face_direction(self):
        self.is_facing_inwards = not self.is_facing_inwards

        temp = self.on_left
        self.on_left = self.on_right
        self.on_right = temp

    def set_left_to(self, friend):
        friend.on_left = self
        self.on_right = friend

    def set_opposite_to(self, friend):
        self.on_opposite = friend
        friend.on_opposite = self

    def set_right_to(self, friend):
        pass

    @staticmethod
    def set_on_opposite(friend_A, friend_B):
        friend_A.on_opposite = friend_B
        friend_B.on_opposite = friend_A


dictionary = {
    1: 'ADJACENT',
    2: 'OPPOSITE',
    3: 'LEFT',
    4: 'RIGHT',
    5: 'INWARDS',
    6: 'OUTWARDS',
    7: 'nINWARDS',
    8: 'nOUTWARD'
}

VAL_OF_N = 2
fact_string = '2AB;72;1AC;6D;4BD;6C'
questions = '?2D;?3C;?4B;?5A;?6B'

all_facts = fact_string.split(';')

Friend.total = VAL_OF_N * 2
Friend.make_ordered_cicle()

for fact in all_facts:
    NUM = int(fact[0])
    friend_A = Friend.get_friend_named(fact[1])
    friend_B = Friend.get_friend_named(fact[2])
    if NUM == 0:
        pass
    elif NUM == 2:
        friend_A.on_opposite = friend_B
        friend_B.on_opposite = friend_A
    elif NUM == 3:
        friend_A.on_right = friend_B
        friend_B.on_left = friend_A
    elif NUM == 4:
        friend_A.on_left = friend_B
        friend_B.on_right = friend_A
    elif NUM == 6:
        friend_A.is_facing_inwards = False
    else:
        pass

""" for i in range_list:
    friend = friend_circle[i]

    opposite_index = (i + val_of_N) % num_of_friends
    friend.on_opposite = friend_circle[opposite_index]
    friend.on_left = friend_circle[(i + 1) % num_of_friends]
    friend.on_right = friend_circle[(i - 1) % num_of_friends] """
