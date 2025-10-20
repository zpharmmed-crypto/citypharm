#!/usr/bin/env bash
# Выполняет миграции и создаёт суперпользователя при деплое на Render

echo "🚀 Запускаем миграции..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "✅ Миграции применены."

# Автоматическое создание суперпользователя (если его нет)
echo "⚙️ Проверяем наличие суперпользователя..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "Admin12345")
    print("👑 Суперпользователь создан: admin / Admin12345")
else:
    print("🟢 Суперпользователь уже существует")
EOF
