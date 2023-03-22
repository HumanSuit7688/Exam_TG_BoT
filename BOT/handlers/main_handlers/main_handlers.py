from aiogram import Dispatcher, types

async def cmd_start(msg: types.Message):        # Хандлер для команды "/help" и помощи
    await msg.answer("")

async def cmd_help(msg: types.Message):         # Хандлер для команды "/start" и приветствия
    await msg.answer("")


def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_help, commands='help')