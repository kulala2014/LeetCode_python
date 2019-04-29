def getCount(input_str):
    num_vowels = 0
    vowel_str = ['a', 'e', 'i', 'o', 'u']
    num_vowels = len([id for i in input_str if i in vowel_str])
    return num_vowels

input_str = 'abracadabra'
result = getCount(input_str)
print(result)