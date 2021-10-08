import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Poll(models.Model):
    question = models.OneToOneField(
        "polls.Question",
        on_delete=models.CASCADE,
        related_name="poll",
    )
    pub_date = models.DateTimeField("date published")
    premium = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        question = str(self.question)

        if self.premium:
            question = f"⭐️ {question}"

        if self.author:
            by = self._get_preposition_by()  # ["By", "Por"] | None
            question = f"{question} - {by} {self.author}"

        return question

    @property
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def _get_preposition_by(self):
        if self.question.is_in_english:
            return "By"

        if self.question.is_in_portuguese:
            return "Por"


class Question(models.Model):
    EN = "EN"
    PT_BR = "PT-BR"
    LANGUAGE_CHOICES = (
        (EN, "English"),
        (PT_BR, "Português (Brasil)"),
    )

    question_text = models.CharField(max_length=200)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default=EN, max_length=5
    )

    @property
    def is_in_english(self):
        return self.language == self.EN

    @property
    def is_in_portuguese(self):
        return self.language == self.PT_BR

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
