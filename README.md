Призначення та коротка характеристика програми
----------------------------------------------
Призначенням нашої програми є встановити наскільки сильно корелюється успіх кінематографу
та в залежності від яких економічних чинників.
Програма видає графіки , які базуються на економічних та кінематографічних даних,
щоб зробити висновок про взаємозв’язок випуску фільмів та економічного становища країни.

Вхідні та вихідні дані програми
----------------------------------------------
Вхідними даними для нашої програми є ввід користувача, який вказує на те, який графік
буде виводитись.
Вихідними даними є наступні графіки (який графік буде виводити програма залежить від вибору користувача):
1) Акції компаній - ВВП США
2) Акції компаній - Прибуток компаній
3) Прибуток компаній - ВВП США
Графіки є інтерактивними - користувач може вибрати для якої саме компанії він хоче побачити графік.

Структура програми з коротким описом модулів, функцій,класів та методів.
----------------------------------------------
Програма містить головний модуль main.py, який відповідає за побудову графіків
та містить наступні функції:
build_stock_gdp() - функція відповідає за побудову графіка "Акції - ВВП"
build_stock_boxoffice() - функція відповідає за побудову графіка "Акції - Прибуток"
build_gdp_boxoffice() - функція відповідає за побудову графіка "ВВП - Прибуток"

Модуль atd.py - містить абстрактну структуру даних:
MoviesBase - клас - абстрактний тип даних

Модуль data_type.py - містить абстрактний тип даних:
MoviesFull - абстрактний тип даних

Json - файл database_profit.json, який містить словник, в якому міститься інформація
про касові збори та акції компаній. Ключами є рік (з 1947 по 2018) а значеннями -
списки. Цей список містить два словники, в обох ключами є компанії. У першому
значеннями є списки касових зборів фільмів, що були зняті в той рік, а в другому -
ціни на акції компаній у цей рік.

Json - файл gdps.json, який містить словник, ключі якого це роки, а значення -
ВВП США на цей рік.

Модуль example.py - містить запуск програми та тестову перевірку:
print_beginning() - виводить вступ та короткий опис графіків для вибору.
choose_func() - функція, яка відповідає за ітеракцію з користувачем. Зчитує ввід
та в залежності від вибору цифри виводить відповідний графік.
main() - головна тестова функція, яка запускає вище перелічені.

Модуль test_data_type.py - містить модульний тест структур даних.

Json - файл sorted_dict.json, який містить словник в якому містяться id фільмів на усі роки 
усіх, вибраних нами, компаній.


Коротка інструкція по користуванню програмою
----------------------------------------------
Для користувача:
В терміналі виводиться запит - питання із запропонованими варіантами, який графік
хоче побачити користувач.
Користувач вибирає варіант і отримує графіки, які відкриваються в новому вікні.


Опис тестових прикладів для перевірки працездатності програми.
----------------------------------------------
Файл з тестовою перевіркою програми - test.py
Даний файл містить 2 функції, які відповідають за інтеракцію з користувачем та запуск функцій, які будують графіки.
main() - головна тестова функція, яка запускає функції, що відповідають за побудову графіків
та інтеракцію.
