import telebot
import mysql.connector
from market import Markets, bot


markets = Markets()


def my_sql_connect(name, password, database):
    mydb = mysql.connector.connect(
      host="localhost",
      user=name,
      password=password,
      database=database
    )
    return mydb


@bot.message_handler(commands=['start'])
def message_welcome(message):
    bot.send_message(message.chat.id , 'Здравствуйте, вас приветствует Market bot.')
    mydb = my_sql_connect('root', '', 'my_market')
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM Users WHERE telegram_id = '{message.chat.id}'")
    myresult = mycursor.fetchall()
    if myresult:
        for i in myresult:
            if i[3] == 'Client':
                pass
            elif i[3] == 'Admin':
                pass
            elif i[3]== 'Market':
                markets.start_command(message)
    else:
        bot.send_mesage(message.chat.id, 'вы новый пользователь')
        sql = "INSERT INTO Users (telegram_id, name) VALUES (%s, %s)"
        val = (message.chat.id, message.from_user.first_name)
        mycursor.execute(sql, val)

        mydb.commit()



@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    mydb = my_sql_connect('root', '', 'my_market')
    



    # bot.send_message(message.chat.id, message)
    photo = message.json["photo"][-1]["file_id"]
    # bot.send_message(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo)




@bot.callback_query_handler(func=lambda call: True)
def inline_answer(call):
    if (call.data == 'new_p'):
        bot.send_message(call.from_user.id , 'Для начало нужно выполнить следующие действия:\n1.Загрузить фото товара.\n2.Информация о товаре\n3.Цена товара\n4.Выбор категории')



    







bot.polling()
