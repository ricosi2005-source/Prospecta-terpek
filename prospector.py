def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
        },
        timeout=30,
    )

    print("=== TELEGRAM DEBUG ===")
    print("HTTP:", response.status_code)
    print("Respuesta:", response.text)
    print("======================")

    response.raise_for_status()
