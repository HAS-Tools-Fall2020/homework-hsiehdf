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
