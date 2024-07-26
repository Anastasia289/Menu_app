from django.db import models
from django.urls import reverse

MAX_NAME_LENGTH = 100


class Menu(models.Model):
    """Основное меню"""

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        verbose_name='Название меню'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['name']

    def get_full_url(self):
        return reverse('draw_menu', kwargs={'path': self.name})


class MenuItem(models.Model):
    """Пункты меню."""
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Пункт меню',
        unique=True,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='От какого пункта спускается',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name='Меню',
        on_delete=models.CASCADE,
        related_name='menu',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['name']
