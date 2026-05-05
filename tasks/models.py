from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name='categories'
)

    def __str__(self):
        return self.name

class Task(models.Model):
    owner = models.ForeignKey(    # ← добавь это!
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tasks'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )

    def __str__(self):
        return self.title