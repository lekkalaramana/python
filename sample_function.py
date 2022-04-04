# def modify(arg):
#     arg.append(7)
#     print("arg =", arg)
#
# modify([3,34,32])
#
#
# # mutable obejects with default value
#
# def add_value(arr=[]):
#     arr.append('default')
#     return arr
#
# add_value()
#
# # immutable obejects with default value
#
# def add_value(arr = None):
#     if arr is None:
#         arr = []
#     arr.append('default')
#     return arr
#
# add_value()

def add_value(arr=[]):
    if arr is None:
        arr = []
    arr.append('default')
    return arr

add_value()


# Rebind global names into a local namespace

count = 0
def show_count():
    print(count)

def set_count(arg):
    count = arg

def set_count(arg):
    global count
    count = arg

show_count()

set_count(5)
show_count()
