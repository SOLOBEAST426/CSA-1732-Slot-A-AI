family = {
    "John": ["Paul", "Lisa"],
    "Mary": ["Paul", "Lisa"],
    "Paul": ["David"],
    "Susan": ["David"]
}

def find_children(parent):
    if parent in family:
        print("Children of", parent, ":", ", ".join(family[parent]))
    else:
        print("No children found.")

def find_parents(child):
    parents = []
    for parent, children in family.items():
        if child in children:
            parents.append(parent)

    if parents:
        print("Parents of", child, ":", ", ".join(parents))
    else:
        print("No parents found.")

def find_siblings(person):
    parents = []
    for parent, children in family.items():
        if person in children:
            parents.append(parent)

    siblings = set()
    for parent in parents:
        siblings.update(family[parent])

    siblings.discard(person)

    if siblings:
        print("Siblings of", person, ":", ", ".join(sorted(siblings)))
    else:
        print("No siblings found.")

find_children("John")
find_parents("Paul")
find_siblings("Paul")