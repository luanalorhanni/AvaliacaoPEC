"""Operações CRUD no paradigma imperativo: mutação direta da lista de livros."""


def gerar_proximo_id(livros):
    maior_id = 0
    indice = 0

    while indice < len(livros):
        if livros[indice]["id"] > maior_id:
            maior_id = livros[indice]["id"]
        indice = indice + 1

    return maior_id + 1


def adicionar_livro(livros, titulo, autor, ano, paginas):
    novo_livro = {
        "id": gerar_proximo_id(livros),
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "paginas": paginas
    }
    livros.append(novo_livro)
    return novo_livro


def remover_livro(livros, id_livro):
    for indice in range(len(livros)):
        if livros[indice]["id"] == id_livro:
            livros.pop(indice)
            return True
    return False


def atualizar_livro(livros, id_livro, novos_dados):
    indice = 0
    while indice < len(livros):
        if livros[indice]["id"] == id_livro:
            if novos_dados.get("titulo"):
                livros[indice]["titulo"] = novos_dados["titulo"]
            if novos_dados.get("autor"):
                livros[indice]["autor"] = novos_dados["autor"]
            if novos_dados.get("ano") is not None:
                livros[indice]["ano"] = novos_dados["ano"]
            if novos_dados.get("paginas") is not None:
                livros[indice]["paginas"] = novos_dados["paginas"]
            return True
        indice = indice + 1
    return False


def buscar_por_id(livros, id_livro):
    for livro in livros:
        if livro["id"] == id_livro:
            return livro
    return None
