from nltk.sem.logic import *
import Logic_calculator

calculator = Logic_calculator.LogicCalculator()

KB = calculator.parse("(A|C)=>(B|D)")
KB = calculator.tell(KB, "(A|C)<=>(B|D)")
KB = calculator.tell(KB, "(A=>C)<=>(B=>D)")
KB = calculator.tell(KB, "(B | C) & (A | D)")
KB = calculator.tell(KB, "(A & D) -> B")
Tree = calculator.expression_to_tree(KB)
Tree.draw()




#class Knowlege_Base:
#    atomic_attributes = list()
#    parser = LogicParser()
#
#    def init_tell(self,expression):
#        assert isinstance(expression,str)
#        self.atomic_attributes = self.parser.parse(expression)
#
#    def tell(self, expression):
#        self.atomic_attributes = AndExpression(self.atomic_attributes, self.parser.parse(expression))
#
#
#KB = Knowlege_Base()
#KB.init_tell("(A|C)=>(B|D)")
#KB.tell("(A|C)<=>(B|D)")
#KB.tell("(A=>C)<=>(B=>D)")

