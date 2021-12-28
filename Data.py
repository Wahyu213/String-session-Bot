from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hello {}

If you don't trust this bot,
1) don't read this message
2) block bot or delete chat

This Bot Works To Help You Get Session String Via Bot. Recommendations If You Want To Take String Use Another Account,
Managed By @zenfrans
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton(text="Home", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton("Maintaned By", url="https://t.me/zenfrans")],
        [
            InlineKeyboardButton("How to use me", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
      ],
        [InlineKeyboardButton("Other bot info", url="https://t.me/nbzoning")],
    ]


    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About this bot
/help - How to use this bot
/start - Start Bot
/generate - Start Generating Session
/cancel - Cancel process
/restart - Restart process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to retrieve pyrograms and telethon string sessions by @nbzoning

Group Support : [Gabung](https://t.me/OkaeriUserbot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @zenfrans
    """
