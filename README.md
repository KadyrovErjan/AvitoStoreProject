<div align="center">

# 🛍️ AvitoStore

### Платформа объявлений и онлайн-магазин на Django

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)]()

</div>

---

## 📖 О проекте

**AvitoStore** — веб-приложение в стиле популярных досок объявлений (Avito), реализованное на фреймворке Django. Проект позволяет пользователям размещать объявления о продаже товаров, просматривать каталог и управлять своим профилем.

---

## ✨ Возможности

- 📦 **Каталог товаров** — просмотр всех доступных объявлений
- 👤 **Аккаунты пользователей** — регистрация, вход, личный кабинет
- 📝 **Создание объявлений** — публикация товаров с описанием и фото
- 🔍 **Поиск и фильтрация** — поиск товаров по категориям и параметрам
- 🛒 **Управление объявлениями** — редактирование и удаление своих публикаций
- 🔒 **Безопасность** — защита Django CSRF, аутентификация

---

## 🗂️ Структура проекта

```
AvitoStoreProject/
│
├── mysite/                  # Основное Django-приложение
│   ├── mysite/              # Конфигурация проекта
│   │   ├── settings.py      # Настройки приложения
│   │   ├── urls.py          # Главный роутер URL
│   │   └── wsgi.py          # WSGI-точка входа
│   │
│   ├── manage.py            # Утилита управления Django
│   └── ...                  # Приложения проекта
│
└── README.md
```

---

## 🚀 Быстрый старт

### Требования

- Python **3.10+**
- pip

### Установка

**1. Клонируй репозиторий**

```bash
git clone https://github.com/KadyrovErjan/AvitoStoreProject.git
cd AvitoStoreProject
```

**2. Создай виртуальное окружение**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Установи зависимости**

```bash
pip install -r requirements.txt
```

**4. Настрой базу данных**

```bash
cd mysite
python manage.py migrate
```

**5. Создай суперпользователя** *(опционально)*

```bash
python manage.py createsuperuser
```

**6. Запусти сервер**

```bash
python manage.py runserver
```

Открой браузер и перейди по адресу: **http://127.0.0.1:8000/**

---

## 🛠️ Технологии

| Технология | Описание |
|---|---|
| **Python** | Основной язык разработки |
| **Django** | Web-фреймворк |
| **SQLite** | База данных (по умолчанию) |
| **Django ORM** | Взаимодействие с БД |
| **HTML / CSS** | Шаблонизация и стили |

---

## 🔧 Конфигурация

Основные настройки находятся в `mysite/mysite/settings.py`.

Для production-окружения рекомендуется:

```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']

# Использовать переменные окружения для SECRET_KEY
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
```

---

## 🤝 Вклад в проект

Вклад приветствуется! Вот как можно помочь:

1. Сделай **Fork** репозитория
2. Создай ветку для фичи: `git checkout -b feature/новая-фича`
3. Зафиксируй изменения: `git commit -m 'Добавлена новая фича'`
4. Отправь в ветку: `git push origin feature/новая-фича`
5. Открой **Pull Request**

---

## 📄 Лицензия

Этот проект распространяется под лицензией **MIT**. Подробнее в файле [LICENSE](LICENSE).

---

<div align="center">

Сделано с ❤️ by [KadyrovErjan](https://github.com/KadyrovErjan)

</div>