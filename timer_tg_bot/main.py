import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID')
BOT = ptbot.Bot(TG_TOKEN)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id, secs_left):
    seconds = parse(secs_left)
    message_id = BOT.send_message(chat_id, "Запускаю таймер")
    BOT.create_countdown(seconds, notify_progress, message_id=message_id, chat_id=chat_id, total_time=seconds)
    BOT.create_timer(seconds, choose, author_id=chat_id, text=secs_left)


def notify_progress(secs_left, chat_id, message_id, total_time):
    update_message = f"{render_progressbar(total_time, total_time - secs_left)}\nОсталось {secs_left} секунд"
    BOT.update_message(chat_id, message_id, update_message)


def choose(author_id, text):
    text = "Время вышло!!"
    BOT.send_message(author_id, text)


def main():
    BOT.reply_on_message(reply)
    BOT.run_bot()


if __name__ == '__main__':
    main()
