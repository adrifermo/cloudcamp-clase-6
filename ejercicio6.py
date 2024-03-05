# function with variable-length keyword arguments
def percentage(**kwargs):
    sum = 0
    items = 0
    
    for sub, value in kwargs.items():
        # get argument name
        sub_name = sub
        # get argument value
        sub_marks = value
        print(sub_name, "=", sub_marks)
        items = items + 1
        sum = sum + value
    
    return(sum/items)

# pass multiple keyword arguments

avg = str(percentage(math=56, english=61, science=73))
print("AVG: " + avg)
