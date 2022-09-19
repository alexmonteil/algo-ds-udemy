# write a function which accepts a variable number of arguments
# and checks whether there are duplicates among the arguments

def duplicate_check(*args):

    arglen = len(args)

    if arglen == 0 or arglen == 1:
        return False

    counter = {}

    for i in range(arglen):
        if args[i] in counter:
            return True
        else:
            counter[args[i]] = args[i]
    
    return False


# solution 2

def duplicate_check2(*args):
    return len(set(args)) != len(args)


print(f"Should print True: {str(duplicate_check(1, 2, 3, 4, 1))}")
print(f"Should print False: {str(duplicate_check(1, 2, 3, 4))}")

print(f"Should print True: {str(duplicate_check2(1, 2, 3, 4, 1))}")
print(f"Should print False: {str(duplicate_check2(1, 2, 3, 4))}")