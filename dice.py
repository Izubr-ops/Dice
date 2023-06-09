import logging
from random import randint
from uuid import uuid4

from telegram import Update, ReplyKeyboardRemove, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters, \
    InlineQueryHandler

from Token import TOKEN
from testbotkeyboard import keyboard_other, keyboardok, OKkeyboard

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

dices, after, choice = range(3)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="""
                                   Hello, my name's Nikita.
                                   This's my first try of making bots on Python
                                   """)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hello. i am dice bot.I will give you a random number from 1 to 6.",
                                   reply_markup=OKkeyboard)

    return choice


async def choicef(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Choose how many dices you want to throw",
                                   reply_markup=keyboard_other)

    return dices


async def onedice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = randint(1, 6)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"🎉🎉🎉And your result is ..... {result}🎉🎉🎉"
                                                                          f"Do you want to retry",
                                   reply_markup=keyboardok)

    return after


async def twodices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = randint(2, 12)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"🎉🎉🎉And your result is ..... {result}🎉🎉🎉"
                                                                          f"Do you want to retry",
                                   reply_markup=keyboardok)

    return after


async def threedices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = randint(3, 18)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"🎉🎉🎉And your result is ..... {result}🎉🎉🎉"
                                        f"Do you want to retry",
                                   reply_markup=keyboardok)

    return after


async def finish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ok, May be later", reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="OK, goodbye")

    return ConversationHandler.END

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query
    if query == "":
        return

    elif len(query) == 1 and query.isdigit()\
        and query in ["1", "2", "3"]:

        results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="🎲",
            input_message_content=InputTextMessageContent(f"You get {str(randint(1, 6))}🎲")
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="🎲🎲",
            input_message_content=InputTextMessageContent(f"You get {str(randint(2, 12))}🎲🎲"),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="🎲🎲🎲",
            input_message_content=InputTextMessageContent(f"You get {str(randint(3, 18))}🎲🎲🎲"),
        )
    ]

        await update.inline_query.answer(results)




if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    info = CommandHandler("info", info)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            choice: [MessageHandler(filters.Regex('Ok'), choicef)],
            dices: [
                MessageHandler(filters.Regex('1🎲'), onedice),
                MessageHandler(filters.Regex('2🎲'), twodices),
                MessageHandler(filters.Regex('3🎲'), threedices),
            ],
            after: [
                MessageHandler(filters.Regex('Yes'), choicef),
                MessageHandler(filters.Regex('No'), finish)
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    application.add_handlers([conv_handler, info])
    application.add_handler(InlineQueryHandler(inline_query))

    application.run_polling()
