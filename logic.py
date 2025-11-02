from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text

    def generate_keyboard(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)

        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(option, callback_data='correct'))
            else:
                markup.add(InlineKeyboardButton(option, callback_data='wrong'))

        return markup

quiz_questions = [
    Question("Какой язык мы используем для этого бота?", 0, "Python", "C++", "Java"),
    Question("Какая библиотека используется для телеграм-бота?", 1, "requests", "pyTelegramBotAPI", "Django"),
    Question("Какая функция отправляет уведомление о правильном/неправильном ответе?", 0, "answer_callback_query", "send_message", "edit_message_text")
]
