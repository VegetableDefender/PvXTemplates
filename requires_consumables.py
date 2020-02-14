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


def generate_template(target="requires_consumables.pvx"):
    with open("consumables.json") as jf:
        DATA = json.load(jf)

    with open("requires_consumables.j2") as tf:
        template = Template(tf.read())

    tpl_parts = []

    for cat in DATA.values():
        for item in cat:
            parts = [
                "{{#ifeq: {{lc: {{{%s|}}} }}" % (item["params"][0],),
                f"| yes | *[[File:{item['file']}|35px|link=gww:{item['name']}",
                f"]] [[gww:{item['file']}|{item['file']}]]",
                "}}<!--\n-->",
            ]
            tpl_parts.append(parts)

    parser_functions = "".join(justify_parts(tpl_parts))

    with open(target, "w") as tf:
        tf.write(template.render(parser_functions=parser_functions, catgories=DATA))


if __name__ == "__main__":
    generate_template()
