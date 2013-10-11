import joeSettings as s

def Return(x):return x

def Make(r, func, name, funcParse = [""], wrapFuncFunc = Return):
    if len(funcParse) and funcParse != [""]:
        return str(r.header(name))+wrapFuncFunc(str(func(funcParse)))+str(r.footer())
    return str(r.header(name))+wrapFuncFunc(str(func()))+str(r.footer())
    

def GetWebpage(web, r):
    i = web.input(p="")
    if i['p'] == "ab":
        return Make(r, r.about, "About")
    elif i['p'] == "bl":
        i = web.input(b="")
        if i['b'] != "":
            b = r.Blogs._lookup(i['b'])[1]
            if b != None:
                return Make(r, r.Blogs._template(i['b']), "Blog", wrapFuncFunc = Format)
        return Make(r, r.blog, "Blog", s.BlogsList)
    elif i['p'] == "pr":
        return Make(r, r.projects, "Projects", s.ProjectsList)
    elif i['p'] == "py":
        return Make(r, r.python, "Python", s.PythonList)
    return Make(r, r.index, "Peilonrayz")


#Used for the converting Python to text-highlighted Python.
kw = ['abs', 'divmod', 'input', 'open', 'staticmethod', 'all', 'enumerate', 'int', 'ord', 'str', 'any', 'eval', 'isinstance', 'pow', 'sum', 'basestring', 'execfile', 'issubclass', 'print', 'super', 'bin', 'file', 'iter', 'property',
      'tuple', 'bool', 'filter', 'len', 'range', 'type', 'bytearray', 'float', 'list', 'raw_input', 'unichr', 'callable', 'format', 'locals', 'reduce', 'unicode', 'chr', 'frozenset', 'long', 'reload', 'vars', 'classmethod', 'getattr',
      'map', 'repr', 'xrange', 'cmp', 'globals', 'max', 'reversed', 'zip', 'compile', 'hasattr', 'memoryview', 'round', '__import__', 'complex', 'hash', 'min', 'set', 'apply', 'delattr', 'help', 'next', 'setattr', 'buffer', 'dict',
      'hex', 'object', 'slice', 'coerce', 'dir', 'id', 'oct', 'sorted', 'intern', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import',
      'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

def Format(string):
    string2 = ""
    i = 0
    j = 0
    stringing = False
    stringing2 = False
    py = False
    func = False
    tempWord = ""
    for i in xrange(len(string)):
        if string[i] == "<":
            if string[i:i+8] == "<Python>":
                py = True
                j = i+8
            elif string[i:i+9] == "</Python>":
                py = False
                j = i+9
        if py and i >= j:
            if string[i] in " \t\n()./\\*!@#$%^&*-_=+[]{};:'\",<>.?":
                if tempWord in kw:
                    string2 += "<keyword>"+tempWord+"</keyword>"
                    if tempWord in ["class", "def"]:
                        func = True
                elif func:
                    string2 += "<func>"+tempWord+"</func>"
                    func = False
                else:
                    string2 += tempWord
                tempWord = ""
            if string[i] == " ":
                string2 += '&nbsp;'
            elif string[i] == "\"":
                if stringing:
                    string2 += string[i]+"</string>"
                    stringing = False
                else:
                    string2 += "<string>"+string[i]
                    stringing = True
            elif string[i] == "'":
                if stringing2:
                    string2 += string[i]+"</string>"
                    stringing2 = False
                else:
                    string2 += "<string>"+string[i]
                    stringing2 = True
            elif not string[i] in " \t\n()./\\*!@#$%^&*-_=+[]{};:'\",<>.?":
                tempWord += string[i]
            else:
                string2 += string[i]
        else:
            string2 += string[i]
    string = string2
    del string2
    string2 = ""
    for i in xrange(len(string)):
        if string[i] == "\n":
            string2 += "\n</br>"
        elif string[i] == "\t":
            string2 += '&nbsp;&nbsp;&nbsp;&nbsp;'
        else:
            string2 += string[i]
    return string2
