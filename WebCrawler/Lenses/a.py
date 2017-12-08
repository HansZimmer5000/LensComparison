from GhLens import GhLens

class A:
    def __init__(self):
        pass

g = GhLens({"_id": "name", "mount": "", "length": ""})
print(g.lens_dict)
g.update({"_id": "name", "mount":"Nikon", "length": ""})
print(g.lens_dict)
g.update({"_id": "name", "mount":"Canon", "length":"300mm"})
print(g.lens_dict)

print(g.equals(""))
print(g.equals(A()))