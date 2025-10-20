#!/usr/bin/env bash
# 🚀 Скрипт автоматических миграций и создания админа на Render

echo "📦 Запуск миграций базы данных..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "✅ Миграции успешно применены."

# Создание суперпользователя (если нет)
echo "👑 Проверяем наличие суперпользователя..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "Admin12345")
    print("✅ Суперпользователь создан: admin / Admin12345")
else:
    print("🟢 Суперпользователь уже существует.")
EOF
