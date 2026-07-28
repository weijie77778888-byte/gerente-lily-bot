import os
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError(
        "TOKEN not found. Add TOKEN in Railway Variables."
    )


def main_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                "🤝 CANAL Cooperar",
                url="https://t.me/lily_grupo_aj",
            )
        ],
        [
            InlineKeyboardButton(
                "📷 INSTAGRAM",
                url="https://www.instagram.com/lily__gerente",
            )
        ],
        [
            InlineKeyboardButton(
                "💬 SUPPORT",
                url=(
                    "https://vue.livehelp100service.com/"
                    "03ddbf9d379cab2jkfle-kelid2bd983091ae237dc6ecf19c4463c6b4b98ff9f1fda5365b7b73424b20baef28"
                ),
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 WEBSITE",
                url="https://www.ajgrupo.com",
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    text = (
        "👋 Olá! Bem-vindo ao Bot Oficial Lily Gerente.\n\n"
        "Escolha uma opção abaixo:"
    )

    if update.message:
        await update.message.reply_text(
            text=text,
            reply_markup=main_menu(),
        )


async def menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message:
        await update.message.reply_text(
            "📋 Menu principal:",
            reply_markup=main_menu(),
        )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message:
        await update.message.reply_text(
            "Use /start ou /menu para abrir o menu.",
            reply_markup=main_menu(),
        )


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Lily Gerente Bot is online")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
