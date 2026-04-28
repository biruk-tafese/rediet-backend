from django.db import models

class PrayerRequest(models.Model):
    telegram_id = models.CharField(max_length=100, db_index=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]