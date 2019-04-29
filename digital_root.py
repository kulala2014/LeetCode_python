def digital_root(data):
    result=0
    if data == 0:
        result =0
    else:
        result = digital_root(data//10) + data%10
    return result