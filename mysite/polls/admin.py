from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        (
            "Question information",
            {
                "fields": ["author", "language", "premium", "pub_date"],
            },
        ),
    ]
    inlines = [ChoiceInline]
    list_display = (
        "question_text",
        "pub_date",
        "was_published_recently",
        "author",
        "language",
        "premium",
    )
    list_filter = ["pub_date", "language", "premium"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
