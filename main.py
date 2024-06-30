from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.types import Message, PreCheckoutQuery
from aiogram import Dispatcher
import asyncio

import logging

from aiogram.types.message import ContentType
from aiogram.utils.callback_answer import CallbackAnswer, CallbackQuery
from typing import Optional
from aiogram.filters.callback_data import CallbackData
from aiogram.types.message import ContentType
from aiogram.methods.create_invoice_link import CreateInvoiceLink
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

# Объект бота
bot = Bot(token="<ВАШ_ТОКЕН>")
# Диспетчер для бота
dp = Dispatcher()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

router = Router()


@dp.message(Command('start'))
async def create_invoice(msg: Message):
    one = types.LabeledPrice(label='Один товар', amount=1)

    await bot.send_invoice(
        msg.chat.id,
        title="Заголовок покупки ",
        description="Описание покупки ",
        provider_token="",
        currency="XTR",
        photo_url="<ссылка_на_картинку>",
        photo_width=3600,
        photo_height=2338,
        photo_size=262000,
        is_flexible=False,
        prices=[one],
        start_parameter="one-more",
        payload="one-more"
    )


@dp.pre_checkout_query()
async def checkout_handler(checkout_query: PreCheckoutQuery):
    await checkout_query.answer(ok=True)


@dp.message(F.successful_payment)
async def star_payment(msg: Message, bot: Bot):
    # await bot.refund_star_payment(  # Тестирование возврата средств
    #     msg.chat.id,
    #     msg.successful_payment.telegram_payment_charge_id,
    # )

    await msg.answer(f"Id транзакции: {msg.successful_payment.telegram_payment_charge_id}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запуск бота
    asyncio.run(main(), debug=True)
