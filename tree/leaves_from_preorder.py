def leaves(pre,ln):
    if ln==0:
        return
    leaves = []
    successor = {}
    prev = None
    for i in pre:
        if not prev:
            successor[i]=None
            prev=i
        elif prev<i:
            if successor.get(prev):
                if successor[prev]<i:
                    leaves.append(prev)
                    curr = successor[prev]
                    while curr:
                        if curr>i:
                            successor[i]=curr
                            break
                        curr = successor.get(curr)
                else:
                    successor[i]=successor.get(prev)
        else:
            successor[i]=prev
        prev=i
    leaves.append(i)
    for leaf in leaves:
        print(leaf)

arr = [61, 8, 48, 767, 675, 465, 323, 95, 91, 212, 156, 201, 210, 240, 265, 261, 270, 401, 393, 388, 425, 558, 556, 502, 478, 598, 563, 587, 646, 621, 754, 689, 686, 696, 713, 702, 757, 993, 967, 870, 837, 829, 925, 920,999]
leaves(arr,len(arr))