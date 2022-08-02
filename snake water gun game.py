from distutils.version import LooseVersion
import random

def snakewatergun(comp,mine):
    if(comp==mine):
        return None
    if(comp=='snake' and mine=='gun'):
        return True
    elif(comp=='water' and mine=='snake'):
        return True
    elif(comp=='gun' and mine=='water'):        
        return True
    else:
        return False  
choice=('snake', 'water', 'gun')
comp=random.randint(0,2)
comp=choice[comp]
mine=input('choose either snake, water or gun: ')
win=snakewatergun(comp, mine)   
if win is None:
    print("Match Drawn")
if win:    
    print("you win")
else:
    print(f"you chose {mine} and the computer chose {comp}")
    print("you lose")
