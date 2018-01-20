from FunctionalDependency import *
from Bernstein import *

def main():

    n = int(raw_input("Enter the number of functional dependencies : "))
    fd_list = []

    for i in xrange(n):
        s = raw_input("Enter the functional dependency no. " + str(i+1)+ " : ")
        fd_list.append(FunctionalDependency(s.split("->")[0], s.split("->")[1]))

    x = raw_input("Enter X : ")
    print "\n"
    bernstein_algo = Bernstein(fd_list)
    print bernstein_algo
    print "Closure of X (X+) : [ " + ", ".join(str(s) for s in bernstein_algo.getclosure(x)) + " ]"
    print "Is X key of for the FDs ? " + str(bernstein_algo.iskey(x))


main()