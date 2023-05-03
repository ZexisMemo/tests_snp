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
        return mult
    else:
        return None
