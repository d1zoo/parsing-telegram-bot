from telegram import CallbackQuery, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from Token import TOKEN
from keys import main_menu_keyboard, vacancies
from buttons import knop, knopka

url = ["https://bishkek.headhunter.kg/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&text=python",
        # "https://bishkek.headhunter.kg/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&text=java",
        # "https://bishkek.headhunter.kg/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&text=java+script",
        "https://bishkek.headhunter.kg/search/vacancy?area=&fromSearchLine=true&text=java",
        "https://bishkek.headhunter.kg/search/vacancy?area=&fromSearchLine=true&text=java+script",
        "https://devkg.com/ru/jobs"]

def make_soup(urlindex):
    resp = Request(urlindex, headers={'User-Agent': 'Mozilla/5.0'})
    data = urlopen(resp).read()
    soup = BeautifulSoup(data, 'html.parser')
    qwe = soup.find_all('a', attrs={'class': 'bloko-link'})
    zxv = soup.find_all('a', attrs={'class': 'link'})

    return qwe, zxv


def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id = update.effective_chat.id,
        sticker = 'CAACAgIAAxkBAAEEkONiaAi5Y7higpMwEWeCOoz5H8OsmwACOAADMWfCNS21WOy1lXbLJAQ'
    )
    update.message.reply_text(
        'Добро пожаловать, {username}'.format(
            username = update.effective_user.first_name \
            if update.effective_user.first_name is not None \
            else update.effective_user.username
        ),
        reply_markup=main_menu_keyboard()
        )
        

def acc(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите направление',
        reply_markup=vacancies()
    )


def vac_python(update: Update, context: CallbackContext):
    items, _ = make_soup(url[0])
    for q in items:
        if 'vacancy?' in q.get('href'):
            continue
        
        if 'Python' in q.get_text() or 'python' in q.get('href'):
            link = q.get('href')
            context.bot.send_message(
                chat_id = update.effective_chat.id,
                text = f'{link}\n{q.text}'
            )
        
    _, items2 = make_soup(url[3])
    for q in items2:
        if 'vacancy?' in q.get('href'):
            continue
        if 'Python' in q.get_text() or 'python' in q.get('href'):
            link = q.get('href')
            a_link='https://devkg.com'+link
            context.bot.send_message(
                chat_id = update.effective_chat.id,
                text = f'{a_link}\n{q.text}'
            )
def vac_java(update: Update, context: CallbackContext):
    items, _ = make_soup(url[1])
    for q in items:
        if 'vacancy?' in q.get('href'):
            continue
        if 'Java' in q.get_text() or 'java' in q.get('href'):
            link = q.get('href')
            context.bot.send_message(
                chat_id = update.effective_chat.id,
                text = f'{link}\n{q.text}'
            )
    _, items2 = make_soup(url[3])
    for q in items2:
        if 'vacancy?' in q.get('href'):
            continue
        if 'Java' in q.get_text() or 'java' in q.get('href'):
            link = q.get('href')
            a_link='https://devkg.com'+link
            context.bot.send_message(
                chat_id = update.effective_chat.id,
                text = f'{a_link}\n{q.text}'
            )
            
def vac_js(update: Update, context: CallbackContext):
    items, _ = make_soup(url[2])
    for q in items:
        if 'vacancy?' in q.get('href'):
            continue
        if 'JS' in q.get_text() or 'JavaScript' in q.get_text() or 'Frontend' in q.get_text():
            link = q.get('href')
            context.bot.send_message(
                chat_id = update.effective_chat.id,
                text = f'{link}\n{q.text}'
            )
            
    _, items2 = make_soup(url[3])
    for q in items2:
        if 'vacancy?' in q.get('href'):
            continue
        if 'JS' in q.get_text() or 'JavaScript' in q.get_text() or 'Frontend' in q.get_text():
            link = q.get('href')
            a_link='https://devkg.com'+link
            context.bot.send_message(
                chat_id = update.effective_chat.id,
                text = f'{a_link}\n{q.text}'
            )
            
    

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(knop[0]),
    acc
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex("Python"),
    vac_python
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex("Java"),
    vac_java
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex("JS"),
    vac_js
))


updater.start_polling()
updater.idle()