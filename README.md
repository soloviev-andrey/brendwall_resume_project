# Тестовое задание: API для продуктов и работа с фронтендом

## Описание
Необходимо создать небольшое Django-приложение, которое будет состоять из двух частей:
1. **API для работы с продуктами** (создание и получение списка).
2. **Страница на HTML с использованием JavaScript** для отправки данных на API и отображения продуктов.

## Требования

### 1. API (Django)
- Создайте модель продукта с полями:
  - **название** (строка)
  - **описание** (текст)
  - **цена** (десятичное число)

- Реализуйте API с двумя конечными точками:
  - **POST-запрос** для создания продукта (принимает JSON с данными: название, описание, цена).
  - **GET-запрос** для получения списка всех продуктов в формате JSON.

- При создании продукта должны выполняться простые проверки:
  - Цена должна быть положительным числом.
  - Название не должно быть пустым.

### 2. Фронтенд (HTML + JavaScript)
- Создайте простую HTML-страницу с формой для добавления нового продукта (поля: название, описание, цена) и кнопкой "Отправить".

- Реализуйте логику с помощью JavaScript, которая отправляет данные формы на API с использованием AJAX (Fetch API).

- После успешного добавления продукта обновите список продуктов на странице, сделав GET-запрос к API для получения всех продуктов и отобразив их в виде таблицы.

