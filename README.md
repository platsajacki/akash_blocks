# Получение данных о транзакциях из блока Akash

Author: Menyukhov Vyacheslav | email: menyukhov@bk.ru

## О проекте

Эта функция позволяет получить информацию о транзакциях из указанного блока на сети Akash.

## Использование

Чтобы использовать программу на локальной машине, выполните следующие шаги:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/platsajacki/akash_blocks.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd akash_blocks
    ```

3. Создайте виртуальное окружение:
    ```bash
    python -m venv venv
    ```

4. Активируйте виртуальное окружение:
    - для Windows:
    ```bash
    venv\Scripts\activate
    ```

    - для macOS и Linux:
    ```bash
    source venv/bin/activate
    ```

5. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Пример использования:

    ```python
    # Замените block_height на номер интересующего вас блока
    block_height = 12345
    result = get_akash_block_transactions(block_height)
    print(result)
    ```

## Возвращаемые значения

Функция может вернуть следующие типы данных:

- Если успешно, список декодированных транзакций в формате bytes.
- В случае ошибки, строка с сообщением об ошибке или уведомлением о отсутствии транзакций.
