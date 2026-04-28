from django.db import models

class Message(models.Model):
    published_for = models.DateField(db_index=True, unique=True)

    title_am = models.TextField()
    title_en = models.TextField(blank=True, null=True)

    content_am = models.TextField()
    content_en = models.TextField(blank=True, null=True)

    verse = models.CharField(max_length=255, blank=True, null=True)
    audio = models.FileField(upload_to="audio/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_for"]

    def __str__(self):
        return f"Message {self.published_for}"