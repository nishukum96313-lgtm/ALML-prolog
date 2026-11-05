def unify(x,y):
    if x==y:
        return
    if x.islower():   #true ya false mai dega
        return {x,y}
    if y.islower():
        return {y,x}

print(unify("x","Ram")) #1st unification
print("A","A")  # unification nahi hoga kyuki dono same values hai A
print("x","y")  #unification hoga
