from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=100, unique=True)
    language = models.CharField(max_length=10, default="am")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.telegram_id