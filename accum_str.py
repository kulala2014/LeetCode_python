#input=‘abcde’ output=‘A-Bb-Ccc-Dddd-Eeeee’

def accum(data):
    temp_data = [(i*(data.index(i) +    1)).title() for i in data]
    result = ‘-‘.join(temp_data)
    return result

def main():
    testing_data = ‘abcd’
    result = accum(testing_data)
    print(result)

if __name__ == ‘__main__’:
    main()
