import random, sys


def rearrange(arg):
    #move all arguments into a list
    args = list(arg)

    #Loop through length of list
    for i in range(len(args)):
        l = random.randint(0, i)

        #Based this off of example in bottom of the file
        args[i], args[l] = args[l], args[i]

    return args


if __name__ == '__main__':
    input = sys.argv[1:]
    rearranged = rearrange(input)
    print(rearranged)




# Example I found from StackOverFlow to assist me with task

# a = [1, 2, 3]
# a[0], a[2] = a[2], a[0]
# a
#
# [3, 2, 1]
