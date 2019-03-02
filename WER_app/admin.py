from django.contrib import admin
from WER_app.models import Review, Page

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewID", "title")
    
    
admin.site.register(Review, ReviewAdmin)
admin.site.register(Page)