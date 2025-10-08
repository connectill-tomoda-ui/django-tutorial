from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]       # サイドバーに日付フィルタ
    search_fields = ["question_text"] # 検索ボックスを追加

admin.site.register(Question, QuestionAdmin)