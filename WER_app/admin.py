from django.contrib import admin
from WER_app.models import Review, Page
from WER_app.models import UserProfile


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewID", "title")

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Review, ReviewAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
