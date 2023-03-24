from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_OGE_math_var1 = InlineKeyboardButton('Вариант 1', callback_data='button_OGE_Var1')
inline_kb_OGE_math_Vars = InlineKeyboardMarkup().add(inline_btn_OGE_math_var1)