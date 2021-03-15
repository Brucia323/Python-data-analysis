str = input('password:')
str = list(str)
flag = ['weak', 'below middle', 'above middle', 'strong']


def password_strengthmetric(password):
    """判断密码强度

    Args:
        password (list): [description]

    Returns:
        int: [description]
    """
    s = 0
    for i in range(len(password)):
        if(password[i].isnumeric()):
            if(s == 0):
                s = 0
        elif(password[i].islower()):
            if(s < 1):
                s = 1
        elif(password[i].isupper()):
            if(s < 2):
                s = 2
        if password[i] in ('.' or '_'):
            s = 3
    return s


print(flag[password_strengthmetric(str)])
