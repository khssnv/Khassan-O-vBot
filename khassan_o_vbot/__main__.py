import logging
import multiprocessing

from aiogram import Bot, Dispatcher, executor, types
from telethon import TelegramClient, events

from khassan_o_vbot.utils.settings import settings


logging.basicConfig(level=logging.INFO)


def telethon_main():
    logging.info('Starting telegram client')

    client = TelegramClient(settings.tgclient_creds.session, settings.tgclient_creds.api_id,
                            settings.tgclient_creds.api_hash, proxy=None)

    @client.on(events.NewMessage(chats=settings.aggregated_chats, incoming=True))
    async def handler(event):
        logging.info(event)
        await client.forward_messages(settings.aggregation_channel, event.message)

    with client:
        client.run_until_disconnected()


def aiogram_main():
    logging.info('Starting telegram bot')

    bot = Bot(token=settings.tgbot_creds.token)
    dp = Dispatcher(bot)

    async def on_startup(dispatcher: Dispatcher):
        await bot.send_message(settings.me, 'Started.', disable_notification=True)

    async def on_shutdown(dispatcher: Dispatcher):
        await bot.send_message(settings.me, 'Terminating...', disable_notification=True)

    @dp.message_handler(commands=['me'])
    async def me_cmd(message: types.Message):
        await message.answer(message)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)


if __name__ == '__main__':
    telethon_proc = multiprocessing.Process(target=telethon_main)
    aiogram_proc = multiprocessing.Process(target=aiogram_main)
    telethon_proc.start()
    aiogram_proc.start()
    telethon_proc.join()
    aiogram_proc.join()
