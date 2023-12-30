# Пояснения к преокту:
## Использование:
* 151.248.116.252
* Данные от админки:
    - admin
    - admin
## Версии приложения (Stripe Session и Stripe Payment Intent):
* последний коммит (9082bdb) - версия с использованием Stripe Payment Intent.
* предпоследний коммит (f17a9b8) - версия на
## Дополнительно:
* Файл env был добавлен в git для наглядности использования - в настоящих проектах так делать запрещено! 
* Перевод в доллары сделан на основе внешнего апи
## URLS:
* Товар можно посмотреть по url: /item/<id>
* Отдельно заказ можно оплатить по url: /pay-order/<id>
    - Если все товары в одной валюте - оплата будет в той же валюте
    - Если какие-то товары в другой валюте, оплата будет в долларах, конвертируя по курсу с внешнего API
    - Такое поведение было добавлено согласно ответу рекрутера с hh.ru :) 
