#! python
def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    assert tag_bloco('Incluído co sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'
