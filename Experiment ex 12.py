def is_safe(queens, col, row):
    """Check whether a queen at (col, row) is attacked by earlier queens."""
    for c in range(col):
        r = queens[c]
        if r == row or abs(r - row) == abs(c - col):   # same row or diagonal
            return False
    return True
 
 
def solve(n, col=0, queens=None, solutions=None):
    """Place queens column by column; backtrack when no row is safe."""
    if queens is None:
        queens, solutions = [-1] * n, []
 
    if col == n:                         
        solutions.append(queens[:])
        return solutions
 
    for row in range(n):
        if is_safe(queens, col, row):
            queens[col] = row            
            solve(n, col + 1, queens, solutions)
            queens[col] = -1             
    return solutions
 
 
def print_board(queens):
    n = len(queens)
    for row in range(n):
        print(" ".join("Q" if queens[col] == row else "." for col in range(n)))
    print()
 
 
if __name__ == "__main__":
    n = int(input("Enter the number of queens (N): "))
    solutions = solve(n)
 
    if solutions:
        print(f"\nTotal solutions for N = {n}: {len(solutions)}")
        print("\nFirst solution (rows by column):", [r + 1 for r in solutions[0]], "\n")
        print_board(solutions[0])
    else:
        print(f"No solution exists for N = {n}.")