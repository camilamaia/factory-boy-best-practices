import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    EN = "EN"
    PT_BR = "PT-BR"
    LANGUAGE_CHOICES = (
        (EN, "English"),
        (PT_BR, "Português (Brasil)"),
    )

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default=EN, max_length=5
    )
    author = models.CharField(max_length=100, null=True, blank=True)
    premium = models.BooleanField(default=False)

    def __str__(self):
        question = self.question_text

        if self.premium:
            question = f"⭐️ {question}"

        if self.author:
            by = self._get_by()  # ["By", "Por"] | None
            question = f"{question} - {by} {self.author}"

        return question

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @property
    def is_in_english(self):
        return self.language == self.EN

    @property
    def is_in_portuguese(self):
        return self.language == self.PT_BR

    def _get_by(self):
        if self.is_in_english:
            return "By"

        if self.is_in_portuguese:
            return "Por"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
