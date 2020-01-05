from django.db import models


class KindQuerySet(models.QuerySet):

    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)


class PeriodManager(models.Manager):

    MIDDAY = '12:00'

    def at_morning(self):
        qs = super().get_queryset()
        qs = self.filter(start__lt=self.MIDDAY)
        return qs

    def at_afternoon(self):
        qs = super().get_queryset()
        qs = self.filter(start__gte=self.MIDDAY)
        return qs
