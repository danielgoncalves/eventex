from django.db import models
from django.shortcuts import resolve_url as r


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