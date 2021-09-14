def longgest_common_prefix(strs):
    _max = max(strs)
    _min = min(strs)
    for index,content in enumerate(_min):
        if _max[index] != content:
            return _min[:index]
    return _min


if __name__ == '__main__':
    # print(longgest_common_prefix(["flower","flow","flight"]))
    print(longgest_common_prefix(["car","carrace","car"]))