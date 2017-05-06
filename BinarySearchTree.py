import sys
import string


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None


def bst_insert(tree, key):
    root = tree
    x = Node(key)
    parent = None  # parent: tree的目标父节点
    while tree:
        parent = tree
        if key < tree.key:
            tree = tree.left
        else:
            tree = tree.right
    x.parent = parent
    if parent is None:
        return x
    elif key < parent.key:
        parent.left = x
    else:
        parent.right = x
    return root

def bst_in_order_walk(tree, f):
    if tree is not None:
        bst_in_order_walk(tree.left, f)
        f(tree.key)
        bst_in_order_walk(tree.right)

def bst_search(tree, x):
    while tree is not None and tree.key is not x:
        if x < tree.key:
            tree = tree.left
        else:
            tree = tree.right
    return tree
    
