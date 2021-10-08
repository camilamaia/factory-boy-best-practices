from django.contrib import admin

from polls.models import Choice, Poll, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollInline(admin.TabularInline):
    model = Poll


class QuestionAdmin(admin.ModelAdmin):
    inlines = [PollInline, ChoiceInline]
    list_display = ("question_text", "language", "poll", "get_pub_date")
    list_filter = ("poll__pub_date", "language", "poll__premium")
    search_fields = ("question_text",)
    ordering = ("-poll__pub_date",)

    @admin.display(description="Pub Date")
    def get_pub_date(self, obj):
        return obj.poll.pub_date


admin.site.register(Question, QuestionAdmin)
