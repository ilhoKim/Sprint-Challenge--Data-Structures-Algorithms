class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # traverse pre-order and run cb 'for each' node
    cb(self.value)

    # Terminate recursion condition
    if self.left is None and self.right is None:
      return
    
    # Go left first
    if self.left is not None:
      self.left.depth_first_for_each(cb(self.value))

    # Go right then
    elif self.right is not None:
      self.right.depth_first_for_each(cb(self.value))


  def breadth_first_for_each(self, cb):
    # initialize a queue
    queue = []
    # fill the root node
    queue.append(self)

    # iterate
    while len(queue) :
      # pull out 'first in' from the queue
      current = queue.pop(0)
      
      # check if the node has left child. If so, put it in the tree
      if current.left is not None:
        queue.append(current.left)

      # check if the node has right child. If so, put it in the tree
      if current.right is not None:
        queue.append(current.right)

      # call the callback on current node value
      cb(current.value)


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
