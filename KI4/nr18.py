from nltk.sem.logic import *

import Logic_calculator
from nr16 import pl_true

import copy


# Ermittle die Menge aller verwendeten Symbole einer Expression, schneide automatisch das "NOT" davor weg, sollte dieses dabei sein
def get_all_symbols(expression: Expression):
    if isinstance(expression, FunctionVariableExpression):
        return set(str(expression))
    if isinstance(expression, NegatedExpression):
        return get_all_symbols(expression.term)
    if not isinstance(expression, BinaryExpression):
        raise Exception("Invalid Argument")

    return set.union(get_all_symbols(expression.first), get_all_symbols(expression.second))


# Implementierungs des Pseudocodes aus den Vorlesungsfolien
def tt_entails(knowledge_base, alpha):  # Starte den rekursiven Algorithmus tt_check_all, mit ermittelten Startwerten
    alpha = LogicParser().parse(alpha)
    symbols = list(set.union(get_all_symbols(knowledge_base), get_all_symbols(alpha)))
    return tt_check_all(knowledge_base, alpha, symbols, {})


def tt_check_all(knowledge_base, alpha, symbols, model):
    if not symbols:
        if pl_true(knowledge_base, model):
            alphaboolean = pl_true(alpha, model)
            print(str(model) + ", KB == True,"+" Alpha == " + str(alphaboolean))
            return alphaboolean
        else:
            alphaboolean = pl_true(alpha, model)
            print(str(model) + ", KB == False,"+" Alpha == " + str(alphaboolean))
            return True
    else:
        symbols_copy = symbols.copy()
        first = symbols_copy.pop()
        rest = symbols_copy

        model_copy = copy.deepcopy(model)
        model[first] = True
        result_one = tt_check_all(knowledge_base, alpha, copy.copy(rest), model)
        model_copy[first] = False
        result_two = tt_check_all(knowledge_base, alpha, copy.copy(rest), model_copy)

        return result_one and result_two


#parse_string = "(A ->B) & D"
calculator = Logic_calculator.LogicCalculator()
#KB = calculator.init(parse_string)
#KB = calculator.init("(A | B | C) & (A | B | -C) & ( -A | B | C) & (-A | -B | -( -C ))")
#KB = calculator.tell(KB,"(A | B | C) & ( ( A | B | -C ) & ( -A | B | C ) ) & (-A | -B | C)")
#KB = calculator.tell(KB,"(A | B | C) & ( A | -C ) & (-A | B | C | D) & (-A | -B | C)")
#KB = calculator.tell(KB,"(A | B | C) & ( A | -C ) & ( -A | B & C | D ) & ( -A | -B | C)")
#KB = calculator.tell(KB,"(A | B | C) & ( A | -C ) & ((-A | B) & (C | D)) | (-A | -B | C)")
#KB = calculator.tell(KB,"(A | B | C) & ( A | -C ) & ( ( (-A | B) & C) | D) & (-A | -B | C)")

KB = calculator.init("(A | B | C) & (A | B | -C) & (-A | B | C) & (-A | -B | -(-C))")
KB = calculator.tell(KB,"(A | B | C) & (A | B | -C) & (-A | B | C) & (-A | -B | C)")
KB= calculator.tell(KB,"(A | B | C) & (A | -C) & (-A | B | C | D) & (-A | -B | C)")
KB= calculator.tell(KB,"(A | B | C) & (A | -C) & (-A | B & C | D) & (-A | -B | C)")
KB= calculator.tell(KB,"(A | B | C) & (A | -C) & ((-A | B) & (C | D)) | (-A | -B | C)")
KB= calculator.tell(KB,"(A | B | C) & (A | -C) & (((-A | B) & C) | D) & (-A | -B | C)")
alpha = "A->(B->(C->D))"
#print(tt_entails(KB, "A -> D"))
print(tt_entails(KB,alpha))