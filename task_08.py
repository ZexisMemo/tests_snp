def multiply_numbers(inputs = False):
    digitflag = False
    if inputs:
        mult = 1
        inputs = str(inputs)
        for i in range(0, len(inputs)):
            if ord(inputs[i]) in range(48,57):
                mult = mult * (ord(inputs[i]) - 48)
                digitflag = True
    if digitflag:
        print(mult)
    else:
        print(None)


multiply_numbers()
multiply_numbers('ss')
multiply_numbers('1234')
multiply_numbers('sssdd34')
multiply_numbers(2.3)
multiply_numbers([5, 6, 4])
