a = "ABDF"; b = "CGHE"; check = "ABCGDHE"

def h():
     global check
     c = a + b
     c = sorted(c); check = sorted(check)
     if c == check:
          return True
     return False

print(h())