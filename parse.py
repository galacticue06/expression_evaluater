alph = ['_','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maths = ['^', '/', '*', '-', '+', '%', '<', '>', '=', '(', ')', '.', 'j']
def solve(string):                
    if "(" in string:
        pos = prim_br(string)
        to_rep = []
        rep = []
        for i in pos:
            ops = get_op(string,i)
            to_rep.append(ops)
            rep.append(str(solve(ops[1:len(ops)-1])))
        for i in range(len(to_rep)):
            string = string.replace(to_rep[i],rep[i])
    return eval(string)

def analyze(string):
    if string.count("(") != string.count(")"):
        return "Mismatched Brackets"
    br = 0
    ls = len(string)
    for j in range(ls):
        i = string[j]
        if not (i in alph or i in maths or i.isnumeric()):
            return "Illegal Use of Characters : "+i
        if j > 0:
            pre = string[j-1]
        if j < ls-1:
            pos = string[j+1]
        if br < 0:
            return "Mismatched Brackets"
        if i == "(":
            br += 1
            if j > 0:
                if pre.isnumeric():
                    return "Incorrect Syntax"
        elif i == ")":
            br -= 1
            if j < ls-1:
                if pos.isnumeric():
                    return "Incorrect Syntax"
    if br != 0:
        return "Mismatched Brackets"

def prim_br(string):
    inds = []
    br = 0
    rev = 0
    for i in range(len(string)):
        rev = 0
        if string[i] == "(":
            br += 1
            if br == 1 and rev == 0:
                rev = 1
        elif string[i] == ")":
            br -= 1
            rev = 0
        if br == 1 and rev == 1:
            inds.append(i)
    return inds

def find(string):
    con = []
    fun = []
    seq = ""
    tog = 0
    for i in range(len(string)):
        c = string[i]
        if c in alph or c.lower() in alph:
            tog = 1
            seq += c
        else:
            if tog:
                acs = 1
                try:
                    if c == "(":
                        acs = 0
                except:
                    pass
                if acs:
                    if not seq in con:
                        con.append(seq)
                else:
                    if not seq in fun:
                        fun.append(seq)
                seq = ""
                tog = 0
    if seq!="":
        if not seq in con:
            con.append(seq)
    if "j" in con:
        con.remove("j")
    return con,fun
           
def depth(string,dp):
    l = [string]
    while True:
        if dp < 1:
            break
        n_l = []
        for i in l:
            n = prim_br(i)
            for j in n:
                prt = get_op(i,j)
                n_l.append(prt[1:len(prt)-1])
            l = n_l[:]
        dp -= 1
    return l
    
def solve_func(string,fname,func):
    ph = fname[:]
    fname.sort(key=len)
    fns = []
    for i in fname:
        fns.append(func[ph.index(i)])
    fname = fname[::-1]
    func = fns[::-1]
    for i in range(len(fname)):
        finder = fname[i]
        call = func[i]
        scrape = string.find(finder)
        try:
            seq = string[scrape:scrape+len(finder)]+get_op(string,scrape+len(finder))
        except:
            seq = ""
        if seq[len(finder)] != "(":
            scrape = -1
        if scrape > -1:
            f = get_op(string,scrape+len(finder))
            splt = f[1:len(f)-1].split(",")
            arg = []
            for j in splt:
                arg.append(float(solve(j)))
            res = call(*arg)
            if "e" in str(res):
                res = "{:.12f}".format(res)
            else:
                res = str(res)
            string = string.replace(seq,res)
        else:
            pass
                
        if finder+"(" in string:
            cont = 1
            while cont:
                scrape = string.find(finder)
                try:
                    seq = string[scrape:scrape+len(finder)]+get_op(string,scrape+len(finder))
                except:
                    seq = ""
                if seq[len(finder)] != "(":
                    scrape = -1
                if scrape > -1:
                    if "," in seq:
                        f = get_op(string,scrape+len(finder))
                        splt = f[1:len(f)-1].split(",")
                        arg = []
                        for j in splt:
                            arg.append(float(solve(j)))
                        res = call(arg)
                    else:
                        norm = solve(get_op(string,scrape+len(finder)))
                        res = call(float(norm))
                    if "e" in str(res):
                        res = "{:.12f}".format(res)
                    else:
                        res = str(res)
                    string = string.replace(seq,res)
                else:
                    pass
                if not (finder+"(" in string):
                    cont = 0
    return string
    
def load_const(string,cnames,vals):
    ph = cnames[:]
    cnames.sort(key=len)
    valn = []
    for i in cnames:
        valn.append(vals[ph.index(i)])
    cnames = cnames[::-1]
    vals = valn[::-1]
    cont = 1
    for i in range(len(cnames)):
        while cont:
            acs = 1
            try:
                if string[string.find(cnames[i])+len(cnames[i])] == "(":
                    acs = 0
                if string.find(cnames[i]) < 0:
                    break
            except:
                pass
            if acs:
                string = string.replace(cnames[i],str(vals[i]))
    return string
        

def get_op(string,index):
    try:
        if string[index] != "(":
            return False
    except:
        return False
    br = 0
    string = string[index:len(string)]
    for i in range(len(string)):
        if string[i] == "(":
            br += 1
        if string[i] == ")":
            br -= 1
        if br == 0:
            break
    return string[0:i+1]

def exp_evaluate(seq,func_nms={},const_nms={}):
    func_names = []
    funcs = []
    const_names = []
    vals = []
    for i in func_nms:
        if i in seq:
            func_names.append(i)
            funcs.append(func_nms[i])
    for i in const_nms:
        if i in seq:
            const_names.append(i)
            vals.append(const_nms[i])
    con, fun = find(seq)
    for i in con:
        if not i in const_names:
            return "Variable not defined : "+i
    for i in fun:
        if not i in func_names:
            return "Function not defined : "+i
    an = analyze(seq)
    if an != None:
        return an
    return evaluate(seq, func_names, funcs, const_names, vals)

def evaluate(seq, func_names = [], funcs = [], const_names = [], vals = []):
    for i in range(seq.count("^")):
        seq = seq.replace("^","**")
    con,fun = find(seq)
    replacement = load_const(seq, const_names, vals)
    replacement = solve_func(replacement,func_names,funcs)
    return eval(replacement)
    
