from .stack import Stack

def is_balanced(expression):
    st = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            st.push(char)
        elif char in ")}]":
            if st.isEmpty() or st.pop() != pairs[char]:
                return False
    return st.isEmpty()

expr1 = "({[]})"
expr2 = "([)]"
print(expr1, "->", is_balanced(expr1))
print(expr2, "->", is_balanced(expr2))