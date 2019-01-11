class MathDojo:
    def __init__(self):
        self.total = 0

    def add(self, *args):
        for arg in range(len(args)):
            if isinstance(args[arg], list) or isinstance(args[arg], tuple):
                for ele in args[arg]:
                    self.total += ele
            else:
                self.total += args[arg]
        return self

    def subtract(self, *args):
        for arg in range(len(args)):
            if isinstance(args[arg], list) or isinstance(args[arg], tuple):
                for ele in args[arg]:
                    self.total -= ele
            else:
                self.total -= args[arg]
        return self

    def result(self):
        return self.total


md = MathDojo()
x = md.add(2).add(2, 5, 1).subtract(3, 2).result()
md1 = MathDojo()
y = md1.add((1, 2, 3, 4, 5)).subtract([1,2,3,4]).result()
print(x)
print(y)
