import logging

from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ConversationHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return choice

async def timetable(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return classs


if __name__ == '__main__':
    application = ApplicationBuilder().token('6192623483:AAGWmrr-9-OkH3hfKcAmfznF0KAEUr1H99A').build()
    conversation_hand = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
           choice : [
               MessageHandler(filters.Regex('time table'), timetable),
               MessageHandler(),
               MessageHandler(),
           ],
            classs : [
                MessageHandler(filters.Regex('7'), seventh),
                MessageHandler(filters.Regex('8'), eighth),
                MessageHandler(filters.Regex('9'), nineth),
            ]
            letter : [
                MessageHandler(filters.Regex('A'), onedice),
                MessageHandler(filters.Regex('B'), twodices),
                MessageHandler(filters.Regex('K'), threedices),
                MessageHandler(filters.Regex('L'), threedices),
                MessageHandler(filters.Regex('D'), threedices),
            ]
            result : [MessageHandler( )]
        }
    )
