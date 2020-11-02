# %%

import json
import pandas as pd
# %%

dict = {}
dict["name"] = "Chaya"
dict["age"] = 12
dict["city"] = "Boulder"
dict["type"] = "Canine"

dict
# %%
json_example = json.dumps(dict, ensure_ascii=False)

json_example
# %%
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# %%
x = thisdict["model"]
# %%
x = thisdict.get("model")
# %%
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
# %%
for x in thisdict:
    print(thisdict[x])
# %%
for x in thisdict.values():
  print(x)
# %%
for x, y in thisdict.items():
  print(x, y)
# %%
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# %%
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# %%
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
# %%
