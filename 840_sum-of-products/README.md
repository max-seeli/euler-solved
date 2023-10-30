# Problem
A __partition__ of `n` is a set of positive integers for which the sum equals `n`. 

The partitions of 5 are:
```
{5}, {1,4}, {2,3}, {1,1,3}, {1,2,2}, {1,1,1,2}, {1,1,1,1,1}
```

Further we define the function `D(p)` as:
```
D(1) = 1
D(p) = 1, for any prime p
D(pq) = D(p)q + pD(q), for any positive integers p, q > 1
```

Now let `{a1, a2, ..., ak}` be a partition of `n`.

We assign to this particular partition the value:
```
P = mult(aj) for j = 1 to k
```

`G(n)` is the sum of P for all partitions of `n`.

We can verify that `G(10) = 164`.

We also define:
```
S(N) = sum(G(n)) for n = 1 to N
```

You are given `S(1)=396`.

Find S(5*10^4) mod 999676999.

Link: [https://projecteuler.net/problem=840](https://projecteuler.net/problem=840)