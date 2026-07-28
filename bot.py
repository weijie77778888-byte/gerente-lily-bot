import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("Railway variable TOKEN is missing")


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:

    keyboard = [
        [
            InlineKeyboardButton(
                "🤝 CANAL Cooperar",
                url="https://t.me/lily_grupo_aj"
            )
        ],
        [
            InlineKeyboardButton(
                "📷 INSTAGRAM",
                url="https://www.instagram.com/lily__gerente"
            )
        ],
        [
            InlineKeyboardButton(
                "💬 Support",
                url=(
                    "https://vue.livehelp100service.com/"
                    "03ddbf9d379cab2jkfle-kelid2bd983091ae237dc6ecf19c4463c6b4b98ff9f1fda5365b7b73424b20baef28"
                )
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 Website",
                url="https://www.ajgrupo.com"
            )
        ],
    ]

    message = (
        "👋 Olá! Bem-vindo ao Bot Oficial Lily Gerente.\n\n"
        "Aqui você encontra acesso rápido ao nosso canal, "
        "Instagram, suporte e site oficial.\n\n"
        "Escolha uma opção abaixo:"
    )

    if update.message:
        await update.message.reply_text(
            message,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    print("Bot Lily Gerente está online.")
    application.run_polling()


if __name__ == "__main__":
    main()
