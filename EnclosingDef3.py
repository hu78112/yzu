# 嵌套函式

def make_lotto(n):
    def mult(x):
        return n * x
    return mult

m3 = make_lotto(3) # n =3
m5 = make_lotto(5) # n =5

print(m3(6)) # x = 6
print(m5(7)) # x = 7

print(m3(m5(2)))