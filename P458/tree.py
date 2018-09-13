# Tree Format
# {
#   'attribute': decision_attribute
#   'children': [
#       { 'if': class_value, 'then': sub_tree },
#       { 'if <': numeric_value, 'then': sub_tree },
#       ...,
#   ],
# }

TAB = '    '

def str_child(attr, child, tab):
    class_value = child['if']
    sub_tree    = child['then']
    return f'{tab}if {attr} = {class_value} then\n{str_tree(sub_tree, tab + TAB)}'

def str_tree(tree, tab=''):
    if 'attribute' in tree and 'children' in tree:
        attr     = tree['attribute']
        children = tree['children']
        return '\n'.join(map(lambda child: str_child(attr, child, tab), children))
    else:
        return f'{tab}{tree}'

def decide(tree, row, attrs):
    if 'attribute' in tree and 'children' in tree:
        attr     = tree['attribute']
        value    = row[attrs.index(attr)]
        children = tree['children']
        for child in children:
            if child['if'] == value:
                return decide(child['then'], row, attrs)
    else:
        return tree