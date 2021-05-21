from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

#class ChoiceInline(admin.StackedInline): #두줄출력
class ChoiceInline(admin.TabularInline): #한줄출력

    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] #출력형태 뒤집기
    fieldsets = [
        ('질문 입력', {'fields' : ['question_text']}),
        ('날짜 입력 ', {'fields' : ['pub_date'], 'classes' : ['collapse']}) #'classes' : ['collapse']} 숨기기기능
    ]
    inlines = [ChoiceInline] #한번에 여러번 생성시키기
    list_display = ('question_text', 'pub_date') #question_text 옆에 DATE PUBLISHED생성후 정렬하는 코드
    list_filter = ['pub_date'] #옆에 필터 생성
    search_fields = ['question_text'] #검색엔진 생성
# Register your models here.
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)