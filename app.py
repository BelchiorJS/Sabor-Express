from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List, Optional



# Modelos / Dados
# =========================

@dataclass
class Restaurante:
    """
    Representa um restaurante cadastrado no sistema.

    Attributes:
        nome: Nome do restaurante.
        categoria: Categoria/Tipo do restaurante (ex.: Italiana, Japonesa).
        ativo: Indica se o restaurante está ativo no sistema.
    """
    nome: str
    categoria: str
    ativo: bool = False


# Base inicial (exemplo)
RESTAURANTES: List[Restaurante] = [
    Restaurante(nome="Pizza Bar", categoria="Italiana", ativo=False),
    Restaurante(nome="Sushi Master", categoria="Japonesa", ativo=True),
    Restaurante(nome="Hamburgueria Gourmet", categoria="Americana", ativo=True),
]



# Utilidades
# =========================

def limpar_tela() -> None:
    """
    Limpa o console de forma portátil (Windows/Linux/macOS).
    """
    os.system("cls" if os.name == "nt" else "clear")


def normalizar_texto(texto: str) -> str:
    """
    Normaliza texto para comparações (remove espaços laterais e ignora maiúsculas/minúsculas).

    Args:
        texto: Texto de entrada.

    Returns:
        Texto normalizado.
    """
    return texto.strip().casefold()


def pausar() -> None:
    """
    Pausa o fluxo até o usuário pressionar Enter.
    """
    input("\nPressione ENTER para voltar ao menu...")



# UI
# =========================

def exibir_nome_do_app() -> None:
    """
    Exibe o nome/arte do aplicativo no console.
    """
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")


def exibir_menu() -> None:
    """
    Exibe as opções do menu principal.
    """
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Alternar Status do Restaurante")
    print("4. Sair")


def exibir_subtitulo(texto: str) -> None:
    """
    Exibe um subtítulo formatado no console.

    Args:
        texto: Texto do subtítulo.
    """
    limpar_tela()
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def opcao_invalida() -> None:
    """
    Exibe mensagem de opção inválida e pausa.
    """
    print("Opção inválida!")
    pausar()



# Regras / Funcionalidades
# =========================

def encontrar_restaurante_por_nome(nome: str, restaurantes: List[Restaurante]) -> Optional[Restaurante]:
    """
    Procura um restaurante pelo nome (comparação normalizada).

    Args:
        nome: Nome digitado pelo usuário.
        restaurantes: Lista de restaurantes cadastrados.

    Returns:
        O restaurante encontrado, ou None se não existir.
    """
    alvo = normalizar_texto(nome)
    for r in restaurantes:
        if normalizar_texto(r.nome) == alvo:
            return r
    return None


def cadastrar_restaurante(restaurantes: List[Restaurante]) -> None:
    """
    Cadastra um novo restaurante na lista.

    Regra de negócio: todo restaurante novo entra como inativo.

    Args:
        restaurantes: Lista onde o restaurante será inserido.
    """
    exibir_subtitulo("Cadastro de Restaurante")

    nome = input("Digite o nome do restaurante: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        pausar()
        return

    # Evita duplicidade simples por nome
    if encontrar_restaurante_por_nome(nome, restaurantes) is not None:
        print("Já existe um restaurante com esse nome.")
        pausar()
        return

    categoria = input(f"Digite a categoria do restaurante '{nome}': ").strip()
    if not categoria:
        print("Categoria não pode ser vazia.")
        pausar()
        return

    restaurantes.append(Restaurante(nome=nome, categoria=categoria, ativo=False))

    print(f"Restaurante '{nome}' cadastrado com sucesso! (Status: Desativado)")
    pausar()


def listar_restaurantes(restaurantes: List[Restaurante]) -> None:
    """
    Lista todos os restaurantes cadastrados.

    Args:
        restaurantes: Lista de restaurantes para exibição.
    """
    exibir_subtitulo("Lista de Restaurantes")

    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
        pausar()
        return

    print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    print("-" * 60)

    for r in restaurantes:
        status = "Ativado" if r.ativo else "Desativado"
        print(f"{r.nome.ljust(22)} | {r.categoria.ljust(20)} | {status}")

    pausar()


def alternar_status_restaurante(restaurantes: List[Restaurante]) -> None:
    """
    Alterna o status (ativo/inativo) de um restaurante existente.

    Args:
        restaurantes: Lista de restaurantes cadastrados.
    """
    exibir_subtitulo("Alterar Status do Restaurante")

    nome = input("Digite o nome do restaurante que deseja ativar/desativar: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        pausar()
        return

    restaurante = encontrar_restaurante_por_nome(nome, restaurantes)
    if restaurante is None:
        print("Restaurante não encontrado!")
        pausar()
        return

    restaurante.ativo = not restaurante.ativo
    status = "ativado" if restaurante.ativo else "desativado"
    print(f"O restaurante '{restaurante.nome}' foi {status} com sucesso!")
    pausar()


def finalizar_app() -> None:
    """
    Exibe mensagem de encerramento.
    """
    exibir_subtitulo("Finalizando o aplicativo...")



# Controle do App
# =========================

def ler_opcao_menu() -> int:
    """
    Lê a opção do menu e retorna um inteiro.

    Returns:
        A opção escolhida (int).

    Raises:
        ValueError: Se a entrada não puder ser convertida para int.
    """
    return int(input("Escolha uma opção: ").strip())


def executar_opcao(opcao: int, restaurantes: List[Restaurante]) -> bool:
    """
    Executa a ação correspondente à opção.

    Args:
        opcao: Número selecionado pelo usuário.
        restaurantes: Lista de restaurantes.

    Returns:
        True se o app deve encerrar, False caso contrário.
    """
    match opcao:
        case 1:
            cadastrar_restaurante(restaurantes)
            return False
        case 2:
            listar_restaurantes(restaurantes)
            return False
        case 3:
            alternar_status_restaurante(restaurantes)
            return False
        case 4:
            finalizar_app()
            return True
        case _:
            opcao_invalida()
            return False


def main() -> None:
    """
    Função principal do programa.

    Mantém o ciclo do menu até o usuário escolher sair.
    """
    while True:
        limpar_tela()
        exibir_nome_do_app()
        exibir_menu()

        try:
            opcao = ler_opcao_menu()
        except ValueError:
            opcao_invalida()
            continue

        sair = executar_opcao(opcao, RESTAURANTES)
        if sair:
            break


if __name__ == "__main__":
    main()
