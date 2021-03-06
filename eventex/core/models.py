from django.db import models
from django.shortcuts import resolve_url as r

from .managers import KindQuerySet
from .managers import PeriodManager


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField()
    website = models.URLField(blank=True)
    photo = models.URLField('foto')
    bio = models.TextField('biografia', blank=True)

    class Meta:
        verbose_name = 'palestrante'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
            (EMAIL, 'Email'),
            (PHONE, 'Telefone'),
        )

    speaker = models.ForeignKey(
            'Speaker',
            on_delete=models.CASCADE,
            verbose_name='palestrante'
        )
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'Contato'

    def __str__(self):
        return self.value


class Talk(models.Model):
    title = models.CharField('título', max_length=200)
    start = models.TimeField('início', null=True, blank=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField(
            'Speaker',
            blank=True,
            verbose_name='palestrantes')

    objects = PeriodManager()

    class Meta:
        verbose_name = 'palestra'

    def __str__(self):
        return self.title
