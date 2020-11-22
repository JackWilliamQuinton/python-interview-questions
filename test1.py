def get_middle(str):
    if len(str) % 2 != 0:
        return str[int(len(str)/2)]
    else:
        return str[int(len(str)/2)-1:int(len(str)/2)+1]


