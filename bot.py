import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN environment variable not found!")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📢 Canal Oficial", url="https://t.me/lily_grupo_aj")],
        [InlineKeyboardButton("🌐 Site Oficial", url="https://grupoaj.com")],
        [InlineKeyboardButton("💬 Suporte", url="https://t.me/lily_grupo_aj")],
        [
            InlineKeyboardButton("ℹ️ Sobre", callback_data="about"),
            InlineKeyboardButton("🔒 Privacidade", callback_data="privacy"),
        ],
    ]

    text = (
        "👋 *Bem-vindo ao Bot Oficial da Lily Gerente!*\n\n"
        "Aqui você encontra acesso rápido ao nosso canal oficial, "
        "site e suporte.\n\n"
        "👇 *Escolha uma opção:*"
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.edit_message_text(
            "ℹ️ *Sobre*\n\n"
            "Este é o Bot Oficial da Lily Gerente.\n"
            "Utilize apenas nossos canais oficiais.",
            parse_mode="Markdown",
        )

    elif query.data == "privacy":
        await query.edit_message_text(
            "🔒 *Privacidade*\n\n"
            "Nunca compartilhe sua senha ou código de verificação.\n"
            "Use somente nossos links oficiais.",
            parse_mode="Markdown",
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Bot Online...")
    app.run_polling()


if __name__ == "__main__":
    main()
