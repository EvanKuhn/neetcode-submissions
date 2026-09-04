class Node:
    def __init__(self, char: str = None):
        self.char: str = char
        self.leaf: bool = False
        self.children: List[Node] = [None] * 26

    def __str__(self):
        return f"Node(char={self.char}, leaf={self.leaf})"


class PrefixTree:
    def __init__(self):
        self.root: Node = Node()

    def get_child(self, node: Node, char: str, create: bool = False) -> Optional[Node]:
        i = ord(char) - ord('a')
        if node.children[i] is None and create:
            node.children[i] = Node()
        return node.children[i]

    def insert(self, word: str) -> None:
        curnode = self.root

        for i, c in enumerate(word):
            # Get node for current char
            curnode = self.get_child(curnode, c, create=True)
            assert curnode.char is None or curnode.char == c

            # Set character and leaf
            curnode.char = c
            if i == len(word)-1:
                curnode.leaf = True

    def search(self, word: str) -> bool:
        return self._search(word)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix, prefix_ok=True)

    def _search(self, word: str, prefix_ok=False) -> bool:
        curnode = self.root
        for i, c in enumerate(word):
            curnode = self.get_child(curnode, c)
            if curnode is None:
                return False
            if curnode.char != c:
                return False
            if i == len(word)-1:
                return curnode.leaf or prefix_ok
            
        return False
