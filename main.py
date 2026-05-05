"""Menu interativo da biblioteca."""

import imperativo
import funcional
import armazenamento


def exibir_menu():
    print("\n" + "=" * 50)
    print("       BIBLIOTECA - SISTEMA DE LIVROS")
    print("=" * 50)
    print("--- Operações IMPERATIVAS (mudam estado) ---")
    print("1. Adicionar livro")
    print("2. Atualizar livro")
    print("3. Remover livro")
    print("4. Buscar livro por ID")
    print("--- Operações FUNCIONAIS (consultas) ---")
    print("5. Listar todos os livros")
    print("6. Filtrar por autor")
    print("7. Filtrar por título")
    print("8. Filtrar por ano mínimo")
    print("9. Listar autores únicos")
    print("10. Total de páginas (todos os livros)")
    print("11. Livro mais antigo / mais recente")
    print("12. Média de páginas por autor")
    print("0. Sair")
    print("=" * 50)


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_texto(mensagem, permitir_vazio=False):
    while True:
        entrada = input(mensagem).strip()
        if entrada or permitir_vazio:
            return entrada
        print("O valor não pode estar vazio.")


def acao_adicionar(livros):
    print("\n-- Adicionar Livro --")
    titulo = ler_texto("Título: ")
    autor = ler_texto("Autor: ")
    ano = ler_inteiro("Ano de publicação: ")
    paginas = ler_inteiro("Número de páginas: ")

    novo = imperativo.adicionar_livro(livros, titulo, autor, ano, paginas)
    armazenamento.salvar_livros(livros)
    print(f"\n✓ Livro adicionado com sucesso! ID: {novo['id']}")


def acao_atualizar(livros):
    print("\n-- Atualizar Livro --")
    id_livro = ler_inteiro("ID do livro a atualizar: ")

    livro = imperativo.buscar_por_id(livros, id_livro)
    if livro is None:
        print("✗ Livro não encontrado.")
        return

    print(f"Livro atual: {livro['titulo']} — {livro['autor']}")
    print("Pressione ENTER para manter o valor atual.\n")

    novo_titulo = ler_texto(f"Novo título [{livro['titulo']}]: ", permitir_vazio=True)
    novo_autor = ler_texto(f"Novo autor [{livro['autor']}]: ", permitir_vazio=True)
    novo_ano_str = input(f"Novo ano [{livro['ano']}]: ").strip()
    novas_pag_str = input(f"Novo nº páginas [{livro['paginas']}]: ").strip()

    novos_dados = {}
    if novo_titulo:
        novos_dados["titulo"] = novo_titulo
    if novo_autor:
        novos_dados["autor"] = novo_autor
    if novo_ano_str:
        try:
            novos_dados["ano"] = int(novo_ano_str)
        except ValueError:
            print("✗ Ano inválido, mantendo o valor anterior.")
    if novas_pag_str:
        try:
            novos_dados["paginas"] = int(novas_pag_str)
        except ValueError:
            print("✗ Páginas inválidas, mantendo o valor anterior.")

    if imperativo.atualizar_livro(livros, id_livro, novos_dados):
        armazenamento.salvar_livros(livros)
        print("✓ Livro atualizado com sucesso!")
    else:
        print("✗ Não foi possível atualizar.")


def acao_remover(livros):
    print("\n-- Remover Livro --")
    id_livro = ler_inteiro("ID do livro a remover: ")

    if imperativo.remover_livro(livros, id_livro):
        armazenamento.salvar_livros(livros)
        print("✓ Livro removido com sucesso!")
    else:
        print("✗ Livro não encontrado.")


def acao_buscar_por_id(livros):
    id_livro = ler_inteiro("ID do livro: ")
    livro = imperativo.buscar_por_id(livros, id_livro)

    if livro is None:
        print("✗ Livro não encontrado.")
    else:
        print(f"\nID: {livro['id']}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"Páginas: {livro['paginas']}")


def acao_listar_todos(livros):
    if len(livros) == 0:
        print("\n(Nenhum livro cadastrado)")
        return

    print("\n-- Todos os Livros --")
    for linha in funcional.listar_resumos(livros):
        print(linha)


def acao_filtrar_por_autor(livros):
    autor = ler_texto("Nome do autor (parcial): ")
    resultado = funcional.filtrar_por_autor(livros, autor)

    if len(resultado) == 0:
        print("Nenhum livro encontrado.")
    else:
        for linha in funcional.listar_resumos(resultado):
            print(linha)


def acao_filtrar_por_titulo(livros):
    titulo = ler_texto("Trecho do título: ")
    resultado = funcional.filtrar_por_titulo(livros, titulo)

    if len(resultado) == 0:
        print("Nenhum livro encontrado.")
    else:
        for linha in funcional.listar_resumos(resultado):
            print(linha)


def acao_filtrar_por_ano(livros):
    ano = ler_inteiro("Ano mínimo: ")
    resultado = funcional.filtrar_por_ano_minimo(livros, ano)

    if len(resultado) == 0:
        print("Nenhum livro encontrado.")
    else:
        for linha in funcional.listar_resumos(resultado):
            print(linha)


def acao_listar_autores(livros):
    autores = funcional.listar_autores_unicos(livros)

    if len(autores) == 0:
        print("(Nenhum autor cadastrado)")
    else:
        print("\n-- Autores únicos --")
        for autor in autores:
            print(f"- {autor}")


def acao_total_paginas(livros):
    total = funcional.total_de_paginas(livros)
    qtd = funcional.contar_livros(livros)
    print(f"\nTotal de livros: {qtd}")
    print(f"Total de páginas (somadas): {total}")


def acao_extremos(livros):
    antigo = funcional.livro_mais_antigo(livros)
    recente = funcional.livro_mais_recente(livros)

    if antigo is None:
        print("(Nenhum livro cadastrado)")
        return

    print(f"\nMais antigo: {antigo['titulo']} ({antigo['ano']}) — {antigo['autor']}")
    print(f"Mais recente: {recente['titulo']} ({recente['ano']}) — {recente['autor']}")


def acao_media_paginas_autor(livros):
    autor = ler_texto("Nome do autor: ")
    media = funcional.media_paginas_por_autor(livros, autor)

    if media == 0:
        print("Nenhum livro encontrado para esse autor.")
    else:
        print(f"\nMédia de páginas dos livros de '{autor}': {media:.1f}")


def main():
    livros = armazenamento.carregar_livros()

    print("Bem-vindo(a) ao sistema da biblioteca!")
    if len(livros) > 0:
        print(f"({len(livros)} livro(s) carregado(s) do arquivo)")

    executando = True
    while executando:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            acao_adicionar(livros)
        elif opcao == "2":
            acao_atualizar(livros)
        elif opcao == "3":
            acao_remover(livros)
        elif opcao == "4":
            acao_buscar_por_id(livros)
        elif opcao == "5":
            acao_listar_todos(livros)
        elif opcao == "6":
            acao_filtrar_por_autor(livros)
        elif opcao == "7":
            acao_filtrar_por_titulo(livros)
        elif opcao == "8":
            acao_filtrar_por_ano(livros)
        elif opcao == "9":
            acao_listar_autores(livros)
        elif opcao == "10":
            acao_total_paginas(livros)
        elif opcao == "11":
            acao_extremos(livros)
        elif opcao == "12":
            acao_media_paginas_autor(livros)
        elif opcao == "0":
            print("\nAté logo!")
            executando = False
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
