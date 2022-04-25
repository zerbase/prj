tree_num, need_tree = map(int, input().split())
tree_list = list(map(int, input().split()))

max_tree = max(tree_list)
min_tree = 0

while min_tree <= max_tree:
    mid = (min_tree + max_tree) // 2
    sums = 0

    for i in tree_list:
        if i >= mid:
            sums += i - mid
    if sums < need_tree:
        max_tree = mid -1
    else:
        min_tree = mid + 1
print(max_tree)