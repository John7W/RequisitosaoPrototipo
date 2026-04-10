import gestao_vagas
import main

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Login de usuários")
        print("2 - Gestão de Vagas")
        print("3 - ")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            main.main()

        elif opcao == "2":
            gestao_vagas.gestao_de_vagas_menus()

        elif opcao == "3":
            continue

        elif opcao == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")

menu()