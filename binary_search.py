array = [5, 7, 15, 18, 22, 35, 40, 48, 50, 54,
         60, 62, 68, 70, 77, 80, 85, 88, 90, 96]
key = int(input("探す値を入力してください: "))
imin = 0
imax = len(array) - 1


def binary_search(ary, key, imin, imax):
    KEY_NOT_FOUND = -1

    if imax < imin:
        return KEY_NOT_FOUND
    else:
        imid = imin + (imax - imin) // 2
        if ary[imid] > key:
            return binary_search(ary, key, imin, imid - 1)
        elif ary[imid] < key:
            return binary_search(ary, key, imid + 1, imax)
        else:
            return imid


index = binary_search(array, key, imin, imax)

if index == -1:
    print("探す値は見つかりませんでした。")
else:
    print(f"探す値 {key} は、インデックス {index} にあります。")
