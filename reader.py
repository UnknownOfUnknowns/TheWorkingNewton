import re


class Reader():
    def __init__(self, ch):
        self.pattern = '(([\+\-]?[\d\.\d]]*)' + ch + '\*{0,2}(\d*))'
        self.terms = []

    def read(self, inp):
        self.terms = re.findall(self.pattern, inp)


    def poly_derivative(self):
        res = ''
        for i in range(0, len(self.terms)):
            inputToFn = self.terms[i]
            if int(inputToFn[1]) > 0:
                res += '+'
            res += self.poly_term_derivative(inputToFn)
        return res

    def poly_term_derivative(self, f):
        if f[2] != '':
            exp = int(f[2])
        else:
            exp = 1
        return str(float(f[1]) * int(exp)) + 'x**' + str(exp - 1)
