def get_prime(n):
  verdict = "prime"
  for i in range(2,n-1):
    if n/i % 1 == 0:
      verdict = "not prime"
  return verdict

def prime_finder(n):
  primelist = []
  for i in range(2,n+1):
    if get_prime(i) == "prime":
      primelist.append(i)
  return primelist

print(prime_finder(11))
