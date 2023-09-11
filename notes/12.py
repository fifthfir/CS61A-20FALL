odds = [3, 5, 7, 9, 11]
list(range(1, 3))
[odds[i] for i in range(1, 3)]
odds[1:3]
odds[:3] # == odds[0:3]
odds[1:]
odds[:]
sum([2, 3, 4], 5) # == 14
[2, 3] + [4] # = [2, 3, 4]
sum([[2, 3], [4]], []) # = [2, 3, 4]
sum([[[1]], [2]], []) # = [[1], 2]
sum([[1]], []) # = [1]
sum([[1], [2, 3], [4]], []) # = [1, 2, 3, 4]

def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        branch_count = [count_leaves(b) for b in branches(t)]
        return sum(branch_count)

def leaves(tree):
    '''Return a list containing the leaf labels of tree.
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    '''
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
    '''Return a tree like t but with leaf labels incremented.'''
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    '''Return a tree like t but with all labels incremented.'''
    return tree(label(t) + 1, [increment(b) for b in branches(t)])
    
def print_tree(t, indent = 0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def fact(n):
    return fact_times(n, 1)

def fact_times(n, k):
    '''Return k * n * ... * 1'''
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)

numbers = tree(3, [tree(4), tree(5, [tree(6)])])
haste = tree('h', [tree('a', [tree('s'), 
                              tree('t')]),
                  tree('e')])

def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)
    
print_sums(numbers, 0) # 7 14
print_sums(haste, '') # has hat he