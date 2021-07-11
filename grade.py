def grade(s):
    if s>=1.0:
        return 'in-appropriate score entered!!'
    elif s>=0.9:
        return 'A'
    elif s>=0.8:
        return 'B'
    elif s>=0.7:
        return 'C'
    elif s>=0.6:
        return 'D'
    elif s>=0.0:
        return 'F'
    else:
        return 'score cannot be negative!!'
sc=input("enter score: ")
score=float(sc)
g=grade(score)
print("grade:-",g)