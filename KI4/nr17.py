from nltk.sem.logic import *
from nltk import Valuation, Assignment, Model


def nltk_pl_true(expression, model):
    mitems = model.items()
    val = Valuation(mitems)
    dom = val.domain
    g = Assignment(dom)
    m = Model(dom, val)

    return m.satisfy(expression, g)


sentence = "(A | B | C) & (A | B | -C) & (-A | B | C) & (-A | -B | C)"
model = {"A": True, "B": False, "C": True}
print(nltk_pl_true(LogicParser().parse(sentence), model))