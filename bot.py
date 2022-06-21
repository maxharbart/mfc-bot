import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config

from telegram import ForceReply, ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext
)
# Configure writing to google sheets


scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("mfc-to-sheets-7e344e318d1d.json", scopes) #access the json key  
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("MFC Anketa")  #open sheet
sheet = sheet.sheet1 
line = 1 



# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Configure steps of questionnaire


FIRSTQ, SECONDQ, THIRDQ, FOURTHQ, FIFTHQ, SIXTHQ, SEVENTHQ, EIGHTQ, NINETHQ, TENHQ, ELEVENTHQ, TWELVTHQ, THIRTEENTHQ, CANCEL = range(14)

def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation."""
    reply_keyboard = [['Да', 'Нет', 'Частично']]
    update.message.reply_text(
        'Пройди, пожалуйста, опрос ниже.\n\n'
        '1. Твои ожидания от работы оправдались?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='Первый вопрос'
        ),
    )

    return FIRSTQ

def secondq(update: Update, context: CallbackContext) -> int:
    """Second question."""
    user = update.message.from_user
    logger.info("Name: %s %s", user.first_name)
    sheet.update('A'+str(line), user.first_name)
    logger.info("1 question: %s", update.message.text)
    reply_keyboard = [['Да, welcome помог мне'], ['Нет, мне не хватило информации'], ['Я не проходил(а) welcome']]

    update.message.reply_text(
        '2. Информации в welcome-тренинге было достаточно?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='Второй вопрос'
        ),
    )

    return SECONDQ

def thirdq(update: Update, context: CallbackContext) -> int:
    """Third question."""
    logger.info("2 question: %s", update.message.text)
    sheet.update('B'+str(line), update.message.text)
    reply_keyboard = [['1', '2', '3', '4', '5']]

    update.message.reply_text(
        '3. Оцени работу наставника',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='Третий вопрос'
        ),
    )

    return THIRDQ

def fourthq(update: Update, context: CallbackContext) -> int:
    """Fourth question."""
    logger.info("3 question: %s", update.message.text)
    sheet.update('C'+str(line), update.message.text)
    reply_keyboard = [['1', '2', '3', '4', '5']]

    update.message.reply_text(
        '4. Оцени работу сервисного центра ',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='Четвертый вопрос'
        ),
    )

    return FOURTHQ

def fifthq(update: Update, context: CallbackContext) -> int: 
    
    """Fifth question."""
    logger.info("4 question: %s", update.message.text)
    sheet.update('D'+str(line), update.message.text)
    reply_keyboard = [['1', '2', '3', '4', '5']]

    update.message.reply_text(
        '5. Оцени работу ОТиПБ',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='Пятый вопрос'
        ),
    )

    return FIFTHQ

def sixthq(update: Update, context: CallbackContext) -> int:
    """Sixth question."""
    logger.info("5 question: %s", update.message.text)
    sheet.update('E'+str(line), update.message.text)
    reply_keyboard = [['1', '2', '3', '4', '5']]

    update.message.reply_text(
        '6. Оцени работу HR',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='Шестой вопрос'
        ),
    )

    return SIXTHQ

def seventhq(update: Update, context: CallbackContext) -> int:
    """Seventh question."""
    logger.info("6 question: %s", update.message.text)
    sheet.update('F'+str(line), update.message.text)
    reply_keyboard = [['1', '2', '3', '4', '5']]

    update.message.reply_text(
        '7. Оцени работу службы безопасности',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='Седьмой вопрос'
        ),
    )

    return SEVENTHQ

def eightq(update: Update, context: CallbackContext) -> int:
    """8 question."""
    
    logger.info("7 question: %s", update.message.text)
    sheet.update('G'+str(line), update.message.text)
    reply_keyboard = [['Все необходимые программы, средства коммуникаций были в моем распоряжении'], ['Возникли затруднения в момент выхода на работу, рабочее место было недостаточно подготовлено'], ['Мое рабочее место было не подготовлено']]

    update.message.reply_text(
        '8. Как было оснащено твое рабочее место?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='Восьмой вопрос'
        ),
    )

    return EIGHTQ

def ninetq(update: Update, context: CallbackContext) -> int:
    """9 question."""
    
    logger.info("8 question: %s", update.message.text)
    sheet.update('H'+str(line), update.message.text)
    reply_keyboard = [['Да', 'Нет', 'Частично']]

    update.message.reply_text(
        '9. Ты понимаешь поставленные задачи в КЛИ, они достижимые?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='Девятый вопрос'
        ),
    )

    return NINETHQ

def tenthq(update: Update, context: CallbackContext) -> int:
    """10 question"""
    logger.info("9 question: %s", update.message.text)
    sheet.update('I'+str(line), update.message.text)
    update.message.reply_text(
        '10. Ты испытываешь недостаток информации/практических навыков для эффективной работы?',
        reply_markup=ForceReply()
    )

    return TENHQ

def eleventhq(update: Update, context: CallbackContext) -> int:
    """11 question"""
    logger.info("10 question: %s", update.message.text)
    sheet.update('J'+str(line), update.message.text)
    update.message.reply_text(
        '11. Возникали трудности в работе и как ты справился с ними?',
        reply_markup=ForceReply()
    )

    return ELEVENTHQ

def twelvthq(update: Update, context: CallbackContext) -> int:
    """12 question"""
    logger.info("11 question: %s", update.message.text)
    sheet.update('K'+str(line), update.message.text)
    update.message.reply_text(
        '12. Оцени психологический климат в коллективе ',
        reply_markup=ForceReply()
    )

    return TWELVTHQ

def thirteenthq(update: Update, context: CallbackContext) -> int:
    """13 question."""
    logger.info("12 question: %s", update.message.text)
    sheet.update('L'+str(line), update.message.text)
    reply_keyboard = [['Да', 'Нет']]

    update.message.reply_text(
        '13. Нужна ли тебе встреча с HR для снятия вопросов?  ',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True, input_field_placeholder='13 вопрос'
        ),
    )

    return THIRTEENTHQ

def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s completed questionnaire.", user.first_name)
    global line
    sheet.update('M'+str(line), update.message.text)
    reply_keyboard = [['Пройти опрос еще раз']]
    
    update.message.reply_text(
        'Спасибо за обратную связь! Продолжай погружаться в работу и культуру компании!', 
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    )
    line = line + 1
    return CANCEL




def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states FIRSTQ, SECONDQ, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRSTQ: [MessageHandler(Filters.regex('^(Да|Нет|Частично|)$'), secondq)],
            SECONDQ: [MessageHandler(Filters.regex('^(Да, welcome помог мне|Нет, мне не хватило информации|Я не проходил\(а\) welcome|)$'), thirdq)],
            THIRDQ: [MessageHandler(Filters.regex('^(1|2|3|4|5|")$'), fourthq)],
            FOURTHQ: [MessageHandler(Filters.regex('^(1|2|3|4|5|")$'), fifthq)],
            FIFTHQ: [MessageHandler(Filters.regex('^(1|2|3|4|5|")$'), sixthq)],
            SIXTHQ: [MessageHandler(Filters.regex('^(1|2|3|4|5|")$'), seventhq)],
            SEVENTHQ: [MessageHandler(Filters.regex('^(1|2|3|4|5|")$'), eightq)],
            EIGHTQ: [MessageHandler(Filters.regex('^(Все необходимые программы, средства коммуникаций были в моем распоряжении|Возникли затруднения в момент выхода на работу, рабочее место было недостаточно подготовлено|Мое рабочее место было не подготовлено|)$'), ninetq)],
            NINETHQ: [MessageHandler(Filters.regex('^(Да|Нет|Частично|)$'), tenthq)],
            TENHQ: [MessageHandler((Filters.text), eleventhq)],
            ELEVENTHQ: [MessageHandler((Filters.text), twelvthq)],
            TWELVTHQ: [MessageHandler((Filters.text), thirteenthq)],
            THIRTEENTHQ: [MessageHandler(Filters.regex('^(Да|Нет|)$'), cancel)],
            CANCEL: [MessageHandler(Filters.regex('^(Пройти опрос еще раз|)$'), start)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()