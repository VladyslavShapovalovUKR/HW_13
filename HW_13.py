#1 task
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

#2
def to_dict(lst):
    return {element: element for element in lst}

#3
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end+1))


