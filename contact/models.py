from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=222, blank=True)
    email = models.EmailField()
    subject = models.TextField(max_length=255, blank=True)
    message = models.TextField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
