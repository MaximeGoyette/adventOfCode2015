import re

data = open('19.txt').read()

replacements = re.findall(r'(\w+) => (\w+)', data)
molecule = data.split('\n')[-1]

class Node:
    def __init__(self, value, parentNode, deepness):
        self.value = value
        self.parentNode = parentNode
        self.deepness = deepness
        self.children = []
        self.children_found = False

def find_children(current_node):
    children = []
    for a, b in replacements:
        indices = [m.start() for m in re.finditer(b, current_node.value)]
        for i in indices:
            new_molecule = current_node.value[:i] + a + current_node.value[i + len(b):]
            children.append(Node(new_molecule, current_node, current_node.deepness + 1))
    return children

node = Node(molecule, None, 0)

while True:
    if node.value == 'e':
        print node.deepness
        exit(0)
    elif not node.children_found:
        node.children = find_children(node)
        node.children_found = True
    elif len(node.children) == 0:
        node.parentNode.children.remove(node)
        node = node.parentNode
    else:
        node = node.children[0]

