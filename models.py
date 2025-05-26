# Definição das classes de dados, como a classe Task#
from datetime import date
class Task:
    def __init__(self, title, description, due_date, priority, status="Pendente", created_at=None):
        self.title =title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.created_at = date.today().strftime("%Y-%m-%d")

    def __str__(self):
        return f"Titulo: {self.title} | Status: {self.status} | Vence: {self.due_date} | Craida em: {self.created_at}"
