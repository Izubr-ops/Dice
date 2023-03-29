from telegram import ReplyKeyboardMarkup

cities = ReplyKeyboardMarkup(
    [['NY', 'Moscow'],
     ['Tokyo', 'London']],
    resize_keyboard=True, one_time_keyboard=True
)
