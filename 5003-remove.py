def remove(str, n):
      first = str[:n] 
      last = str[n+1:]
      return first + last
print(remove('Python', 0))
print(remove('Python', 3))
print(remove('Python', 6))
