
from .swap_node import Node, swap_node
from .in_order import inOrder

N = int(input())

nodes = []

for i in range(N):    
    nodes.append(Node(i+1))
    
for a_node in nodes:
    
    lr = input().strip().split()
    l, r = int(lr[0]), int(lr[1])

    if l != -1:
        a_node.left = nodes[l-1]
    if r != -1:
        a_node.right = nodes[r-1]

K = int(input())

for _ in range(K):

    height = int(input())
    swap_node(nodes[0],height,0)
    inOrder(nodes[0])

