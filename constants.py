from telegram import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup

MAIN_MENU_BTNS = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('1️⃣ Module Selection', callback_data='module_select')],
                [InlineKeyboardButton('2️⃣ Discussion Board', callback_data='discussion_board')],
                [InlineKeyboardButton('3️⃣ Group Study Chat', callback_data='group_study_chat')]
            ]
        )

MODULE_SELECT_BTNS = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('🧪 Organic Chemistry', callback_data='org_chem')],
                [InlineKeyboardButton('🔬 Physical Chemistry', callback_data='phy_chem')],
                [InlineKeyboardButton('🔬 Biochemistry', callback_data='bio_chem')],
                [
                    InlineKeyboardButton('📚 Main Menu', callback_data="main_menu")
                ],
                [
                    InlineKeyboardButton('◀️ Back', callback_data="main_menu")
                ]
            ]
        )

# ORGANIC CHEMISTRY ACTIONS
ORGANIC_CHEM_BTNS = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Topic 1: Carbonyl group', callback_data='carbonyl_lec_tut'),
                    InlineKeyboardButton('Topic 2: Aldols', callback_data='adols_lec_tut')
                ],
                [
                    InlineKeyboardButton('📓 Supplementary Information', callback_data='supp_info')
                ],
                [
                    InlineKeyboardButton('📚 Main Menu', callback_data="main_menu")
                ],
                [
                    InlineKeyboardButton('◀️ Back', callback_data="module_select")
                ]
            ]
        )

ORGANIC_CHEM_TOPIC1 = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🎞️ Lecture Videos', callback_data="organic_topic1_lec"),
                    InlineKeyboardButton('🎞️ Tutorial Videos', callback_data="organic_topic1_tut")
                ],
                [
                    InlineKeyboardButton('Lecture Slides', callback_data="organic_topic1_slides"),
                    InlineKeyboardButton('❓ Tutorial Questions', callback_data="organic_topic1_questions")
                ],
                [
                    InlineKeyboardButton('📚 Main Menu', callback_data="main_menu")
                ],
                [
                    InlineKeyboardButton('◀️ Back', callback_data="org_chem")
                ]
            ]
        )
