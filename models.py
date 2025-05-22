# Definição das classes de dados, como a classe Task#

class Task:
    def __init__(self, title, description, due_date, priority, status="Pendente"):
        self.title =title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Titulo: {self.title} | Status: {self.status} | Vence: {self.due_date}"
