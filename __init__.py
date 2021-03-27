from expression_evaluater import parse

class evaluate_math:
    '''Evaluates the given mathematical expression.\nTakes 2 positional arguments as dictionaries for functions and constants.'''
    def __init__(self, expression, functions={}, constants={}):
        self.result = parse.exp_evaluate(expression,functions,constants)
        
class evaluate_expr:
    '''Evaluates the given logical expression.\nTakes 2 positional arguments as dictionaries for functions and constants.'''
    def __init__(self, expression, functions={}, constants={}):
        self.result = parse.eq_evaluate(expression,functions,constants)
        
class evaluate_depth:
    '''Analyzes the given sequence and returns bracket's content in the matching depth.'''
    def __init__(self, expression, dpt):
        self.result = parse.depth(expression, dpt)

class parse_expr:
    '''Parse the given expression\n\nSelf.constants -> Returns constant names\nSelf.functions -> Returns function names'''
    def __init__(self, expression):
        result = parse.find(expression)
        try:
            if self.content == "":
                pass
        except:
            self.content = None
        self.expression = expression
        self.constants = result[0]
        self.functions = result[1]
    def get_raw_content(self, f_name):
        '''Finds raw content of the given function name.'''
        s = self.expression.find(f_name)
        if s > -1:
            s += len(f_name)
            fn = parse.get_op(self.expression,s)
            self.content = fn[1:len(fn)-1]
        else:
            self.content = None
    def get_evaluated_content(self, f_name, fun={}, con={}):
        '''Finds evaluated content of the given function name.'''
        s = self.expression.find(f_name)
        ret = []
        if s > -1:
            s += len(f_name)
            fn = parse.get_op(self.expression,s)
            fn = fn[1:len(fn)-1].split(',')
            for i in fn:
                ret.append(parse.exp_evaluate(i,fun,con)) 
            self.content = ret
        else:
            self.content = None
    def get_arguments(self, f_name):
        '''Finds arguments of the given function name.'''
        s = self.expression.find(f_name)
        if s > -1:
            s += len(f_name)
            fn =  parse.get_op(self.expression,s)
            self.content = fn[1:len(fn)-1].split(',')
        else:
            self.content = None
