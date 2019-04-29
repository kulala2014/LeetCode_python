import re
def sort_string(data):
    result = ''
    if len(data) > 0:
        digit_list = {}
        digit_list = dict((re.sub("\D", "", i), i) for i in data.split()) 
        result = dict(sorted(digit_list.items(),key=lambda item:item[0]))
        result = ' '.join(result.values())
    return result





