
def is_primo(value):
    if value <= 1:
        return False
    for i in range(2 ,int(value**0.5) + 1):
        if value % i == 0:
            return False
    return True 

