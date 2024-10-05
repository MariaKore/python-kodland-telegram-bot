import telebot
from config import API_TOKEN
from random import choice

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['quote'])
def quote_handler(message):
    quote = choice([
        "The only way out is through. — Robert Frost",
        "It always seems impossible until it’s done. — Nelson Mandela",
        "Faith is taking the first step even when you don't see the whole staircase. — Martin Luther King Jr.",
        "Even if I knew that tomorrow the world would go to pieces, I would still plant my apple tree. — Martin Luther",
        "Focus on yourself and your growth. You are your biggest competition. — Wonyoung",
        "Just eat peanut! Hospital very close, don't worry. — Uncle Roger"
    ])
    bot.reply_to(message, quote)

if __name__ == "__main__":
    bot.polling()
