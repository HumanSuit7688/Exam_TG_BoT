# Основной файл, который будет брать инфу из всех осталльных файлов, запускаться и работать
import config
import asyncio
from aiogram import Bot, Dispatcher, types
from BOT.handlers.main_handlers.main_handlers import register_handlers_main
from BOT.handlers.OGE_handlers.Variants_handlers import register_handlers_OGE_Vars

bot = Bot(token=config.TOKEN_test)
dp = Dispatcher(bot)

async def main():
    register_handlers_OGE_Vars(dp)
    register_handlers_main(dp)
    await dp.skip_updates()
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())