from .stack import Stack

def evaluate_postfix(expression):
    s = Stack()
    # Split by space if expression is like "5 3 +" 
    # or iterate directly if it's "53+"
    for char in expression.split():
        if char.isdigit():
            s.push(int(char))
        else:
            val2 = s.pop()
            val1 = s.pop()
            
            if char == '+': s.push(val1 + val2)
            elif char == '-': s.push(val1 - val2)
            elif char == '*': s.push(val1 * val2)
            elif char == '/': s.push(val1 / val2)
            
    return s.pop()

if __name__ == "__main__":
    # Example: "10 2 + 3 *" -> (10 + 2) * 3 = 36
    expr = "10 2 + 3 *"
    print(f"{expr}: {evaluate_postfix(expr)}")