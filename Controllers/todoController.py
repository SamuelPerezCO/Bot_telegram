from telegram import Update
from telegram.ext import ContextTypes

from Models.todo import Todo
from Models.todoList import todo_list
class TodoController:

    @staticmethod
    async def add_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.split()[0]
        title = "".join(update.message.text.split(command)[1])
        todo_list.append(Todo(title))
        await update.message.reply_text("Nota agregada!")

    @staticmethod
    async def list_todos(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if ( len(todo_list) == 0):
            await update.message.reply_text("No hay tareas todavia")
            return
        answer = ""
        for i , todo in enumerate(todo_list):
            answer = answer + f"{i + 1} - { 'Melo' if todo.is_completed else 'Melont'} {todo.title}\n"
        await update.message.reply_text(answer)