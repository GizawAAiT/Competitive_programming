def get_primes(n):
      sieve = [True] * (n + 1)
      primes = set()
      for i in range(2, n + 1):
         if sieve[i]:
            primes.add(i)
            for j in range(i, n + 1, i):
               sieve[j] = False
      return primes

n = int(input())
a = [int(_) for _ in input().split()]

one, two = [0, 0]
for x in a:
    if x == 1:
        one += 1
    else:
        two += 1

primes = get_primes(sum(a))
result = []
max_primes = [0]
def backtrack(tot, path, one, two, count):
    global result
    if max_primes[0] < count:
        max_primes[0] = count
        result = path[:]
    if one <= 0 and two <= 0:
        return
    
    if not one:
        path.append(2)
        tot += 2
        two -= 1
        backtrack(tot, path, one, two, count + 1 if tot in primes else count)
    
    elif not two:
        path.append(1)
        tot += 1
        one -= 1
        backtrack(tot, path, one, two, count + 1 if tot in primes else count)
    
    else:
        path.append(1)
        tot += 1
        one -= 1
        backtrack(tot, path, one, two, count + 1 if tot in primes else count)
        # backtrack
        path.pop()
        path.append(2)
        tot += 1
        one += 1
        two -= 1
        backtrack(tot, path, one, two, count + 1 if tot in primes else count)
backtrack(0, [], one, two, 0)
print(*result)
