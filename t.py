import json

with open("consumables.json") as jf:
    data = json.load(jf)


new_data = []

for cat, items in data.items():
    new_data.append(
        {"name": cat, "selectable": False, "items": items}
    )


with open("_consumables.json", "w") as jf:
    json.dump(new_data, jf, indent=1)
