"""
Experiment 11: Map-Coloring as a Constraint Satisfaction Problem (CSP)
solved with Backtracking Search.
 
CSP formulation (Australia map):
  Variables : WA, NT, SA, Q, NSW, V, T
  Domains   : {Red, Green, Blue} for every variable
  Constraints: adjacent regions must have different colors
"""
 
# ---------- 1. CSP definition ----------
variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
 
domains = {v: ["Red", "Green", "Blue"] for v in variables}
 
# Adjacency (neighbors) - binary constraints: color(A) != color(B)
neighbors = {
    "WA":  ["NT", "SA"],
    "NT":  ["WA", "SA", "Q"],
    "SA":  ["WA", "NT", "Q", "NSW", "V"],
    "Q":   ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V":   ["SA", "NSW"],
    "T":   [],
}
 
 
# ---------- 2. Constraint check ----------
def is_consistent(var, color, assignment):
    """A color is consistent if no already-colored neighbor has the same color."""
    for n in neighbors[var]:
        if assignment.get(n) == color:
            return False
    return True
 
 
# ---------- 3. Backtracking search ----------
def select_unassigned_variable(assignment):
    """Pick the next unassigned variable (simple static order)."""
    for v in variables:
        if v not in assignment:
            return v
    return None
 
 
def backtrack(assignment):
    # Goal test: all variables assigned
    if len(assignment) == len(variables):
        return assignment
 
    var = select_unassigned_variable(assignment)
 
    for color in domains[var]:
        if is_consistent(var, color, assignment):
            assignment[var] = color              # make assignment
            result = backtrack(assignment)       # recurse
            if result is not None:
                return result
            del assignment[var]                  # undo (backtrack)
 
    return None                                  # failure -> backtrack
 
 
# ---------- 4. (Optional) count all solutions ----------
def count_solutions(assignment):
    if len(assignment) == len(variables):
        return 1
    var = select_unassigned_variable(assignment)
    total = 0
    for color in domains[var]:
        if is_consistent(var, color, assignment):
            assignment[var] = color
            total += count_solutions(assignment)
            del assignment[var]
    return total
 
 
# ---------- 5. Main ----------
if __name__ == "__main__":
    print("Map Coloring CSP (Australia) - Backtracking Search\n")
    solution = backtrack({})
 
    if solution:
        print("Solution found:")
        for region in variables:
            print(f"  {region:<4} -> {solution[region]}")
        print("\nTotal number of valid colorings:", count_solutions({}))
    else:
        print("No solution exists.")