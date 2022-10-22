def calc (a, b, sign):
    print(type(b))
    if((type(a) != int and type(a) != float) or (type(b) != int and type(b) != float)):
        raise ValueError
    if(sign == '+'):
        return a + b
    elif(sign == '-'):
        return a - b
    elif(sign == '*'):
        return a * b
    elif(sign == '/'):
        return a/b
    else:
        raise ValueError