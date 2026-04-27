from telegram.ext import ApplicationBuilder , CommandHandler , ContextTypes
from telegram import Update

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Controllers.todoController import TodoController
from dotenv import load_dotenv
import os

load_dotenv() 

TOKEN = os.getenv("BOT_TOKEN")

application = ApplicationBuilder().token(TOKEN).build()

application.add_handler( CommandHandler("add" , TodoController.add_todo ))
application.add_handler( CommandHandler("list" , TodoController.list_todos))

application.run_polling(allowed_updates=Update.ALL_TYPES)
 