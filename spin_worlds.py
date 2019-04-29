def spin_words(input_str):
    result = ''

    temp_data = [i if len(i)<5 else i[::-1] for i in input_str.split()]

    result = ' '.join(temp_data)
    return result