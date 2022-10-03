# импортируем специальные типы телеграм бота для создания элементов интерфейса
from telebot. types import KeyboardButton
# импортируем настройки и утилиты
from settings import config
# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


class Keyboards:

    # инициализация разметки

    def __init__(self):
        self.markup = None
        # инициализируем менеджер для работы с БД
        Self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """
        Создаём и возвращаем кнопку по входным пааметрам
        """

        return KeyboardButton(config.KEYBOARD[name])