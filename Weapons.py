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
        
    def cut_off(self, target):
        target.damage(self.damage)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
sword = two_hand(Weapons) 
      
        
class two_hand2(Weapons):
    def __init__(self, name, damage = 50, weight = 80):
        super(two_hand2, self).__init__(name, damage = 50, weight = 80)
        
    def slaughter(self, target):
        target.damage(self.damage)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
axe = two_hand2(Weapons)
        
class two_hand3(Weapons):
    def __init__(self, name, damage = 55, weight = 100):
        super(two_hand3, self).__init__(name, damage = 55, weight = 100)
        
    def shoot(self, target):
        target.damage(self.damage)
        if target.health <= 0:
            return "0"
        else:
            return target.health
            
cross_bow = two_hand3(Weapons)
        
    
class one_hand(Weapons):
    def __init__(self, name, damage = 10, weight = 15):
        super(one_hand, self).__init__(name, damage = 10, weight = 15)
        
    def stab(self, target):
        target.damage(self.damage)
        if target.health <= 0:
            return "0"
        else:
            return target.health
        
dagger = one_hand(Weapons)

class one_hand2(Weapons):
    def __init__(self, name, damage = 20, weight = 0):
        super(one_hand2, self).__init__(name, damage = 20, weight = 0)
        
    def hit(self, target):
        target.damage(self.damage)
        if target.health <= 0 :
            return "0"
        else:
            return target.health
            
club = one_hand2(Weapons)
    

#HP OF ZOMBIE
class Zombie(object):
    def __init__(self, health = 5000, attack = 1500):
        self.health = health
        self.attack = attack 
        

    #COMMAND TO ATTACK     
    def attacks(self, target):
        target.damage(self.attack)
        if target.health <= 0:
            return "Enemy down!"
        else:
            return target.health
            
    #DAMAGE TAKEN   
    def damage(self, amount):
        self.health -= amount
        
zombie = Zombie()

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

     