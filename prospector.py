import os
import sys
import requests


def get_secret(name):
    value = os.getenv(name)

    if not value:
        print(f"ERROR: Falta el secreto {name}")
        sys.exit(1)

    return value


TELEGRAM_TOKEN = get_secret("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = get_secret("TELEGRAM_CHAT_ID")
OPENROUTER_API_KEY = get_secret("OPENROUTER_API_KEY")


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

    response.raise_for_status()


def test_openrouter():
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": "Responde únicamente: PROSPECTA TERPEK OK",
            }
        ],
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]


def main():
    print("Iniciando Prospecta Terpek...")

    ai_response = test_openrouter()

    message = (
        "🚀 PROSPECTA TERPEK\n\n"
        "✅ GitHub Actions funcionando\n"
        "✅ Telegram conectado\n"
        "✅ OpenRouter conectado\n\n"
        f"🤖 IA: {ai_response}\n\n"
        "Siguiente bloque:\n"
        "🔎 búsqueda de oportunidades\n"
        "🌎 múltiples idiomas y países\n"
        "💼 trabajos freelance\n"
        "🏢 clientes potenciales\n"
        "🔥 oportunidades recientes\n"
        "💰 puntuación y precio sugerido"
    )

    send_telegram(message)

    print("Prueba completada correctamente.")


if __name__ == "__main__":
    main()
