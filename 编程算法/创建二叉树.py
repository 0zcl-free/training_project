
class TreeNode(object):  # 创建树的结点
    def __init__(self, node_data=None, left=None, right=None):
        self.node_data = node_data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self, root=None):  # 初始化根结点
        self.root = root

    def preorder(self, tree_node):
        if tree_node is None:
            return
        print(tree_node.node_data)
        self.preorder(tree_node.left)
        self.preorder(tree_node.right)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2, n1)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5, n3, n4)
    n6 = TreeNode(6, n2, n5)
    n7 = TreeNode(7, n6)
    n8 = TreeNode(8)

    root_node = TreeNode('root', n7, n8)  # 根结点

    bt = BTree(root_node)  # 将根结点(包含左右结点)当作参数传给BTree类

    # 前序遍历
    bt.preorder(root_node)