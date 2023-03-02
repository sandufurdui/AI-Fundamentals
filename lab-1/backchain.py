from production import OR, AND, match, populate, simplify

def backchain_to_goal_tree(rules, hypothesis):
    length = len(rules) 

    if length==0:
        return hypothesis
    tree = AND()
    
    for element in rules:
        con = element.consequent()
        mat = match(con[0], hypothesis)
        if mat is not None and len(mat)>=0:
            antec = element.antecedent()
            if isinstance(antec, list):
                sub = AND()
                if isinstance(antec, OR): sub = OR()
                for x in antec:
                    new_tree = backchain_to_goal_tree(rules, populate(x, mat))
                    sub.append(new_tree)
                tree.append(sub)
            else:
                new_tree = backchain_to_goal_tree(rules, populate(antec, mat))
                tree.append(AND(new_tree))
        else:
            tree.append(hypothesis)
    new = simplify(tree) 
    return new