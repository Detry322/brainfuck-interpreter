import sys
import readchar

class Instruction:
  def __init__(self,prev):
    self.prev = prev
    if prev:
      self.prev.next = self
    self.partner = None
    self.next = None
  def execute(self, node):
    return (self.next, node)

class LBracket(Instruction):
  symbol = "["
  def execute(self, node):
    return (self.next, node)

class RBracket(Instruction):
  symbol = "]"
  def execute(self, node):
    return (self.next, node) if node.value == 0 else (self.partner, node)

class Plus(Instruction):
  symbol = "+"
  def execute(self, node):
    node.value += 1
    return (self.next, node)

class Minus(Instruction):
  symbol = "-"
  def execute(self, node):
    node.value -= 1
    return (self.next, node)

class LShift(Instruction):
  symbol = "<"
  def execute(self, node):
    return (self.next, node.prev())

class RShift(Instruction):
  symbol = ">"
  def execute(self, node):
    return (self.next, node.next())

class Dot(Instruction):
  symbol = "."
  def execute(self, node):
    sys.stdout.write(chr(node.value))
    sys.stdout.flush()
    return (self.next, node)

class Comma(Instruction):
  symbol = ","
  def execute(self, node):
    node.value = ord(readchar.readchar())
    return (self.next, node)

instruction_types = [LBracket, RBracket, Plus, Minus, LShift, RShift, Dot, Comma]
instruction_regex = r'[^\+\-\[\]\<\>\.\,]'
