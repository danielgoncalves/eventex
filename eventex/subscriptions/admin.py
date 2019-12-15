from django.contrib import admin
from django.utils.timezone import now

from .models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = (
            'name',
            'email',
            'phone',
            'cpf',
            'created_at',)
    list_display = (
            'name',
            'email',
            'phone',
            'cpf',
            'created_at',
            'subscribed_today',
            'paid',)
    list_filter = ('paid', 'created_at',)

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
