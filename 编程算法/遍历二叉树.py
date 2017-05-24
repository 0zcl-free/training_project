
class TreeNode(object):  # 创建树的结点
    def __init__(self, node_data=None, left=None, right=None):
        self.node_data = node_data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self, root=None):  # 初始化根结点
        self.root = root

    def PreOrder(self, tree_node):  # 先序遍历
        if tree_node is None:
            return
        print(tree_node.node_data)
        self.PreOrder(tree_node.left)
        self.PreOrder(tree_node.right)

    def InOrder(self, tree_node):  # 中序遍历
        if tree_node is None:
            return
        self.InOrder(tree_node.left)
        print(tree_node.node_data)
        self.InOrder(tree_node.right)

    def PostOrder(self, tree_node):  # 后序遍历
        if tree_node is None:
            return
        self.PostOrder(tree_node.left)
        self.PostOrder(tree_node.right)
        print(tree_node.node_data)

    def BitTreeDepth(self, tree_node):  # tree_node为结点
        if tree_node is None:  # 空二叉树深度为０
            return 0
        else:
            depth_left = self.BitTreeDepth(tree_node.left)  # 求左子树深度
            depth_right = self.BitTreeDepth(tree_node.right)  # 求右子树深度
            # 左右子树深度较大值+1
            return 1 + (depth_left if depth_left>depth_right else depth_right)

    def CountLeaf(self, tree_node, count):
        if tree_node is None:
            return count

        if not tree_node.left and not tree_node.right:  # 没有左右结点，即为叶子结点
            count += 1

        count = self.CountLeaf(tree_node.left, count)  # 对左子树进行递归计数
        count = self.CountLeaf(tree_node.right, count)
        return count  # 叶子数


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

    print("\033[31;1m二叉树已创建完成\033[0m".center(50, "-"))

    while True:
        print("""\033[31;1m
            1.遍历二叉树
            2.求二叉树的深度
            3.求二叉树叶子结点数
            exit.退出\033[0m
        """)
        choice = input("\033[31;1m please choose:\033[0m")
        if choice == "1":
            print("开始遍历二叉树".center(50, "-"))
            # 前序遍历
            print("PreOrder".center(50, "-"))
            bt.PreOrder(root_node)
            # 中序遍历
            print("InOrder".center(50, "-"))
            bt.InOrder(root_node)
            # 后序遍历
            print("PostOrder".center(50, "-"))
            bt.PostOrder(root_node)
        elif choice == "2":
            # 求二叉树的深度
            depth = bt.BitTreeDepth(root_node)
            print("\033[31;1m depth:\033[0m", depth)
        elif choice == "3":
            # 求二叉树叶子结点数
            leaf_count = bt.CountLeaf(root_node, count=0)  # 叶子数为０，当作参数传入
            print("\033[31;1m leaf_count\033[0m", leaf_count)
        elif choice == "exit":
            exit()
        else:
            print("\033[31;1mPlease input value num\033[0m")
            continue
