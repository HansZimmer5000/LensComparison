from webcrawler.lenses.ghlens import GhLens

c = GhLens
g = c({"_id": "name", "mount": "", "length": ""})
print(g.lens_dict)
g.update({"_id": "name", "mount":"Nikon", "length": ""})
print(g.lens_dict)
g.update({"_id": "name", "mount":"Canon", "length":"300mm"})
print(g.lens_dict)