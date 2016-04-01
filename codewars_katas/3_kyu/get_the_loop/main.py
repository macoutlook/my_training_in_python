class Node(object):
    pass


# def loop_size(node):
#     # counter = 0
#     # nodes = []
#     # while not node in nodes:
#     #     nodes.append(node)
#     #     node = node.next
#     # counter = len(nodes[nodes.index(nodes[-1].next):-1]) + 1
#     #
#     # return counter
#     nodes = []
#     tortoise = node
#     hare = node.next
#     lam = 1
#
#     # while True:
#     #     nodes.append(tortoise)
#     #     if not hare.next:
#     #         return 0
#     #     hare = hare.next
#     #     if not hare.next:
#     #         return 0
#     #     hare = hare.next
#     #     tortoise = tortoise.next
#     #     if hare == tortoise:
#     #         nodes.append(tortoise)
#     #         return nodes[nodes.index(nodes[-1].next)]
#     # return len(nodes[nodes.index(nodes[-1].next):-1]) + 1
#     #     print nodes[-1].next

def loop_size_from_codewars(node):
    index = {}
    i = 0
    while True:
        if node in index:
            return i - index[node]
        index[node] = i
        node = node.next
        i += 1

def loop_size(node):
    tortoise = node.next
    hare = tortoise.next
    counter = 1
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next
    hare = tortoise.next
    while tortoise != hare:
        hare = hare.next
        counter += 1

    return counter




def main():
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print loop_size(node1)
    # assert(loop_size(node1)) == 4
    nodes = [Node() for _ in xrange(50)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[49].next = nodes[21]
    print floyd(nodes[0])


if __name__ == '__main__':
    main()