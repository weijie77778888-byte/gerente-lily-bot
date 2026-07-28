keyboard = [
    [
        InlineKeyboardButton(
            "🤝 CANAL Cooperar",
            url="https://t.me/lily_grupo_aj"
        )
    ],
    [
        InlineKeyboardButton(
            "📷 Instagram",
            url="https://www.instagram.com/lily__gerente"
        )
    ],
    [
        InlineKeyboardButton(
            "💬 Support",
            url="https://vue.livehelp100service.com/03ddbf9d379cab2jkfle-kelid2bd983091ae237dc6ecf19c4463c6b4b98ff9f1fda5365b7b73424b20baef28"
        )
    ],
    [
        InlineKeyboardButton(
            "🌐 Website",
            url="https://www.ajgrupo.com"
        )
    ],
]

await update.message.reply_text(
    "👋 *Bem-vindo ao Bot Oficial Lily Gerente!*\n\n"
    "Escolha uma opção abaixo:",
    parse_mode="Markdown",
    reply_markup=InlineKeyboardMarkup(keyboard),
)
