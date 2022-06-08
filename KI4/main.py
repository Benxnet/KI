import Logic_calculator

# operatorreihenfolge:
# 1. -
# 2. &
# 3. |
# 4. ->
# 5. <->
#STring to expression
calculator = Logic_calculator.LogicCalculator()

KB = calculator.parse("(A | B | C) & (A | B | -C) & (-A | B | C) & (-A | -B | C)")
Tree = calculator.expression_to_tree(KB)
Tree.draw()
#15

#KB = calculator.parse("(A|C)=>(B|D)")
#KB = calculator.tell(KB, "(A|C)<=>(B|D)")
#KB = calculator.tell(KB, "(A=>C)<=>(B=>D)")
#KB = calculator.tell(KB, "(B | C) & (A | D)")
#KB = calculator.tell(KB, "(A & D) -> B")
#Tree = calculator.expression_to_tree(KB)
#Tree.draw()




