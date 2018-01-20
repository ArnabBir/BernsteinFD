class FunctionalDependency:

    def __init__(self, lhs, rhs):
        self.lhs = set(lhs.split(","))
        self.rhs = set(rhs.split(","))

    def __str__(self):
        FD = "[ " + ", ".join(str(lhs) for lhs in self.lhs)
        FD += " ] -> [ " + ", ".join(str(rhs) for rhs in self.rhs) + " ]"
        return FD

    
