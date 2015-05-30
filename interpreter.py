from instructions import instruction_types, instruction_regex, RBracket, LBracket
from node import Node
import re, sys

class TerminatedException(Exception):
  pass
class ParseException(Exception):
  pass

class BrainfuckInterpreter:
  def __init__(self, code):
    """
    Takes a string that represents the code, and initializes the interpreter
    """
    self.code = code
    self.current_instruction = None
    self.first_instruction = None
    self.current_cell = Node()
    self.parse(code)
  def parse(self, code):
    """
    Takes a string that represents the code, and parses it into a tree of instructions
    """
    stripped_code = re.sub(instruction_regex,"", code)
    parse_current = None
    for char in stripped_code:
      prev = parse_current
      for t in instruction_types:
        if char == t.symbol:
          parse_current = t(prev)
      if isinstance(parse_current, RBracket):
        traceback = parse_current
        while True:
          if traceback == None:
            raise ParseException("No corresponding left bracket")
          if isinstance(traceback, LBracket) and traceback.partner == None:
            parse_current.partner = traceback
            traceback.partner = parse_current
            break
          traceback = traceback.prev
      if prev == None:
        self.first_instruction = parse_current
    self.current_instruction = self.first_instruction
  def step(self):
    """
    Executes a single step of the program, throws an exception if the program is finished
    """
    if not self.current_instruction:
      raise TerminatedException()
    self.current_instruction, self.current_cell = self.current_instruction.execute(self.current_cell)
  def run(self):
    """
    Steps continuously through the program until it reaches the end
    """
    try:
      while True:
        self.step()
    except TerminatedException:
      pass

if __name__ == "__main__":
  code = None
  if len(sys.argv) > 1:
    f = open(sys.argv[1])
    code = f.read()
  else:
    code = raw_input("Enter some Brainfuck code: ")
  interpreter = BrainfuckInterpreter(code)
  interpreter.run()
