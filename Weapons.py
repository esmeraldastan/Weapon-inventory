class item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description 
        
class weapons(item):
    def __init__(self, name, description, damage, weight):
        super(weapons, self).__init__(name, description)
        self.damage = damage
        self.weight = weight

class two_hand(weapons):
        
        