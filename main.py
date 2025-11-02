import telebot
from logic import quiz_questions

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

user_responses = {}

def send_question(chat_id):
    question_index = user_responses[chat_id]
    question = quiz_questions[question_index]
    bot.send_message(chat_id, question.text, reply_markup=question.generate_keyboard())

@bot.message_handler(commands=['start'])
def start_quiz(message):
    chat_id = message.chat.id
    user_responses[chat_id] = 0
    send_question(chat_id)

@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    chat_id = call.message.chat.id
    if call.data == 'correct':
        bot.answer_callback_query(call.id, "Верно! ✅")
    else:
        bot.answer_callback_query(call.id, "Неверно ❌")

    user_responses[chat_id] += 1

    if user_responses[chat_id] >= len(quiz_questions):
        bot.send_message(chat_id, "Вы ответили на все вопросы! 🎉")
    else:
        send_question(chat_id)

bot.infinity_polling()
