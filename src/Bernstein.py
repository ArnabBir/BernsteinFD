class Bernstein:

    def __init__(self, fds):

        self.fds = fds
        self.set_u = set()
        for fd in fds:
            self.set_u = self.set_u.union(fd.lhs).union(fd.rhs)

    def __str__(self):

        bernstein = "Bernstein Model : \n"
        bernstein += "Set of attributes : [ " + ", ".join(self.set_u) + " ]\n"
        bernstein += "Functional dependencies : \n"
        for fd in self.fds:
            bernstein += str(fd) + "\n"
        return bernstein

    def addfd(self, fd):
        self.fds.append(fd)

    def getclosure(self, x):

        x = set(x.split(','))
        closure_x = x
        while True:
            x = closure_x
            for fd in self.fds:
                if fd.lhs.issubset(x):
                    closure_x = closure_x.union(fd.rhs)
            if x == closure_x:
                break

        return closure_x

    def iskey(self, x):

        return self.set_u == self.getclosure(x)
