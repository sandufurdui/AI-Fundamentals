from production import forward_chain 
import rules

answers = []

def tourist_type(input_str):
    tourist_types = {
        'mexican': 'mexican tourist',
        'turkish': 'is a turkish tourist',
        'chinese': 'chinese tourist',
        'naughty black': 'naughty black tourist',
        'educated black': 'educated black tourist'
    }
    
    for key in tourist_types:
        if key in input_str.lower():
            return tourist_types[key]
    
    return None


def ask_questions(tree, name):
    if tree is None:
        return False
    
    answer = input(tree.cargo.format(name) + '? y/n ')
    while answer not in ['y', 'n']:
        answer = input("Please enter 'y' or 'n': ")
    
    subtree_explored = False
    if answer == 'y':
        for subtree in tree.subtrees:
            if ask_questions(subtree, name):
                answers.append(tree.cargo.format(name))
                return True
            if answers and answers[-1] == tree.cargo.format(name):
                subtree_explored = True
        if not subtree_explored and not tree.subtrees:
            answers.append(tree.cargo.format(name))
            return True
    elif tree.right:
        if ask_questions(tree.right, name):
            return True 
    return False

results = []
while True: 
    print('Give name')
    name = input('Name: ')
    type_of_chain = input('Forward or Backward chain?(F/B):')
    if type_of_chain == "F":
        ask_questions(rules.tree, name)
        result = forward_chain(rules.RULES, answers)
        print(result)
        tourist_found = False
        for item in result:
            if 'tourist' in item:
                tourist_found = True
                if 'mexican tourist' or 'is a turkish tourist' or 'chinesse tourist' or 'naughty black tourist' or 'educated black tourist' in item:
                    print(item)
        else:
            print('It is not a tourist')
  

    else:
        from backchain import backchain_to_goal_tree
        tourist_types = {
            "educated black": '(?y) is an educated black tourist',
            "naughty black": '(?y) is a naughty black tourist',
            "chinese": '(?y) is a chinesse tourist',
            "turkish": '(?y) is a turkish tourist',
            "mexican": '(?y) is a mexican tourist'
        }
        tourist_type = input('What type of tourist are you? ') 
        hypothesis = tourist_types[tourist_type.lower()] 
        result = backchain_to_goal_tree(rules.RULES, hypothesis)
        print(result)

    answers = []
