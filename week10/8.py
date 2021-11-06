f, s, t, o, y = int(input()), int(input()), int(input()), 0, 0
if f > s and f > t:
    o = f
    if s > t:
        y = t
    else:
        y = s
elif s > f and s > t:
    o = s
    if f > t:
        y = t
    else: 
        y = f
else:
    o = t
    if f > s:
        y = s
    else: 
        y = f
print(f"The oldest is {o} of age.\nThe youngest is {y} of age.")