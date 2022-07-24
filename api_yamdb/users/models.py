from django.contrib.auth.models import AbstractUser
from django.db import models

USER = "user"
MODERATOR = "moderator"
ADMIN = "admin"

role_choices = [
    (USER, USER),
    (MODERATOR, MODERATOR),
    (ADMIN, ADMIN),
]


class User(AbstractUser):
    email = models.EmailField("email address", unique=True, blank=False)
    bio = models.TextField(
        "Биография",
        blank=True,
    )
    role = models.TextField("Роль", choices=role_choices, default=USER)
