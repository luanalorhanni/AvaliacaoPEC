"""Cadastro em massa de livros para testes do sistema."""

import imperativo
import armazenamento


LIVROS_TESTE = [
    # Machado de Assis (3 livros)
    ("Dom Casmurro", "Machado de Assis", 1899, 256),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, 320),
    ("Quincas Borba", "Machado de Assis", 1891, 304),

    # José de Alencar (3 livros)
    ("Iracema", "José de Alencar", 1865, 144),
    ("O Guarani", "José de Alencar", 1857, 432),
    ("Senhora", "José de Alencar", 1875, 320),

    # Jorge Amado (3 livros)
    ("Capitães da Areia", "Jorge Amado", 1937, 280),
    ("Gabriela, Cravo e Canela", "Jorge Amado", 1958, 424),
    ("Dona Flor e Seus Dois Maridos", "Jorge Amado", 1966, 552),

    # Graciliano Ramos (2 livros)
    ("Vidas Secas", "Graciliano Ramos", 1938, 176),
    ("São Bernardo", "Graciliano Ramos", 1934, 224),

    # Clarice Lispector (2 livros)
    ("A Hora da Estrela", "Clarice Lispector", 1977, 96),
    ("A Paixão Segundo G.H.", "Clarice Lispector", 1964, 192),

    # Aluísio Azevedo
    ("O Cortiço", "Aluísio Azevedo", 1890, 304),

    # Guimarães Rosa
    ("Grande Sertão: Veredas", "Guimarães Rosa", 1956, 624),

    # Gabriel García Márquez (2 livros)
    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967, 448),
    ("O Amor nos Tempos do Cólera", "Gabriel García Márquez", 1985, 416),

    # Fiódor Dostoiévski (2 livros)
    ("Crime e Castigo", "Fiódor Dostoiévski", 1866, 592),
    ("Os Irmãos Karamázov", "Fiódor Dostoiévski", 1880, 832),

    # Liev Tolstói (2 livros)
    ("Guerra e Paz", "Liev Tolstói", 1869, 1225),
    ("Anna Karênina", "Liev Tolstói", 1877, 864),

    # George Orwell (2 livros)
    ("1984", "George Orwell", 1949, 328),
    ("A Revolução dos Bichos", "George Orwell", 1945, 152),

    # J.R.R. Tolkien (2 livros)
    ("O Hobbit", "J.R.R. Tolkien", 1937, 336),
    ("A Sociedade do Anel", "J.R.R. Tolkien", 1954, 576),

    # Outros autores
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96),
    ("Orgulho e Preconceito", "Jane Austen", 1813, 432),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 264),
    ("Fahrenheit 451", "Ray Bradbury", 1953, 256),
    ("O Apanhador no Campo de Centeio", "J.D. Salinger", 1951, 240),
]


def main():
    livros = armazenamento.carregar_livros()
    quantidade_inicial = len(livros)

    if quantidade_inicial > 0:
        print(f"⚠ Já existem {quantidade_inicial} livro(s) cadastrado(s).")
        resposta = input("Deseja adicionar os livros de teste mesmo assim? (s/n): ").strip().lower()
        if resposta != "s":
            print("Operação cancelada.")
            return

    print(f"\nCadastrando {len(LIVROS_TESTE)} livros...\n")

    for titulo, autor, ano, paginas in LIVROS_TESTE:
        livro = imperativo.adicionar_livro(livros, titulo, autor, ano, paginas)
        print(f"  ✓ [{livro['id']}] {livro['titulo']} — {livro['autor']}")

    armazenamento.salvar_livros(livros)

    print(f"\n✓ Cadastro em massa concluído!")
    print(f"  Total adicionado: {len(LIVROS_TESTE)} livro(s)")
    print(f"  Total no sistema: {len(livros)} livro(s)")


if __name__ == "__main__":
    main()
