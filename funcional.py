"""Consultas e agregações no paradigma funcional: funções puras com map, filter, reduce."""

from functools import reduce


def filtrar_por_autor(livros, autor):
    autor_lower = autor.lower()
    return list(filter(
        lambda livro: autor_lower in livro["autor"].lower(),
        livros
    ))


def filtrar_por_titulo(livros, titulo):
    titulo_lower = titulo.lower()
    return list(filter(
        lambda livro: titulo_lower in livro["titulo"].lower(),
        livros
    ))


def filtrar_por_ano_minimo(livros, ano_minimo):
    return list(filter(lambda livro: livro["ano"] >= ano_minimo, livros))


def filtrar_livros_extensos(livros, paginas_minimas=300):
    return list(filter(lambda livro: livro["paginas"] >= paginas_minimas, livros))


def listar_titulos(livros):
    return list(map(lambda livro: livro["titulo"], livros))


def listar_resumos(livros):
    return list(map(
        lambda l: f"[{l['id']}] {l['titulo']} — {l['autor']} ({l['ano']})",
        livros
    ))


def listar_autores_unicos(livros):
    autores = list(map(lambda livro: livro["autor"], livros))
    return sorted(set(autores))


def total_de_paginas(livros):
    return reduce(lambda acc, livro: acc + livro["paginas"], livros, 0)


def contar_livros(livros):
    return reduce(lambda acc, _: acc + 1, livros, 0)


def livro_mais_antigo(livros):
    if len(livros) == 0:
        return None
    return reduce(
        lambda atual, prox: atual if atual["ano"] <= prox["ano"] else prox,
        livros
    )


def livro_mais_recente(livros):
    if len(livros) == 0:
        return None
    return reduce(
        lambda atual, prox: atual if atual["ano"] >= prox["ano"] else prox,
        livros
    )


def media_paginas_por_autor(livros, autor):
    """Combina filter + map + reduce para calcular a média de páginas de um autor."""
    livros_do_autor = filtrar_por_autor(livros, autor)
    if len(livros_do_autor) == 0:
        return 0

    paginas = list(map(lambda livro: livro["paginas"], livros_do_autor))
    soma = reduce(lambda a, b: a + b, paginas, 0)
    return soma / len(paginas)
