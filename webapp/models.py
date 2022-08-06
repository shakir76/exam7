from django.db import models


# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=100, null=False, blank=False, verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.id}. {self.question}: {self.created_at} "

    class Meta:
        db_table = "Polls"
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Choice(models.Model):
    text = models.CharField(max_length=100, null=False, blank=False, verbose_name="Текст")
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE, related_name="poll",
                             verbose_name="Опрос")

    def __str__(self):
        return f"{self.text} - {self.poll}"

    class Meta:
        db_table = "Choice"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
