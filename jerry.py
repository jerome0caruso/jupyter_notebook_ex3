def area(len, wid):
    if type(len) == int and type(wid) == int:
        return len * wid  
    else:
        return("Error: Please enter valid numbers.")    



def circumference(radius):
    if type(radius) == int:
        return round(3.1415 * radius * 2, 2)

      