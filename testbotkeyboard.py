from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(
    [["Yes", "idk", "No"]],
    resize_keyboard=True
)

keyboard_other = ReplyKeyboardMarkup(
    [["1🎲", "2🎲", "3🎲"]],
    resize_keyboard=True, one_time_keyboard=True
)


bottons = [[
                  InlineKeyboardButton("🎲", callback_data="1"),
                  InlineKeyboardButton("🎲🎲", callback_data="2"),
                  InlineKeyboardButton("🎲🎲🎲", callback_data="3")]
    ]
inline_keyboard = InlineKeyboardMarkup(bottons)

keyboardok = ReplyKeyboardMarkup(
    [["Yes", "No"]],
    resize_keyboard=True, one_time_keyboard=True
)


OKkeyboard = ReplyKeyboardMarkup(
    [["Ok"]],
    resize_keyboard=True, one_time_keyboard=True
)
