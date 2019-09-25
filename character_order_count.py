#input=‘aaabbbccc’ output=[(‘a’,3),(‘b’,3),(‘c’,3)]

from collections import Counter

#solution 1
def ordered_count(data):
    result = []
    temp_data = list(set(data))
    temp_data = sort()
    result = [(i, data.count(i)) for i in temp_data]
    return result

#solution 2
def ordered_count_s2(data):
    char_count = Counter(data)
    return char_count

def main():
    testing_data = ‘aaaabcdeddddghhhsmmljler’
    result = order_count(testing_data)
    result_s2 = ordered_count_s2(testing_data)
    print(result)
    print(result_s2)

if __name__ == ‘__main__’:
   main()