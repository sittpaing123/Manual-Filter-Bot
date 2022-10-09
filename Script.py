class script(object):
    START_TXT = """Hello {} 👋
I'm An Advanced Manual Filter Bot 😎
Just Add Me To Your Group As Admin 🤩"""

    HELP_TXT = """Here Is The Help For My Commands"""

    ABOUT_TXT = """★ My Name: <a href=https://t.me/{}>{}</a>
★ Creator: <a href=https://t.me/Hansaka_Anuhas>Hansaka Anuhas</a> 🇱🇰
★ Bot Server: <a href=https://railway.app/>Railway</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>"""

    MANUELFILTER_TXT = """Help: <b>Manual Filters</b>

<b>Commands and Usage:</b>
• /filter - Add Filter
• /filters - List All Filters
• /del - Delete Filter
• /delall - Delete All Filters"""

    BUTTON_TXT = """Help: <b>Buttons</b>

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/{})</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:Alert Message)</code>"""

    CONNECTION_TXT = """Help: <b>Connections</b>

<b>Commands and Usage:</b>
• /connect - Connect PM
• /disconnect - Disconnect PM
• /connections - List All Connections"""

    STATUS_TXT = """★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""
