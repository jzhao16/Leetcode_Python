import string

alpha_list = list(string.ascii_uppercase)
digit_list = list(range(1,27))
a2d_dict = dict(zip(digit_list, alpha_list))

def d2a(digit):
    code = []
    while digit > 0:
        num = digit%26 
        if num == 0:
            code.append('Z')
            digit = (digit -26)//26
        else: 
            code.append(a2d_dict[num]) 
            digit = digit // 26
        
    return ''.join(code[::-1])