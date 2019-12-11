from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import SubscriptionForm
from .models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = {'form': form}
        return render(request, 'subscriptions/subscription_form.html', context)

    subscription = Subscription.objects.create(**form.cleaned_data)

    _send_mail(
            'Confirmação de inscrição',
            settings.DEFAULT_FROM_EMAIL,
            subscription.email,
            'subscriptions/subscription_email.txt',
            {'subscription': subscription})

    return HttpResponseRedirect('/inscricao/{}/'.format(subscription.hash_id))


def new(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)


def detail(request, hash_id):
    subscription = get_object_or_404(Subscription, hash_id=hash_id)
    context = {'subscription': subscription}
    template = 'subscriptions/subscription_detail.html'
    return render(request, template, context)


def _send_mail(subject, mail_from, mail_to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, mail_from, [mail_from, mail_to])
