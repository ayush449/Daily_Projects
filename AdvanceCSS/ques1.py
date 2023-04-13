def fun(string):
    if len(string) < 2:
        return ''
    else:
        return string[:2] + string[-2:]

inputstring=input ()
print(fun(inputstring))
