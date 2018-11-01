# Write a definition for a class of anything you want. You have to use the following methods:

# __init__ method that initializes some attributes. One of the attributes has to be an empty list.
# __str__ method that returns a string that reasonably represent the thing.
# A special method that overloads the one type of operators.
# Some other methods that reasonably represent the thing's actions, inclduing one method that takes an 
# object of any type and adds it to the attribute of type list.

# Test your code by creating two objects and using all the methods.

class SiddyG:
    """Sid is a super-cool dude
    
    attributes: favfoods, favmovies
    """
    
    def __init__(self, favfoods = None, favmovies = None):
        """initializes a list of my favorite foods
        favfoods: str
        favmovies: str
        """
        self.favfoods = []
        self.favmovies = []
        
    def put_in_favfoods(self, food):
        self.favfoods.append(food)
    
    def __str__(self):
        return "My fav foods are {} ".format(self.favfoods)


Sid = SiddyG()
Sid.put_in_favfoods("pie")
