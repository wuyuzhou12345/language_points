def find_the_longgest_common_str(arr):
    min_str = min(arr)
    max_str = max(arr)
    for i,v in enumerate(min_str):
        if max_str[i] != v:
            return min_str[:i]
    return min_str

if __name__ == '__main__':
    print(find_the_longgest_common_str(['1r1','carhello','car1']))
