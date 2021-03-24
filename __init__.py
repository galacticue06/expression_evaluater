from math_parser import parse

class evaluate_math:
    def __init__(self, expression, functions={}, constants={}):
        self.result = parse.exp_evaluate(expression,functions,constants)
        
class evaluate_expr:
    def __init__(self, expression, functions={}, constants={}):
        self.result = parse.eq_evaluate(expression,functions,constants)
        
class evaluate_depth:
    def __init__(self, expression, dpt):
        self.result = parse.depth(expression, dpt)
