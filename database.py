# Conexão e operações com o banco de dados (SQLite)

import sqlite3

def create_connection(db_file):

    conection= None

    try:
        conection = sqlite3.connect(db_file)
        print("Conexão estabelecida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro de conexão com o banco de dados: {e}")
    return conection

def initalize_database(conection):

    create_table_sql = """CREATE TABLE IF NOT EXISTS tasks (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        priority INTEGER,
        status TEXT,
        created_at TEXT);
        """
    try:
        curs = conection.cursor()
        curs.execute(create_table_sql)
        conection.commit()
        print("Tabela 'tasks' inicializada com sucesso")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela. {e}")

def add_task(conection, task):
    sql = """ INSERT INTO tasks(title, description, due_date, priority, status, created_at)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    curs = conection.cursor()
    curs.execute(sql, (task.title, task.description, task.due_date, task.priority, task.status, task.created_at))
    conection.commit()
    return curs.lastrowid

def get_all_tasks(conection, order_by:None):
    sql = "SELECT id, title, description, due_date, priority, status, created_at FROM tasks "
    if order_by in ["due_date", "status", "priority"]:
        sql += f"ORDER BY {order_by} ASC;"
    else:
        sql += ";"

    curs = conection.cursor()
    curs.execute(sql)
    rows = curs.fetchall()

    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "due_date": row[3],
            "priority": row[4],
            "status": row[5],
            "created_at": row[6],

        })
    return tasks

def get_task(conection, task_id):
    sql = "SELECT id, title, description, due_date, priority, status, created_at FROM tasks WHERE id = ?;"
    curs = conection.cursor()
    curs.execute(sql, (task_id,))
    row = curs.fetchone()
    if row is None:
        return  None
    return {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "due_date": row[3],
        "priority": row[4],
        "status": row[5],
        "created_at": row[6],
    }

def update_task(conection, task_id, new_title=None, new_description=None, new_due_date=None, new_priority=None, new_status=None):

    fields = []
    params = []
    if new_title is not None:
        fields.append("title = ?")
        params.append(new_title)
    if new_description is not None:
        fields.append("description = ?")
        params.append(new_description)
    if new_due_date is not None:
        fields.append("due_date = ?")
        params.append(new_due_date)
    if new_priority is not None:
        fields.append("priority = ?")
        params.append(new_priority)
    if new_status is not None:
        fields.append("status : ?")
        params.append(new_status)

    if not fields:
        return False

    params.append(task_id)
    sql = f"UPDATE tasks SET {', '.join(fields)} WHERE id = ?;"
    curs = conection.cursor()
    curs.execute(sql, tuple(params))
    conection.commit()
    return curs.rowcount > 0

def update_task_status(conection, task_id, new_status):
    sql = f"UPDATE tasks SET status = ? WHERE id = ?;"
    curs = conection.cursor()
    curs.execute(sql, (new_status, task_id))
    conection.commit()
    return curs.rowcount > 0

def delete_task(conection, task_id):
    sql = "DELETE FROM tasks WHERE id = ?;"
    curs = conection.cursor()
    curs.execute(sql, (task_id,))
    conection.commit()
    return curs.rowcount > 0



