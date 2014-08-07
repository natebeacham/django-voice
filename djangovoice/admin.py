from django.contrib import admin
from djangovoice.models import Feedback, Status, Type


class SlugFieldAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class FeedbackAdmin(admin.ModelAdmin):
    list_display = [
        '__unicode__', 'type', 'status', 'duplicate', 'anonymous', 'private',
        'user', 'email']
    list_filter = ['type', 'status', 'anonymous', 'private']
    list_editable = ['type', 'status', 'anonymous', 'private']
    raw_id_fields = ['user', 'duplicate']

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register([Status, Type], SlugFieldAdmin)
