#! python
def tag_lista(*items):
    lista = ''.join((f'<li>{item}</li>' for item in items))
    return f'<ul>{lista}</ul>'


print(tag_lista('Pedro', 'Marcia', 'John'))
