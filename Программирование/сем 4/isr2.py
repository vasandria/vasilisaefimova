def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        with open('logs.txt', "w") as f:
          f.write(str(result))
        return result
    return wrapper


@logger
def calc(x, y, s):
  x = float(input("x="))
  y = float(input("y="))
  if s == '+':
    print("%.2f" % (x+y))
  elif s == '-':
    print("%.2f" % (x-y))
  elif s == '*':
    print("%.2f" % (x*y))
  elif s == '/':
    if y != 0:
      print("%.2f" % (x/y))
    else:
      print("Деление на ноль!")