import time
import telegram
from constants import *
from telegram import Update
from telegram.ext import CallbackContext

class Menu:
    def __init__(self):
        pass

    @staticmethod
    def menu_button(bot, update):
        bot.message.reply_text("⚠️<b> Disclaimer </b>⚠️ Please be aware that with the ongoing NUS LifeHack Hackathon 2021 and its development, this bot is a prototype of our entire project. As such, this bot has only been designed for one major at the moment.", parse_mode = telegram.ParseMode.HTML)
        time.sleep(1)
        bot.message.reply_text("Welcome to Team SYS Education Bot! This bot is designed in Telegram to offer the versatility between both iOS and Android users whilst taking advantage in technology to not only provide new ways to learn, but also on how people teach, with the extensive use and collaboration of resources to make learning and teaching to be a more safer, exciting, effective and engaging activity!\n\nYou are currently registered in the course <b>Chemistry</b>, what would you like to do today?",
                         reply_markup=MAIN_MENU_BTNS, parse_mode = telegram.ParseMode.HTML)

    @staticmethod
    def main_menu_btns(bot, update):
        bot.callback_query.message.edit_text("Welcome to Team SYS Education Bot! This bot is designed in Telegram to offer the versatility between both iOS and Android users whilst taking advantage in technology to not only provide new ways to learn, but also on how people teach, with the extensive use and collaboration of resources to make learning and teaching to be a more safer, exciting, effective and engaging activity!\n\nYou are currently registered in the course <b>Chemistry</b>, what would you like to do today?",
                          reply_markup=MAIN_MENU_BTNS, parse_mode = telegram.ParseMode.HTML)

    @staticmethod
    def module_select_menu(bot, update):
        bot.callback_query.message.edit_text("<b>1️⃣ Module Selection</b>\n\nThe catalog of courses your major is currently registered in is now open. What would you like to find out more about in your current major?",
                          reply_markup=MODULE_SELECT_BTNS, parse_mode = telegram.ParseMode.HTML)

    @staticmethod
    def organic_chem_menu(bot, update):
        bot.callback_query.message.edit_text("<b>Organic Chemistry</b> module has been selected.\n\nHere are the list of chapters and supplementary information for your use. What would you like to do?",
                          reply_markup=ORGANIC_CHEM_BTNS, parse_mode = telegram.ParseMode.HTML)

    @staticmethod
    def module_select_menu(bot, update) -> None:
        bot.callback_query.message.edit_text("<b>1️⃣ Module Selection</b>\n\nThe catalog of courses your major is currently registered in is now open. What would you like to find out more about in your current major?",
                          reply_markup=MODULE_SELECT_BTNS, parse_mode = telegram.ParseMode.HTML)

    @staticmethod
    def organic_chem_topic1(bot, update):
        bot.callback_query.message.edit_text("<b>Topic 1: Carbonyl Carbons</b> has been selected.\n\nGreat! What material would you like to review right now?",
                          reply_markup=ORGANIC_CHEM_TOPIC1, parse_mode = telegram.ParseMode.HTML)

    @staticmethod
    def organic_topic1_lec(update, context) -> None:
        context.bot.sendMessage(update.effective_chat.id, text="https://www.youtube.com/watch?v=gbOyppJ9OK4")

    @staticmethod
    def organic_topic1_tut(update, context) -> None:
        context.bot.sendMessage(update.effective_chat.id, text="https://www.youtube.com/watch?v=nB9yqj-ZcAk")

    @staticmethod
    def error_message(update, context) -> None:
        message_id = context.bot.sendMessage(update.effective_chat.id, text="❌ There is currently no content for this module")
        time.sleep(5)
        context.bot.deleteMessage(update.effective_chat.id, message_id.message_id)

    @staticmethod
    def supplementary_info(update, context) -> None:
        xfile = "./resources/supp_info.pdf"
        context.bot.sendDocument(update.effective_chat.id, document=open(xfile, "rb"))

    @staticmethod
    def organic_topic1_slides(update, context) -> None:
        xfile = "./resources/topic_1_slides.pdf"
        context.bot.sendDocument(update.effective_chat.id, document=open(xfile, "rb"))

    @staticmethod
    def organic_topic1_questions(update, context) -> None:
        xfile = "./resources/topic_1_tutorial.pdf"
        context.bot.sendDocument(update.effective_chat.id, document=open(xfile, "rb"))

    @staticmethod
    def discussion_board(update, context) -> None:
        context.bot.sendMessage(update.effective_chat.id, text="Great to know that you are interested in joining in more discussions about this particular module! Want to answer some questions or have some burning questions to ask your peers? Check out the resources down below!\n\n<b>To ask a question</b>, use the command /discqn (your question here) and submit them accordingly! You (and your peers) can join the discussion board and actively answer or look up any questions there!\n\nYou are invited to join the discussion board here: https://t.me/sys_module", parse_mode = telegram.ParseMode.HTML)

    @staticmethod
    def group_study_chat(update, context) -> None:
        context.bot.sendMessage(update.effective_chat.id, text="Awesome! We are committed into protecting your privacy and ensuring that you don't get any dubious strangers by yourself in a 1-to-1 conversation, so we have decided to make these group requests open for viewing to all so that others (and the moderators) can help you check them out as well!\n\n<b>To initiate a group request</b>, use the command /group (description) and submit them accordingly! Your information will be protected here, so you can choose the people that you want to form a group with at your own discretion!\n\nYou are invited to join the study group sessions here: https://t.me/sys_group", parse_mode = telegram.ParseMode.HTML)

    @staticmethod
    def command_discqn(update: Update, _: CallbackContext):
        user = update.message.from_user
        
        if update.message.text == "/discqn":
            update.message.reply_text("Please enter your discussion question down below, and we will post it in the discussion board for students to respond!\n\nThe correct format is: /discqn <your question>")
        
        elif len(update.message.text.partition("/discqn ")[2]) <= 50:
            update.message.reply_text("Your question that you have asked seems quite short! Please try that again and add more details into your questions so that it is more thoughtful and detailed! (min 50 characters)")
        
        else:
            update.message.reply_text("✅ <b>Your question has been received.</b> ✅\n\nCheck out the discussion board now! We have put up your question in the discussion board for the class to see! Hope that you can get some good replies soon!\n\n<i>You will be brought back to the main menu now.</i>", parse_mode = telegram.ParseMode.HTML)
            message = update.message.text.partition("/discqn ")[2]
            _.bot.send_message(chat_id = -1001591984369, text = "✋ <b>Question Discussions</b> ✋\n\nStudent ID: " + str(user.id) + "\n\nMessage: " + str(message) + "\n\n<i>Please remember the human behind the question and be nice! We are all here to learn and to clarify our doubts.</i> 😇", parse_mode = telegram.ParseMode.HTML)
            time.sleep(1)
            return Menu.menu_button(update, _)

    @staticmethod
    def command_group(update: Update, _: CallbackContext):
        user = update.message.from_user
        
        if update.message.text == "/group":
            update.message.reply_text("Please enter your study group invitation down below, and we will post it in the forum for students to respond and for you to initiate a conversation!\n\nThe correct format is: /group <description of what you want in a study group>")
        
        elif len(update.message.text.partition("/group ")[2]) <= 10:
            update.message.reply_text("That request seems quite short! Please try that again and add more details into your request so that people can know what kind of study group you're looking for! (min 10 characters)")
        
        else:
            update.message.reply_text("✅ <b>Your request has been received.</b> ✅\n\nCheck out the available study group requests now! We have put up your group offer in the discussion board for the class to see! Hope that you can find some friends and study buddies to go along with!\n\n<i>You will be brought back to the main menu now.</i>", parse_mode = telegram.ParseMode.HTML)
            message = update.message.text.partition("/group ")[2]
            _.bot.send_message(chat_id = -1001592146749, text = "📖 <b>Study Group Request!</b> 📖\n\nStudent First Name: " + str(user.first_name) + "\n\nMessage: " + str(message) + "\n\n<i>Please remember the human behind this group study request and be nice! Any suspicious messages can result in disciplinary actions against you.</i>", parse_mode = telegram.ParseMode.HTML)
            time.sleep(1)
            return Menu.menu_button(update, _)

    @staticmethod
    def error(update, context):
        print(f'Update {update} caused error {context.error}')
