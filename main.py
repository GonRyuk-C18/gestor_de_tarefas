from views import exibir_menu, select_opcao

def main():
    opcao = ""
    while opcao != '5':
        opcao= exibir_menu()
        select_opcao(opcao)
        print("")

if __name__ == '__main__':
    main()
