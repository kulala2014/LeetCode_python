# def get_character(data):
#     data_temp = list(set(data))
#     data_temp.sort()
#     result = [(i,data.count(i)) for i in data_temp]
#     return result

# def main():
#     str_data = 'abcacadabra'
#     print(get_character(str_data))

# if __name__ == '__main__':
#     main()



# def character_to_upper(data):
#     data_temp = data.title()
#     title = [i[0] for i in data_temp.split(' ')]
#     result = '.'.join(title)
#     return result


# def main():
#     str_data = 'Sam Harris'
#     print(character_to_upper(str_data))

# if __name__ == '__main__':
#     main()

def sum_plus(data):
    result = 0
    b = [i for i in data if i >0]
    if len(b) > 0:
        result = sum(b)
    return result

testing_data = [1,2,34,-2,-9,12,3]
print(sum_plus(testing_data))


def format_str(data):
    temp = [(i*(data.index(i)+1)).title() for i in data]
    result = '-'.join(temp)
    return result
testing_str = 'abcdfg'
print(format_str(testing_str))
