from aiogram import Dispatcher, types, Bot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from BOT.handlers.main_handlers.buttons import inline_kb_start_menu
from BOT.main import config

bot = Bot(token=config.TOKEN_test)

async def cmd_start(msg: types.Message):        # Хандлер для команды "/start" и приветствия
    await msg.answer("Привет, давай подготовимся к ОГЭ и ЕГЭ.\n"
                     "К какому экзамену будем готовится?\n"
                     "Все подробности и нстркуция пользования после команды - /help.",
                     reply_markup=inline_kb_start_menu)

async def cmd_help(msg: types.Message):         # Хандлер для команды "/help" и помощи
    await msg.answer("Я могу подготовить тебя к ОГЭ и ЕГЭ.\n"
                     "Все команды в меню команд(слева от ввода сообщения)."
                     "Если что-то не работает, что-то не так или просто есть вопросы пиши разаботчикам этого бота:\n"
                     "https://t.me/HumanSuit8\n"
                     "https://t.me/Dan4ksapr123")

async def cmd_button_OGE(callback_query: types.CallbackQuery):
    await bot.send_message(text='ОГЭ', chat_id=callback_query.message.chat.id)

def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_help, commands='help')
    dp.register_callback_query_handler(cmd_button_OGE, lambda c: c.data == 'button_OGE')