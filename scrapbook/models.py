from django.db import models


class ScrapImage(models.Model):
    original_image = models.ImageField(upload_to='originals/')
    edited_image = models.ImageField(upload_to='edited/', null=True, blank=True)
    aesthetic = models.CharField(max_length=100)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aesthetic} - {self.caption[:30]}..."
