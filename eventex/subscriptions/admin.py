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

    actions = ['mark_as_paid']

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        if count == 1:
            msg = '{} inscrição foi marcada como paga'
        else:
            msg = '{} inscrições foram marcadas como pagas'
        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar como "Pago"'


admin.site.register(Subscription, SubscriptionModelAdmin)
