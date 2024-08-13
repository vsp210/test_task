from django.db import models


class Participant(models.Model):
    name = models.CharField(
        "Имя",
        max_length=50,
    )
    email = models.CharField(
        "Email",
        max_length=70,
    )
    code = models.TextField(
        "Код",
        max_length=1000,
    )

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = 'Участник конкурса'
        verbose_name_plural = 'Участники конкурса'
