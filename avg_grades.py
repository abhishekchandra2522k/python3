def avg_grades(*grades):
    """
    Calculates average of the grades provided.
    Can take many number of grades due to * 
    """

    i=0
    sum=0.0
    for grade in grades:
        sum = sum + grade
        i=i+1
    avg = sum / i
    return avg

avg = avg_grades(2.5,3.0,3.5)
print(avg)
