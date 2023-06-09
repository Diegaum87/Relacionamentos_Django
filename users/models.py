from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()

    def __repr__(self) -> str:
        return f"<User ({self.id}) - ({self.first_name})>"
