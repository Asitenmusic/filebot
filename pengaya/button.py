# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL1, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4 and FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ²", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ¹", url=client.invitelink1),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ³", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
if FORCE_SUB_CHANNEL4 and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ⁴", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ¹", url=client.invitelink1),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ²", url=client.invitelink2),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ³", url=client.invitelink3),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ⁴", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ²", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ¹", url=client.invitelink1),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ³", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL4 and not FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ⁴", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL1 and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ¹", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ²", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ³", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ⁴", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
