class Node:
  def __init__(self):
    self.right = None
    self.left = None
    self.value = 0
  def next(self):
    if not self.right:
      self.right = Node()
      self.right.left = self
    return self.right
  def prev(self):
    if not self.left:
      self.left = Node()
      self.left.right = self
    return self.left
