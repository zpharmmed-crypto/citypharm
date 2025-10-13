import threading
import os
from pyngrok import ngrok

# Запускаем Django сервер в отдельном потоке
def run_django():
    os.system("python manage.py runserver 8000")

# Открываем туннель ngrok
public_url = ngrok.connect(8000).public_url
print(f"\n🌍 Платформа доступна по ссылке: {public_url}\n")

# Запускаем Django в отдельном потоке
threading.Thread(target=run_django).start()

# Оставляем ngrok активным
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Остановка ngrok...")
    ngrok.disconnect(public_url)
