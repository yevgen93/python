class Sequence:
    def __init__(self, a):
        self.a = a

    # returns x numbers as a list
    def take(self,x):
        return tuple(self.a[0:x])

    # returns the xth number
    def get(self,x):
        return int(self.a[x-1])

    # add x to every element in the list
    def add(self,x):
        new_seq = list(self.a)
        for i in new_seq:
            new_seq[i] += x
        return tuple(new_seq)

    # subtract x from every element in the list
    def sub(self,x):
        new_seq = list(self.a)
        for i in new_seq:
            new_seq[i] -= x
        return tuple(new_seq)

    # Multiply every element in the list by x
    def mult(self,x):
        new_seq = list(self.a)
        for i in new_seq:
            new_seq[i] *= x
        return tuple(new_seq)

    # Divide every element in the list by x
    def div(self,x):
        new_seq = list(self.a)
        for i in new_seq:
            new_seq[i] /= x
        return tuple(new_seq)


seq = Sequence([0,1,2,3,4,5])
print(seq.take(3))
print(seq.get(3))
print(seq.add(1))
print(seq.sub(1))
print(seq.mult(2))
print(seq.div(2))
# print(seq.add(1).seq.mult(3).add(5).take(10))
