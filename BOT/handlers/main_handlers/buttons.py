from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


inline_btn_OGE = InlineKeyboardButton('ОГЭ', callback_data='button_OGE')
inline_btn_EGE = InlineKeyboardButton('ЕГЭ', callback_data='button_EGE')
inline_kb_start_menu = InlineKeyboardMarkup().add(inline_btn_OGE).add(inline_btn_EGE)

inline_btn_Math = InlineKeyboardButton('Математика', callback_data='button_OGE_math')
inline_btn_IT = InlineKeyboardButton('Информатика', callback_data='button_OGE_IT')
inline_kb_OGE_menu = InlineKeyboardMarkup().add(inline_btn_Math).add(inline_btn_IT)