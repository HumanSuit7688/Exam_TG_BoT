from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


inline_btn_OGE = InlineKeyboardButton('ОГЭ', callback_data='button_OGE')
inline_btn_EGE = InlineKeyboardButton('ЕГЭ', callback_data='button_EGE')
inline_kb_start_menu = InlineKeyboardMarkup().add(inline_btn_OGE).add(inline_btn_EGE)


inline_btn_OGE_Math = InlineKeyboardButton('Математика', callback_data='button_OGE_math')
inline_btn_OGE_IT = InlineKeyboardButton('Информатика', callback_data='button_OGE_IT')
inline_btn_OGE_Rus = InlineKeyboardButton('Русский язык', callback_data='button_OGE_Rus')
inline_btn_OGE_Phys = InlineKeyboardButton('Физика', callback_data='button_OGE_Phys')
inline_btn_OGE_Chem = InlineKeyboardButton('Химия', callback_data='button_OGE_Chem')
inline_btn_OGE_Bio = InlineKeyboardButton('Биология', callback_data='button_OGE_Bio')
inline_btn_OGE_Next = InlineKeyboardButton('Дальше', callback_data='button_OGE_Next')
inline_kb_OGE_menu = InlineKeyboardMarkup().row(inline_btn_OGE_Math).row(inline_btn_OGE_IT).row(inline_btn_OGE_Rus).row(inline_btn_OGE_Phys).row(inline_btn_OGE_Chem).row(inline_btn_OGE_Next)



inline_btn_OGE_math_Vars = InlineKeyboardButton('Варианты', callback_data='button_OGE_math_Vars')
inline_btn_OGE_math_Exers = InlineKeyboardButton('Задачи', callback_data='button_OGE_math_Exers')
inline_kb_OGE_math_menu = InlineKeyboardMarkup().add(inline_btn_OGE_math_Vars).add(inline_btn_OGE_math_Exers)


inline_kb_OGE_Next_menu = InlineKeyboardMarkup().row(inline_btn_OGE_Bio)
