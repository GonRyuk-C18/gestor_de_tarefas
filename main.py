from views import exibir_menu, select_opcao
from database import create_connection, initalize_database

def main():
    db_file = "gestor_tarefas.db"
    conection = create_connection(db_file)
    if conection is None:
        print("Erro ao conectar o banco de dados!")
        return
    initalize_database(conection)


    opcao = ""
    while opcao != '5':
        opcao= exibir_menu()
        select_opcao(opcao, conection)
        # select_opcao(opcao)
        print("")

if __name__ == '__main__':
    main()
