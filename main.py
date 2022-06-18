from sympy import *

x = Symbol("x")

def newton(xn, fun, der, maxIter, curIter, resList):
    fn = sympify(fun)
    dr = sympify(der)
    xn1 = xn-fn.evalf(subs={x: xn})/dr.evalf(subs={x: xn})
    resList.append(xn1)
    if curIter <= maxIter:
        return newton(xn1, fun, der, maxIter, curIter +1, resList)
    return xn1
