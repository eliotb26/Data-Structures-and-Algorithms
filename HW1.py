#Eliot Brown

#1
def harmonic(n):
    i = 1
    total = 0
    while i <= n:
        val = 1 / i
        total += val
        i += 1
    return total
#print(harmonic(5))

def harmonicV2(n):
    harmonic_total = sum([1/i for i in range(1, n + 1)])
    return harmonic_total
#print(harmonicV2(5))

#2
def find_primes(n):
    prime_lst = []
    if n == 0:
        return []
    for i in range(2, n+1):
        val = False
        for k in range(2, int(i**0.5)+1):
            if i % k == 0:
                val = True
                break
        if val == False:
            prime_lst.append(i)
    return prime_lst

#print(find_primes(17))


def prime_lst(n):
    prime_list = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p*p <= n):
        if (prime[p] == True):
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            prime_list.append(p)
    return prime_list

#print(prime_lst(17))

#3
def leonardo(n):
    a, b = 1, 1
    for i in range(0,n):
        if i == 0 or i == 1:
            yield 1
        else:
            c = a + b + 1
            a,b = b,c
            yield c

#for val in leonardo(7):
#    print(val,end=" ")

#4

import ctypes

def make_array(n):
    return (ctypes.py_object * n)()

class MyList:
    def __init__(self):
        self.data = make_array(1) #stores elem
        self.capacity = 1
        self.n = 0

    def __repr__(self):
        if self.n == 0:
            return '[]'
        var = '['
        for i in range(self.n):
            var += str(self.data[i]) + ', '
        var = var[:-2]
        var += ']'
        return var

    def append(self, val):
        # append: O(1) amortized
        if self.n == self.capacity:
            self.resize(self.capacity * 2)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_capacity):
        # resize: O(n), where n is number of elements in list
        new_data = make_array(new_capacity)
        for i in range(self.n):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __getitem__(self, ind):
        # Runinng time O(1)
        if not (0 <= ind <= self.n - 1):
            raise IndexError(str(ind) + " is out of range")
        return self.data[ind]

    def __setitem__(self, ind, value):
        # Running time O(1)
        if not (0 <= ind <= self.n - 1):
            raise IndexError(str(ind) + " is out of range")
        self.data[ind] = value

    def extend(self, other):
        # extend: O(k) amortized, where k is number of elements in other
        for elem in other:
            self.append(elem)

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def __add__(self, other):
        new_lst = MyList()
        new_lst.extend(self)
        new_lst.extend(other)

        return new_lst

    def __mul__(self, n):
        new_lst = MyList()
        for i in range(1, n+1):
            new_lst.extend(self)
        return new_lst

    def __rmul__(self, n):
        new_lst = MyList()
        for i in range(1, n+1):
            new_lst.extend(self)
        return new_lst
'''
def main():
    lst1 = MyList()
    for i in range(1,4):
        lst1.append(i)
    print(lst1)
    lst2 = MyList()
    for i in range(4,7):
        lst2.append(i)
    print(lst2)
    lst3 = lst1 + lst2
    print(lst3)
main()
'''

#5
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

#print(gcd(10, 100))

#WRITEN PART
''' Theta = Big Theta
#1 a)
    Theta(n)
    
    b)
    Theta(n**2)
    
    c) 
    Theta(log(n))
    
2 a)
    3n**4 + 8n**3 − 3n = Θ(n**4)
    3n**4 <= 3n**4 + 8n**3 − 3n <= 3n**4 + 8n**3 <= 3n**4 + 8n**4 = 11n**4
    
    find n value :
    8n**3 - 3n >= 0
    8n**2 >= 3
    n >= (3/8)**0.5
ANS    n**4 <= 3n**4 <= 11n**4
    
    c_1 = 11
    c_2 = 3
    n_o >= 1 
    
    b)
    (17n**2 + 4n - 7)**0.5 = Θ(n)
    17n <= (17n**2 + 4n - 7)**0.5 <= 17n + 4n = 21n 
    17n <= (17n**2 + 4n - 7)**0.5 <= 21n
    
    4n-7>=0
    4n>=7
    n>=2
     
    c_1 = 17
    c_2 = 21
    n_0 >= 2  #n to work for both smaller and upper !!
    
    c) if f(n) = O(g(n)) and g(n) = O(h(n)). This would show that 
    f(n) <= c * g(n) for some values of n and c. Then the second 
    one would show that g(n) <= c2 * h(n) for some values of n and c. 
    This would then show that f(n) <= c*g(n) <= c2*h(n) for some values
    for c's and n's.   
    

#3 
    The run time for this would be Theta(n(n**0.5)). This would be 
    because this iterates through the values up to n, but then within
    it iterates through the square root of the specific i value that
    it is on. This would normally cause it to be n^2 run time, but 
    since it is the square root of the i value that it originally 
    iterated from, it results in iterating the iterator to the square
    of the value causing n * n**0.5 as its worst run time. 
    
#4
    a)
    The worst running time for reverse1 is n^2. This is because it 
    would iterate through the list, then insert which would have to 
    reform the list by changing the position of the values n times. 
    This would cause the worst run time to be n^2.
    
    
    b) the worst running time for reverse2 is (n). This is because
    this is because this iterates through the list for each value with
    append as the only primitive action on the code O(1). Therefore the
    worst runtime for this code is n. 
'''