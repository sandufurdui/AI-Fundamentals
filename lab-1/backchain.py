def match(pattern, fact):
    if isinstance(pattern, str):
        return {pattern: fact} if pattern == fact else None
    elif isinstance(pattern, tuple) and isinstance(fact, tuple) and len(pattern) == len(fact):
        bindings = {}
        for p, f in zip(pattern, fact):
            sub_bindings = match(p, f)
            if sub_bindings is None:
                return None
            bindings.update(sub_bindings)
        return bindings
    else:
        return None

def populate(pattern, bindings):
    if isinstance(pattern, str):
        return bindings.get(pattern, pattern)
    elif isinstance(pattern, tuple):
        return tuple([populate(p, bindings) for p in pattern])
    else:
        return pattern

def simplify(exp):
    if isinstance(exp, tuple):
        exp = tuple(set([simplify(e) for e in exp if e != ()]))
        if len(exp) == 1:
            return exp[0]
        else:
            return exp
    else:
        return exp

def backward_chain(rules, hypothesis):
    for rule in rules:
        lhs, rhs = rule.antecedent(), rule.consequent()
        bindings = match(rhs, hypothesis)
        if bindings is not None:
            if lhs == ():
                return populate(rhs, bindings)
            else:
                results = []
                for subgoal in lhs:
                    new_hypothesis = populate(subgoal, bindings)
                    subresults = backward_chain(rules, new_hypothesis)
                    if subresults is not None:
                        results.append(subresults)
                if len(results) > 0:
                    return simplify(tuple(results))
    return None
