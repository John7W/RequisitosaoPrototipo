import time

vagas = [
    {"id": 1, "setor": "A", "tipo": "comum", "status": "livre"},
    {"id": 2, "setor": "A", "tipo": "reservada", "status": "ocupada"},
    {"id": 3, "setor": "A", "tipo": "desconhecida", "status": "livre"},
    {"id": 4, "setor": "B", "tipo": "comum", "status": "ocupada"},
    {"id": 5, "setor": "B", "tipo": "reservada", "status": "livre"},
    {"id": 6, "setor": "B", "tipo": "comum", "status": "livre"},
]


def cor_tipo_vaga(tipo):
    if tipo == "comum":
        return "VERDE"
    elif tipo == "reservada":
        return "AZUL"
    else:
        return "CINZA"


def simbolo_status(status):
    if status == "livre":
        return "[LIVRE]"
    else:
        return "[OCUPADA]"


def listar_todas_vagas():
    print("\n=== TODAS AS VAGAS ===")
    for vaga in vagas:
        print(
            f"Vaga {vaga['id']} | "
            f"Setor {vaga['setor']} | "
            f"Tipo: {vaga['tipo']} ({cor_tipo_vaga(vaga['tipo'])}) | "
            f"Status: {simbolo_status(vaga['status'])}"
        )


def listar_vagas_disponiveis_por_setor():
    print("\n=== VAGAS DISPONÍVEIS POR SETOR ===")
    setores = {}

    for vaga in vagas:
        if vaga["status"] == "livre":
            setor = vaga["setor"]
            if setor not in setores:
                setores[setor] = []
            setores[setor].append(vaga)

    if not setores:
        print("Nenhuma vaga disponível no momento.")
        return

    for setor, lista_vagas in setores.items():
        print(f"\nSetor {setor}:")
        for vaga in lista_vagas:
            print(
                f"  Vaga {vaga['id']} - "
                f"Tipo: {vaga['tipo']} ({cor_tipo_vaga(vaga['tipo'])})"
            )


def atualizar_status_vaga(id_vaga, novo_status):
    for vaga in vagas:
        if vaga["id"] == id_vaga:
            vaga["status"] = novo_status
            print(f"Status da vaga {id_vaga} atualizado para {novo_status}.")
            return
    print("Vaga não encontrada.")


def simulacao_atualizacao_automatica(intervalo=5, repeticoes=3):
    print("\n=== SIMULAÇÃO DE ATUALIZAÇÃO AUTOMÁTICA ===")
    for i in range(repeticoes):
        print(f"\nAtualização {i + 1}:")
        listar_todas_vagas()
        time.sleep(intervalo)
    
def gestao_de_vagas_menus():    
    while True:
            print("\n=== Gestão de Vagas ===")
            print("1 - Listar todas as vagas")
            print("2 - Listar vagas disponíveis por setor")
            print("3 - Atualizar status de uma vaga")
            print("4 - Simular atualização automática")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                listar_todas_vagas()

            elif opcao == "2":
                listar_vagas_disponiveis_por_setor()

            elif opcao == "3":
                try:
                    id_vaga = int(input("Digite o ID da vaga: "))
                    novo_status = input("Digite o novo status (livre/ocupada): ").lower()
                    if novo_status in ["livre", "ocupada"]:
                        atualizar_status_vaga(id_vaga, novo_status)
                    else:
                        print("Status inválido.")
                except ValueError:
                    print("Digite um ID numérico válido.")

            elif opcao == "4":
                simulacao_atualizacao_automatica()

            elif opcao == "0":
                print("Voltando ao menu principal")
                return

            else:
                print("Opção inválida.")