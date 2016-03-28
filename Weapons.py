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
         def __init__(self, name = 'bow', description = 'kill' , damage = 50, weight = 100):
            super(two_hand, self).__init__(name = 'bow', description = 'kill' , damage = 50, weight = 100)
            
         def bow(self):
             print '%s can kill' 
            
        