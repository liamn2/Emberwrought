def capital_chars(string):  #Define function with string input
  return [for i in i, for char in enumerate(string), return char.index() if char.isupper()]
  
return capital_chars("HeLlO")

# Binary Tree Preorder Traversal
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def dfs(root):
    ans.append(root.val)
    dfs(root.left)
    dfs(root.right)

    ans = []
    dfs(root)
    return ans
