
def VerifyInput(input):
    try:
        i = int(length)
    except ValueError:
        return False
    if(int(length) <=0):
        return False
    else:
        return True
