class Object(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Object %r" % self.__dict__

p = Object(x = 300, y = 400)
print(p)
print(p.x)
print(p.y)
p.x += 10
print(p)
print(p.x)
