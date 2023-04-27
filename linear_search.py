array = [5, 7, 15, 18, 22, 35, 40, 48, 50, 54,
         60, 62, 68, 70, 77, 80, 85, 88, 90, 96]
ary_size = len(array)
key = int(input("探す値を入力してください: "))


def linear_search(ary, ary_size, key):
    for i in range(ary_size):
        if ary[i] == key:
            return i
    return -1


index = linear_search(array, ary_size, key)

if index == -1:
    print("探す値は見つかりませんでした。")
else:
    print(f"探す値 {key} は、インデックス {index} にあります。")
