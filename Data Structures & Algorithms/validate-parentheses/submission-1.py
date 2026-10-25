class Solution:

  def _matches_top(self, stack: list, expected_open: str) -> bool:
    if stack and stack[-1] == expected_open:
        stack.pop()
        return True
    return False

  def isValid(self, s: str) -> bool:
    stack = []

    for c in s:
      if c in "([{":
        stack.append(c)
      elif c == ")" and not self._matches_top(stack, "("):
        return False
      elif c == "}" and not self._matches_top(stack, "{"):
        return False
      elif c == "]" and not self._matches_top(stack, "["):
        return False

    return len(stack) == 0