# 裝飾器

def mak_dress(func):
    def dress():
        print("穿衣服")
        func()
    return dress

def out():
    print("我出門了")

john = mak_dress(out)
john()