
import sys

from .swap_node import Node, swap_node
from tree_inorder_traversal.run import inOrder

sys.setrecursionlimit(1500)

N = int(input())

nodes = []

for i in range(N+1):
    nodes.append(Node(i+1))

for node in nodes[:-1]:
    l, r = map(int,input().split())
    if l > 0:
        node.left = nodes[l-1]
    if r > 0:
        node.right = nodes[r-1]

K = int(input())

for _ in range(K):
    height_swap = int(input())
    swap_node(nodes[0], height_swap, 0)
    inOrder(nodes[0])

