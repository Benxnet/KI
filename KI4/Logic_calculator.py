from nltk.sem.logic import *
from nltk.tree import Tree


class LogicCalculator:
    parser = LogicParser()

    def parse(self, string):
        return self.parser.parse(string)

    def init(self, string):
        return self.parser.parse(string)

    def expression_to_tree(self, expression: Expression):
        if not isinstance(expression, BinaryExpression):
            return Tree("%s" % expression, ())
        knoten = expression.getOp()

        kind_knoten = [
            self.expression_to_tree(expression.first),
            self.expression_to_tree(expression.second)
        ]
        return Tree(knoten, kind_knoten)

    def tell(self, KB, expression):
        return AndExpression(KB, self.parser.parse(expression))


