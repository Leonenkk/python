import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
email_sender='leonenko.maksym@yandex.by'
email_receiver='maxleon1611@gmail.com'
subject='Приглашение!'
letter="""From: {email_s}
To: {email_r}
Subject: {sub}
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
""".format(email_s=email_sender,email_r=email_receiver,sub=subject)
site_name='https://dvmn.org/referrals/dyIERzS1VX85dP8gzMFuxEM36urVVWrwBbLjhGmM/'
friend_name='Влад'
sender_name='Максим'
letter=letter.replace('%website%',site_name).replace('%friend_name%',friend_name).replace('%my_name%',sender_name)
print(letter)
letter=letter.encode("UTF-8")
server=smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(os.getenv("LOGIN"),os.getenv("PASSWORD"))
server.sendmail(email_sender,email_receiver,letter)
server.quit()
