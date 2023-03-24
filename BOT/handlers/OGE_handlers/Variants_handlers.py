from aiogram import Dispatcher, types, Bot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from BOT.main import config
from OGE.Math.Variants.Parsing import parsing_var1
from BOT.handlers.OGE_handlers.buttons import inline_kb_OGE_math_Vars
bot = Bot(token=config.TOKEN_test)

async def OGE_math_Vars(callback_query: types.CallbackQuery):
    await bot.send_message(text=f'Тренировочные варианты ОГЭ по математике', chat_id=callback_query.message.chat.id, reply_markup=inline_kb_OGE_math_Vars)

async def OGE_math_Var1(callback_query: types.CallbackQuery):
    tasks = parsing_var1()
    await bot.send_message(text=f'Первый тренировочный вариант ОГЭ по математике\n\n'
                           f'{tasks[0]}', chat_id=callback_query.message.chat.id)

def register_handlers_OGE_Vars(dp: Dispatcher):
    dp.register_callback_query_handler(OGE_math_Vars, lambda c: c.data == 'button_OGE_math_Vars')
    dp.register_callback_query_handler(OGE_math_Var1, lambda c: c.data == 'button_OGE_math_Var1')
