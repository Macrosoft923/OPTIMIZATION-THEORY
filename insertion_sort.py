import random


def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        if data[i - 1] > data[i]:
            j = i
            tmp = data[i]
            while j > 0 and data[j - 1] > tmp:
                data[j] = data[j - 1]
                j -= 1
            data[j] = tmp
    return data


random_list = [random.randint(1, 100) for _ in range(10)]
print("ソート前: ", random_list)

sorted_list = insertion_sort(random_list)
print("ソート後: ", sorted_list)
