from datetime import datetime
import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from testbotkeyboard import keyboard

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.full_name}!",
        reply_markup=ForceReply(selective=True),
    )
    """await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")"""

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Its {current_time}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def helloing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    user = update.effective_user
    current_time = now.strftime("%H")
    if int(current_time) < 12 and int(current_time) > 6:
        await  context.bot.send_message(chat_id=update.effective_chat.id, text=rf"Good morning, {user.first_name}")
    elif int(current_time) > 17 and int(current_time) < 23:
        await  context.bot.send_message(chat_id=update.effective_chat.id, text=rf"Good evening, {user.first_name}")
    elif int(current_time) > 12 and int(current_time) < 17:
        await  context.bot.send_message(chat_id=update.effective_chat.id, text=rf"Good afternoon, {user.first_name}")
    else:
        await  context.bot.send_message(chat_id=update.effective_chat.id, text=rf"Good night, {user.first_name}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Am I right", reply_markup=keyboard)

async def yesing (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="yeah, i am always right")

async def noing (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Something is wrong here")

async def idking (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Yeah, you are stupid human")

if __name__ == '__main__':
    application = ApplicationBuilder().token('6192623483:AAGWmrr-9-OkH3hfKcAmfznF0KAEUr1H99A').build()
    start_handler = CommandHandler('start', start)
    question_handler = CommandHandler('date', question)
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    helloing_handler = MessageHandler(filters.Regex('Hello')  | filters.Regex('Good morning') , helloing)
    yesing_handler = MessageHandler(filters.Regex('Yes'),yesing)
    noing_handler = MessageHandler(filters.Regex('No'),noing)
    adking_handler = MessageHandler(filters.Regex('idk'), idking)

    application.add_handlers([start_handler, question_handler, helloing_handler, yesing_handler, noing_handler, adking_handler, echo_handler])


    application.run_polling()