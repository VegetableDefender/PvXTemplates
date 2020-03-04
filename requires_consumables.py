import json
from jinja2 import Template


def justify_parts(tpl_parts):
    parts_to_fill = len(tpl_parts[0]) - 1
    longest = []

    for i in range(parts_to_fill):
        longest.append(max(len(p[i]) for p in tpl_parts))

    out = []

    for line_parts in tpl_parts:
        line = ""
        for i in range(parts_to_fill):
            line += line_parts[i] + (" " * (longest[i] - len(line_parts[i])))
        line += line_parts[i + 1]
        out.append(line)

    return out


def write_params(params):
    if not params:
        return ""
    return "{{{%s | %s }}}" % (params.pop(), write_params(params))


def generate_template(target="requires_consumables"):
    with open("consumables.json") as jf:
        DATA = json.load(jf)

    with open("requires_consumables.j2") as tf:
        template = Template(tf.read())

    tpl_parts = []

    for cat in DATA:
        items = cat["items"]
        if cat["selectable"]:
            items = [*items, dict(name=cat["name"], file=cat["file"], params=cat["params"], wiki=cat.get("wiki"))]
        for item in items:
            wiki_name = item.get('wiki', item['name'])
            parts = [
                "{{#ifeq: {{lc: %s }}" % (write_params(list(reversed(item["params"]))),),
                f"| yes | *[[File:{item['file']}|35px|link=gww:{wiki_name}",
                f"]] [[gww:{wiki_name}|{item['name']}]]",
                "}}<!--\n-->",
            ]
            tpl_parts.append(parts)

    parser_functions = "".join(justify_parts(tpl_parts))


    with open(target+".pvx", "w") as tf:
        tf.write(template.render(parser_functions=parser_functions, catgories=DATA))


if __name__ == "__main__":
    generate_template()
