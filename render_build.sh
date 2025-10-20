#!/usr/bin/env bash
# Render build script for Django

set -o errexit  # Exit on error

echo "📦 Running Django migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "✅ Migrations completed."

# Optional: auto-create superuser
echo "👑 Checking for superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "Admin12345")
    print("✅ Superuser created: admin / Admin12345")
else:
    print("🟢 Superuser already exists.")
EOF
