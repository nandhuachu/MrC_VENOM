"""Get Detailed info about any message
Syntax: .json"""

import os
from pyrogram import Client, filters
from info import COMMAND_HAND_LER, USE_AS_BOT
from plugins.helper_functions.cust_p_filters import f_onw_fliter


@Client.on_message(filters.command("json", COMMAND_HAND_LER) & f_onw_fliter)
async def jsonify(_, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message

    try:
        await message.reply_text(f"<code>{the_real_message}</code>")
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            reply_to_message_id=reply_to_id
        )
        os.remove("json.text")
