from nltk.sem.logic import *

def pl_true(expression: Expression, model):
    if isinstance(expression, FunctionVariableExpression):
        return model[str(expression)]
    if isinstance(expression, NegatedExpression):
        return not pl_true(expression.term, model)
    if not isinstance(expression, BinaryExpression):
        return "Fail"

    first = pl_true(expression.first, model)
    second = pl_true(expression.second, model)

    if isinstance(expression, AndExpression):
        return first and second
    if isinstance(expression, OrExpression):
        return first or second
    if isinstance(expression, ImpExpression):
        return (not first) or second
    if isinstance(expression, IffExpression):
        return first == second

sentence = "(A->C)<=>-(B->D)"
model = {"A": False, "B": False, "C": True, "D": False}
print(pl_true(LogicParser().parse(sentence), model))
