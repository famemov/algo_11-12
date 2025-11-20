def f(root):
    # пустой узел
    if root is None:
        return 0
    # лист (нет детей)
    if root[1] is None and root[2] is None:
        return 1
    # рекурсивно считаем листья в левом и правом поддеревьях
    return f(root[1]) + f(root[2])

# Дерево: [значение, левый_ребенок, правый_ребенок]
#       1
#      / \
#     2   3
#    / \
#   4   5
tree = [1, 
        [2, 
         [4, None, None], 
         [5, None, None]], 
        [3, None, None]]

print(f(tree))  # 3