from .stack import Stack

precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def infix_to_postfix(expression):
    st = Stack()
    output = []

    for token in expression:
        if token.isalnum():  
            output.append(token)
        elif token == '(':
            st.push(token)
        elif token == ')':
            while not st.isEmpty() and st.peek() != '(':
                output.append(st.pop())
            st.pop()  
        else:  
            while (not st.isEmpty() and st.peek() != '(' and
                   precedence.get(st.peek(), 0) >= precedence.get(token, 0)):
                output.append(st.pop())
            st.push(token)

    while not st.isEmpty():
        output.append(st.pop())

    return ''.join(output)

#Implementation
 
expr = "A+B*(C-D)"
print("Infix:", expr)
print("Postfix:", infix_to_postfix(expr))  # ABCD-*+