from aiogram import Dispatcher, types

async def cmd_start(msg: types.Message):        # Хандлер для команды "/help" и помощи
    await msg.answer("Привет, давай подготовимся к ОГЭ и ЕГЭ.\n"
                     "Все команды в меню команд(слева от ввода сообщения).")

async def cmd_help(msg: types.Message):         # Хандлер для команды "/start" и приветствия
    await msg.answer("Я могу подготовить тебя к ОГЭ и ЕГЭ.\n"
                     "Все команды в меню команд(слева от ввода сообщения)."
                     "Если что-то не работает, что-то не так или просто есть вопросы пиши разаботчикам этого бота:\n "
                     "https://t.me/HumanSuit8 \n"
                     "https://t.me/Dan4ksapr123")


def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_help, commands='help')