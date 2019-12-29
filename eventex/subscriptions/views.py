from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import resolve_url as r
from django.template.loader import render_to_string

from .forms import SubscriptionForm
from .models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = {'form': form}
        return render(request, 'subscriptions/subscription_form.html', context)

    subscription = form.save()

    _send_mail(
            'Confirmação de inscrição',
            settings.DEFAULT_FROM_EMAIL,
            subscription.email,
            'subscriptions/subscription_email.txt',
            {'subscription': subscription})

    url = r('subscriptions:detail', subscription.hash_id)
    return HttpResponseRedirect(url)


def detail(request, hash_id):
    subscription = get_object_or_404(Subscription, hash_id=hash_id)
    context = {'subscription': subscription}
    template = 'subscriptions/subscription_detail.html'
    return render(request, template, context)


def _send_mail(subject, mail_from, mail_to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, mail_from, [mail_from, mail_to])
