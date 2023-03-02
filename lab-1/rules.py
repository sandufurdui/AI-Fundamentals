from production import IF, AND, THEN

RULES = (
    IF(AND('(?y) has backpack and camera'),  # tourist 
       THEN('(?y) is a tourist')),

    IF(AND('(?y) is a tourist',  # educated black tourist
           '(?y) knows who his father is',
           '(?y) has bachelor'),
       THEN('(?y) is an educated black tourist')),

    IF(AND('(?y) is a tourist',  # naughty black tourist
           '(?y) doesnt know who his father is',
           '(?y) sells drugs',
           '(?y) has dark past'),
       THEN('(?y) is a naughty black tourist')),

    IF(AND('(?y) is a tourist',  # chinesse tourist
           '(?y) eats bats',
           '(?y) started covid',
           '(?y) says nothing happened on 5th of June, 1989'),
       THEN('(?y) is a chinesse tourist')),

    IF(AND('(?y) is a tourist',  # turkish tourist
           '(?y) knows the difference between shaorma, doner and kebab',
           '(?y) wears fez',
           '(?y) hates kurdish'),
       THEN('(?y) is a turkish tourist')),

    IF(AND('(?y) is a tourist',  # mexican tourist
           '(?y) loves guacamole',
           '(?y) dances while making salsa',
           '(?y) immigrated to the US'),
       THEN('(?y) is a mexican tourist')),
)
 
class Tree:
    def __init__(self, cargo, *subtrees, right=None):
        self.cargo = cargo
        self.subtrees = subtrees
        self.right = right

    def __str__(self):
        return str(self.cargo)

tree = Tree('{0} has backpack and camera', 
            Tree('{0} knows who his father is', 
                Tree('{0} has bachelor')
                ),
            Tree('{0} doesnt know who his father is', 
                Tree('{0} sells drugs', 
                    Tree('{0} has dark past')
                    )
                ),
            Tree('{0} knows the difference between shaorma, doner and kebab', 
                Tree('{0} wears fez', 
                    Tree('{0} hates kurdish')
                    )
                ),
            Tree('{0} loves guacamole', 
                Tree('{0} dances while making salsa', 
                     Tree('{0} immigrated to the US')
                     )
                 ),
            Tree('{0} eats bats', 
                Tree('{0} started covid', 
                    Tree('{0} says nothing happened on 5th of June, 1989')
                    )
                )
            )
