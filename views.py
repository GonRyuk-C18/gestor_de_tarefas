

from controllers import create_task, get_all_tasks, change_task, delete_task, change_task_db, update_task,update_task_status_db,get_all_tasks_db,get_task_db, delete_task_db

def exibir_menu():
    print("\n --- Gestor de Tarefas ---")
    print("1. Criar Tarefa")
    print("2. Listar Tarefa")
    print("3. Detalhe Tarefa")
    print("4. Alterar Status Tarefa")
    print("5. Editar Tarefa")
    print("6. Excluir Tarefa")
    print("0. Sair")
    return input("Escolha uma opção: ")

#def select_opcao(opcao):
def select_opcao(conection, opcao):
    if opcao == '1':
        title = input("Titulo da Tarefa: ")
        description = input("Descrição: ")
        due_date = input("Data de vencimento (YYYY-MM-DD) : ")
        priority = input("Prioridade (1-5): ")
        #task = create_task(title,description,due_date,priority)
        task = create_task(conection,title,description,due_date,priority)
        print('Tarefa Criada com sucesso!')
        #print(f"{task}")
        print(task)
    elif opcao == '2':
        print("\n---Lista de Tarefas---")
        #tasks = get_all_tasks()
        tasks = get_all_tasks_db(conection)
        if not tasks:
            print("Nenhuma tarefa encontrada")
        else:
            # enumera apartir do numero 1 as tarefas
            #for idx, t in enumerate(tasks, start=1):
                #print(f"{idx}. {t}")
            for task in tasks:
                print(f"ID {task['id']} | Titulo: {task['title']} | Status: {task['status']} | Vence: {task['due_date']}")
    elif opcao == '3':
        print("\n---Detalhe Tarefa---")
        task_id = int(input("\n Digite o id da tarefa: "))
        task = get_task_db(conection,task_id)
        if task is None:
            print("Tarefa não encontrada! Valide se id correto!")
        else:
            print(f"ID: {task['id']} | Titulo: {task['title']} | Status: {task['status']} | Descrição: {task['description']} | Vence: {task['due_date']}")

    elif opcao =='4':
        print("\n---Update Task Status---")
        task_id = int(input("\n Digite o numero da tarefa:"))
        print("\n--- Estados: ---")
        print("1. Pendente")
        print("2. In Progress")
        print("3. Done")
        print("4. Canceled")
        i = int(input(" alterar para: "))
        if i <0 or i >= 4:
            print("Estado inválido!")
        else:
            if i == 1:
                new_status = 'Pedente'
            elif i == 2:
                new_status = 'In Progress'
            elif i == 3:
                new_status = 'Done'
            else:
                new_status = 'Canceled'
            if update_task_status_db(conection,task_id,new_status) is not None:
                print("Status atualizado com Sucesso!")
            else:
                print("Id invalido! Validade se Id correto!")



    elif opcao =='5':
        print("\n---Update Task---")
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

        #task = change_task((index-1), new_title, new_description, new_due_date, new_priority, new_status)
        updated= change_task_db(conection,index, new_title, new_description, new_due_date, new_priority, new_status)
        if updated:
            print("Tarefa atualizada com sucesso!")
        else:
            print("Nenhuma tarefa atualizada, verifique se o Id está correto!")
    elif opcao == '6':
        print("\n---Delete Task---")
        index = int(input("Digite o numero da tarefa a ser eliminada: "))
        #if delete_task((index-1)):
        if delete_task_db(conection, index):
            print("tarefa eliminda com sucesso!")
        else:
            print("tarefa não encontrada!")
    elif opcao == '0':
            print("Saindo do sistema. Até logo!")
    else:
            print("Opção inválida. Por favor, tenta novamente.")