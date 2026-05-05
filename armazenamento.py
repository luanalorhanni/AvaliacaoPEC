"""Persistência dos livros em arquivo JSON."""

import json
import os

ARQUIVO_DADOS = "livros.json"


def carregar_livros():
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_livros(livros):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)
