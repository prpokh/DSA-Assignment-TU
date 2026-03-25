def fibonacci_dp(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # We only need to keep track of the last two numbers
    prev_2 = 0  # F(n-2)
    prev_1 = 1  # F(n-1)
    current = 0
    
    for i in range(2, n + 1):
        current = prev_1 + prev_2
        # Update our markers for the next iteration
        prev_2 = prev_1
        prev_1 = current
        
    return current

# Example Usage:
n_terms = 10
print(f"The {n_terms}th Fibonacci number is: {fibonacci_dp(n_terms)}")