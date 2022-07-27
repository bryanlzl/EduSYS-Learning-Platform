
import os

from menu import Menu
from dotenv import load_dotenv
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

load_dotenv()

def main():
    updater = Updater(os.getenv("PYTHON_BOT_TOKEN"), use_context=True)

    updater.dispatcher.add_handler(CommandHandler("group", Menu.command_group));
    updater.dispatcher.add_handler(CommandHandler("discqn", Menu.command_discqn));

    # MODULE SELECT OPTION
    updater.dispatcher.add_handler(CommandHandler('start', Menu.menu_button))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.error_message, pattern='phy_chem'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.error_message, pattern='bio_chem'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.main_menu_btns, pattern='main_menu'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.organic_chem_menu, pattern='org_chem'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.error_message, pattern='adols_lec_tut'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.supplementary_info, pattern='supp_info'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.module_select_menu, pattern='module_select'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.discussion_board, pattern='discussion_board'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.group_study_chat, pattern='group_study_chat'))

    # ORGANIC CHEMISTRY 
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.organic_chem_topic1, pattern='carbonyl_lec_tut'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.organic_topic1_lec, pattern='organic_topic1_lec'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.organic_topic1_tut, pattern='organic_topic1_tut'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.organic_topic1_slides, pattern='organic_topic1_slides'))
    updater.dispatcher.add_handler(CallbackQueryHandler(Menu.organic_topic1_questions, pattern='organic_topic1_questions'))
    updater.dispatcher.add_error_handler(Menu.error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()