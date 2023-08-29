list_in = [2, 3, [4, 5, [6, 7], 6], 2, [5, 6]]


def get_depths(lst, depths, current_depth=0):
    out = [
        get_depths(v, depths, current_depth + 1) if isinstance(v, list) else v
        for v in lst
    ]
    print(type(out))
    # depths[current_depth] = out
    depths.setdefault(current_depth, []).append(out)

    return out


depths = {}
list_out = get_depths(list_in, depths)
for lst in depths[max(depths)]:
    lst.append(lst[-1] + 1)

print(list_out)