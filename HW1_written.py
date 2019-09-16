#Eliot Brown
#CS 1134



# WRITEN PART
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