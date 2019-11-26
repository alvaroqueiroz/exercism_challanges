import re

class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if input_string == "(;)":
        return SgfTree()
    else:
        # Regex to find child nodes
        vr = r"\[((?:[A-Za-z\s]|\\.)+)\]"
        pr = r"([A-Z]+)((?:" + vr + ")+)"

        # Regex to find properties
        sr = r"\(;(?P<node>(" + pr + ")+)(?P<children>(\(?;" + pr + "\))*)\)?"

        # find if have mathes
        input_match = re.match(sr, input_string)
        if input_match:
            # get mathces
            children_matching = re.findall(pr, input_match["children"])
            children = []
            for child in children_matching:
                children.append(SgfTree({child[0]: re.findall(vr, child[1])}))

            properties = {}
            # get properties
            for key, values, _ in re.findall(pr, input_match["node"]):
                values = re.findall(vr, values)
                values = [v.replace("\t", " ").replace("\\", "") for v in values]
                properties[key] = values
            # make sgf tree thats corresponds to the string
            return SgfTree(properties, children)

# testing
print(parse('(;A[B](;B[C])(;C[D]))') == SgfTree(properties={'A': ['B']},children=[SgfTree({'B': ['C']}),SgfTree({'C': ['D']}),]))

