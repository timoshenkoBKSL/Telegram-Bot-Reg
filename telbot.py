# импортируем функцию создания объекта бота
from telebot import TeleBot
# импортируем основные настройки проекта
from settings import config
# импортируем главный класс-обработчик бота
from handlers.handler_main import HandlerMain


class TelBot:
    __version__ = config.VERSION

    def __init__(self):
        """
        Инициализация бота
        """
        # получаем токен
        self.token = config.TOKEN
        # инициализируем бот на основе зарегистрированного токена
        self.bot = TeleBot(self.token)
        # инициализируем обаботчик событий
        self.handler = HandlerMain(self.bot)

    def start(self):
        """
        Метод предназначен для старта обработчика событий
        """
        self.handler.handle()

    def run_bot(self):
        """
        Метод запуcкает основные события сервера
        """
        # обработчик событий
        self.start()
        # служит аля запуска бота (работа в режиме нон-стоп)
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()
