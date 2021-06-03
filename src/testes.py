dic = dict(a="1")


def teste(a=None, b=None):
    print(f"a: {a}")
    print(f"b: {b}")


teste(**dic)
