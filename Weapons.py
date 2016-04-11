print '''
        Weapons Available:
            
            *axe
            *sword
            *cross_bow
            *dagger
            *club
        '''


class Item(object):
    def __init__(self, name):
        self.name = name
         
#Basic Attacks          
class defense(Item):
    
    def __init__(self, name, damage):
        super(defense, self).__init__(name)
        self.damage = damage
        
class punch(defense):
    
    def __init__(self, name, damage = 50):
        super(punch, self).__init__(name, damage = 500)
        
class kick(defense):

    def __init__(self, name , damage = 100):
        super(kick, self).__init__(name, damage = 100)
        
kick = kick(defense)
punch = punch(defense)
        

#WEAPONS AT USE
#SUPERCLASS                
class Weapons(Item):
    
    def __init__(self, name, damage, weight):
        super(Weapons, self).__init__(name)
        self.damage = damage
        self.weight = weight
         
#SUB_CLASSES        
class two_hand(Weapons):
    def __init__(self, name, damage = 100, weight = 150):
        super(two_hand, self).__init__(name, damage = 100, weight = 150)
        
        
class two_hand2(Weapons):
    def __init__(self, name, damage = 50, weight = 80):
        super(two_hand2, self).__init__(name, damage = 50, weight = 80)
        
class two_hand3(Weapons):
    def __init__(self, name, damage = 55, weight = 100):
        super(two_hand3, self).__init__(name, damage = 55, weight = 100)
        
class two_hand4(Weapons):
    def __init__(self, name, damage = 100, weight = 100):
        super(two_hand4, self).__init__(name, damage, weight = 100)
        
    
class one_hand(Weapons):
    def __init__(self, name, damage = 10, weight = 15):
        super(one_hand, self).__init__(name, damage = 10, weight = 15)
        
    
sword = two_hand(Weapons) 
axe = two_hand2(Weapons)
cross_bow = two_hand3(Weapons)
dagger = one_hand(Weapons)
club = two_hand4(Weapons)        

    
#CONSUMABLES   

#SUBCLASS
class Consumable(Item):
    
    def __init__(self, name, health):
        super(Consumable, self).__init__(name)
        self.health = health
        
class health_potion(Consumable):
    def __init__(self, name, health = 200):
        super(health_potion, self).__init__(name, health = 200)
        
health = health_potion(Consumable)

     