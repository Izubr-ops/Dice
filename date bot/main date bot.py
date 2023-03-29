import logging
from datetime import datetime

import pytz as pytz
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler, filters

from Token import TOKEN
from date_keyboard import cities


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

country = 1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hello, i can show you current time of some cities",
                                   reply_markup=cities)

    return country


async def ny(update: Update, context: ContextTypes.DEFAULT_TYPE):
    timeZ_Ny = pytz.timezone('America/New_York')
    dt_Ny = datetime.now(timeZ_Ny)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"It's {dt_Ny.strftime('%Y-%m-%d %H:%M:%S')}.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


async def london(update: Update, context: ContextTypes.DEFAULT_TYPE):
    timeZ_Ln = pytz.timezone('Europe/London')
    dt_Ln = datetime.now(timeZ_Ln)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"It's {dt_Ln.strftime('%Y-%m-%d %H:%M:%S')}.", reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


async def moscow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    timeZ_Mos = pytz.timezone('Europe/Moscow')
    dt_Mos = datetime.now(timeZ_Mos)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=f"It's {dt_Mos.strftime('%Y-%m-%d %H:%M:%S')}.", reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


async def tokyo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    timeZ_Tok = pytz.timezone('Asia/Tokyo')
    dt_Tok = datetime.now(timeZ_Tok)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text=f"It's {dt_Tok.strftime('%Y-%m-%d %H:%M:%S')}.", reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                                   text="Ok, see you later", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            country : [
                MessageHandler(filters.Regex('NY'), ny),
                MessageHandler(filters.Regex('London'), london),
                MessageHandler(filters.Regex('Moscow'), moscow),
                MessageHandler(filters.Regex('Tokyo'), tokyo)
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    application.add_handlers([conv_handler])

    application.run_polling()