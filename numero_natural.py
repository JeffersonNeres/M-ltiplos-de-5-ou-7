"docstring"
def multiplos(natural):
    "docstring"
    resultado_7 = natural//7
    resultado_5 = natural//5
    if resultado_7*7 == natural and resultado_5*5 == natural:
        print("fizzbuzz")
        return resultado_7*7
    elif resultado_5*5 == natural:
        print("fizz")
        return resultado_5*5
    elif resultado_7*7 == natural:
        print("buzz")
        return resultado_7*7
    else:
        print("miss")
        return resultado_7*7
