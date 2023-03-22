from aiogram import Dispatcher, types

async def cmd_start(msg: types.Message):
    await msg.answer("Привет, я могу сделать тебе фонетический разбор слова\n"
                     "Используй команду '/fonetic' и следуй инструкциям далее.\n"
                     "Все команды в меню команд(слева от ввода сообщения).")

async def cmd_help(msg: types.Message):
    await msg.answer("Я могу сделать тебе фонетический разбор слова\n"
                     "Используй команду '/fonetic' и следуй инструкциям далее.\n"
                     "Все команды в меню команд(слева от ввода сообщения)."
                     "Если что-то не работает, что-то не так или просто есть вопросы пиши разаботчику этого бота - https://t.me/HumanSuit8")


def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_help, commands='help')