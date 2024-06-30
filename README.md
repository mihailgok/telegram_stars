# Оплата в Телеграм ботах с помощью Telegram Stars

___________

Бот простейший и написан на aiogram 3.0.

```python
pip3 install aiogram
```

____________

Для создания товара используйте стандартную функцию 
```python
types.LabeledPrice(label='Один товар', amount=1)
```

Затем создайте платёж - в качестве валюты укажите "XTR", а в токен передайте пустую строку:

```python
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
```

_____________

Подробная информация в [статье](https://blog.mihailgok.ru/?p=402)