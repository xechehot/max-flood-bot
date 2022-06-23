import logging
import re
import random
from telegram import Update, ChatAction
from telegram.ext import Updater, CommandHandler, CallbackContext

logger = logging.getLogger(__name__)


def get_n_words():
    return random.randint(30, 60)


def get_temperature():
    return random.uniform(0.6, 0.8)


def start(update: Update, context: CallbackContext) -> None:
    """Sends explanation on how to use the bot."""
    update.message.reply_text('Привет! Напиши мне что-нибудь')


def predict(update: Update, context: CallbackContext) -> None:
    from nlp import predict
    n_words = get_n_words()
    temperature = get_temperature()
    logger.info(f'--> Predicting with text "{update.message.text}", {n_words} words with temperature {temperature}...')
    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
    predicted_text = predict(update.message.text,
                             n_words=n_words,
                             temperature=temperature,
                             only_last_word=False)
    logger.info(f'<-- {predicted_text}')
    for sm in predicted_text.split('xxmessage')[1:]:
        for m in sm.split('xxmax'):
            if m.strip() != '':
                update.message.reply_text(m)
    # update.message.reply_text(predicted_text)
