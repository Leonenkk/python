import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id, secs_left, bot):
    seconds = parse(secs_left)
    message_id = bot.send_message(chat_id, "Запускаю таймер")
    bot.create_countdown(seconds, notify_progress, message_id=message_id, chat_id=chat_id, total_time=seconds)
    bot.create_timer(seconds, choose, author_id=chat_id, text=secs_left)


def notify_progress(secs_left, chat_id, message_id, total_time, bot):
    update_message = f"{render_progressbar(total_time, total_time - secs_left)}\nОсталось {secs_left} секунд"
    bot.update_message(chat_id, message_id, update_message)


def choose(author_id, text, bot):
    text = "Время вышло!!"
    bot.send_message(author_id, text)


def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(reply)
    bot.run_bot()


if __name__ == '__main__':
    main()
