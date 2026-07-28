import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("TOKEN not found. Please add TOKEN in Railway Variables.")


def menu():
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
                "💬 SUPPORT",
                url="https://vue.livehelp100service.com/03ddbf9d379cab2jkfle-kelid2bd983091ae237dc6ecf19c4463c6b4b98ff9f1fda5365b7b73424b20baef28"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 WEBSITE",
                url="https://www.ajgrupo.com"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 *Bem-vindo ao Bot Oficial Lily Gerente!*\n\n"
        "Escolha uma opção abaixo:"
    )

    await update.message.reply_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=menu(),
    )


async def canal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤝 Canal Cooperar\n\nhttps://t.me/lily_grupo_aj"
    )


async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📷 Instagram Oficial\n\nhttps://www.instagram.com/lily__gerente"
    )


async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 Suporte Oficial\n\nhttps://vue.livehelp100service.com/03ddbf9d379cab2jkfle-kelid2bd983091ae237dc6ecf19c4463c6b4b98ff9f1fda5365b7b73424b20baef28"
    )


async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌐 Website Oficial\n\nhttps://www.ajgrupo.com"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("canal", canal))
    app.add_handler(CommandHandler("instagram", instagram))
    app.add_handler(CommandHandler("support", support))
    app.add_handler(CommandHandler("website", website))

    print("✅ Lily Gerente Bot Online")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
