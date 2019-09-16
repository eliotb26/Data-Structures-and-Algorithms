
class Polynomial:

    def __init__(self, lst):
        self.lst = lst

    def __repr__(self):
        poly = []
        for i in range(len(self.lst)):
            if i == 0:
                poly.append(str(self.lst[i]))
            elif i == 0 and i == len(self.lst):
                poly = []
            else:
                power = i
                poly.append((str(self.lst[i]) + 'x ^' + str(power)))
        poly.reverse()
        strpoly = " + ".join(poly)
        return strpoly

    def eval(self, val):
        tot = 0
        for i in range(len(self.lst)):
            if i == 0:
                tot += self.lst[i]
            elif i == 1:
                tot += self.lst[i] * val
            else:
                tot += self.lst[i] * val ** i
        return tot

    def __add__(self, other):
        addlist = []
        if len(self.lst) <= len(other):
            minlist = self.lst
            maxlist = other
        else:
            minlist = other
            maxlist = self.lst
        print(maxlist)
        for i in range(len(minlist)):
            sumplace = self.lst[i] + other[i]
            addlist.append(sumplace)
        if len(self.lst) != len(other):
            for extra in range(len(minlist), len(maxlist)):
                addlist.append(maxlist[extra])
        return Polynomial(addlist)

    def __mul__(self, other):
        temp_lst = []
        multi_lst = [0] * (len(self.lst) + len(other.lst))
        for val in range(len(self.lst)):
            for num in range(len(other.lst)):
                x_val = num + val
                total = other.lst[num] * self.lst[val]
                temp_lst.append((total,x_val))
        print(temp_lst)
        for num,pos in temp_lst:
            multi_lst[pos] += num
        for i in range(len(multi_lst)-1,0,-1):
            if multi_lst[i] == 0:
                multi_lst.pop(i)
            else:
                break
        print(multi_lst)
        return Polynomial(multi_lst)

    def polySequence(self, start, end, step=1):
        for i in range(start, end, step):
            num = self.eval(i)
            yield num



p1 = Polynomial([1,2])
p2 = Polynomial([0,2,3])
print(p1 + p2)
print(p1 * p2)

#for val in p1.polySequence(0,5):
    #print(val)