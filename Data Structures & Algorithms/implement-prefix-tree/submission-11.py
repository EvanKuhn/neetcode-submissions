

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
        #print(f"insert({word})")
        curnode = self.root

        for i, c in enumerate(word):
            # Get node for current char
            curnode = self.get_child(curnode, c, create=True)
            #print(f"- char={c}, curnode={curnode}")
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




# class Node:
#     def __init__(self, value: str = None):
#         self.value: str = value
#         self.leaf: bool = False
#         self.children: List[Node] = [None] * 26
    

#     def add_word(self, word: str) -> None:
#         """
#         Recursively create the nodes to store the characters for the word.
#         """
#         print(f"add_word({word})")
#         assert len(word) > 0
#         assert self.value is None or self.value == word[0]
#         self.value = word[0]
#         if len(word) == 1:
#             self.leaf = True
#         else:
#             child = self.put_child(word[1])
#             child.add_word(word[1:])

#     def put_child(self, char: str) -> Node:
#         """
#         Return the child node for a given character, creating 
#         the node if needed.
#         """
#         print(f"put_child({char})")
#         assert len(char) == 1
#         assert ord('a') <= ord(char) <= ord('z')
#         i = ord(char) - ord('a')
#         if self.children[i] is None:
#             self.children[i] = Node(value=char)
#         return self.children[i]

#     def get_child(self, char: str) -> Optional[Node]:
#         """
#         Return the child node for the given character, or None if not found
#         """
#         assert len(char) == 1
#         assert ord('a') <= ord(char) <= ord('z')
#         i = ord(char) - ord('a')
#         self.children[i]

#     def has_word(self, word: str, prefix_ok: bool = False) -> bool:
#         print(f"has_word(word={word}, prefix_ok={prefix_ok}), self.value={self.value}, self.leaf={self.leaf}")
#         assert len(word) > 0
#         if word[0] != self.value:
#             print("- chars don't match")
#             return False
#         if len(word) == 1:
#             print("- returning if leaf or prefix_ok")
#             return self.leaf or prefix_ok
#         child = self.get_child(word[1])
#         print(f"- looking at child {child.value}")
#         return child is not None and child.has_word(word[1:])
        


# class PrefixTree:

#     def __init__(self):
#         self.root: Node = None
        
#     def insert(self, word: str) -> None:
#         if not self.root:
#             self.root = Node()
#         self.root.add_word(word)

#     def search(self, word: str) -> bool:
#         if not word:
#             return False
#         return self.root.has_word(word)
    
#     def startsWith(self, prefix: str) -> bool:
#         if not prefix:
#             return False
#         return self.root.has_word(prefix, prefix_ok=True)

        
        