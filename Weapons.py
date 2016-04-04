class Item(object):
    def __init__(self, name):
        self.name = name
         
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
        
        
class one_hand(Weapons):
    def __init__(self, name, damage = 10, weight = 15):
        super(one_hand, self).__init__(name, damage = 10, weight = 15)
        
    
sword = two_hand(Weapons) 
axe = two_hand2(Weapons)
cross_bow = two_hand3(Weapons)
dagger = one_hand(Weapons) 

#WEAPON INVENTORY
class player(object):

    def __init__(self, name, weight, items):
        self.name = name
        self.weight = weight
        self.items = items 
     
    def inventory(self):
        for item in self.items:
            print item
         
    def take(self, new_item):
        if len(self.items)<self.weight:
            self.items.append(new_item)
        else:
            print "A weight limit has been reached. No more items can be taken. Leave some other weapons behind."
       
    def leave(self, old_item):
        if old_item in self.items:
            self.items.remove(old_item)
        else:
            print "Weapon not found."
              

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

     