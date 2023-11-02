num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

def karatsuba(x, y):
  if x < 10 or y < 10:
      return x * y
  else:
      n = max(len(str(x)), len(str(y)))
      n2 = (n + 1) // 2 
      a = x // (10 ** n2)
      b = x % (10 ** n2)
      c = y // (10 ** n2)
      d = y % (10 ** n2)
      ac = karatsuba(a, c)
      bd = karatsuba(b, d)
      ad_bc = karatsuba(a + b, c + d) - ac - bd
      result = ac * (10 ** (2 * n2)) + ad_bc * (10 ** n2) + bd
      return result

print(karatsuba(num1, num2))
