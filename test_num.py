import random
import itertools
def get_num_count():
    data = [1,2,3,4,5,6,7,8,9]
    result = [random.sample(data, 3) for i in range(len(data))]
    return result

    x = itertools.combinations(range(4), 3)


data = [1,2,3,4,5,6,7,8,9]
x = itertools.combinations(data, 3)
result = [i for i in list(x) if sum(i) == 15]
print(result)