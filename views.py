

from controllers import create_task, get_all_tasks, change_task, delete_task

def exibir_menu():
    print("1. Criar Tarefa")
    print("2. Listar Tarefa")
    print("3. Editar Tarefa")
    print("4. Excluir Tarefa")
    print("5. Sair")
    return input("Escolha uma opção: ")

def select_opcao(opcao):
    if opcao == '1':
        title = input("Titulo da Tarefa: ")
        description = input("Descrição: ")
        due_date = input("Data de vencimento (YYYY-MM-DD) : ")
        priority = input("Prioridade (1-5): ")
        task = create_task(title,description,due_date,property)
        print('Tarefa Criada com sucesso!')
        print(f"{task}")
    elif opcao == '2':
        print("\n---Lista de Tarefas---")
        tasks = get_all_tasks()
        if not tasks:
            print("Nenhuma tarefa encontrada")
        else:
            # enumera apartir do numero 1 as tarefas
            for idx, t in enumerate(tasks, start=1):
                print(f"{idx}. {t}")
    elif opcao =='3':
        index = int(input("Digite o numero da tarefa a ser alterada: "))
        new_title = input("Novo titulo (em branco se não quisera alterar) ") or None
        new_description = input("Nova descrição (em branco se não quisera alterar) ") or None
        new_due_date = input("Nova data de vencimento (YYYY-MM-DD) (em branco se não quisera alterar) ") or None
        new_priority = input("Nova prioiridade (1-5) (em branco se não quisera alterar) ") or None
        new_status = input("Novo status (em branco se não quisera alterar) ") or None

        # new_title = new_title if new_title else None
        # new_description = new_description if new_description else None
        # new_due_date = new_due_date if new_due_date else None
        # new_priority = new_priority if new_priority else None
        # new_status = new_status if new_status else None

        task = change_task((index-1), new_title, new_description, new_due_date, new_priority, new_status)
    elif opcao == '4':
        index = int(input("Digite o numero da tarefa a ser eliminada: "))
        if delete_task((index-1)):
            print("tarefa eliminda com sucesso!")
        else:
            print("tarefa não encontrada!")
    elif opcao == '5':
            print("Saindo do sistema. Até logo!")
    else:
            print("Opção inválida. Por favor, tenta novamente.")