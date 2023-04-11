from django.db import models
from django.urls import reverse


# Create your models here.
# Меню
class Menu(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("activate_menu", args=(self.slug, ))

    class Meta:
        verbose_name = 'Заголовок меню'
        verbose_name_plural = 'Заголовки меню'


# Содержимое меню
class MenuItem(models.Model):
    item_title = models.CharField(max_length=50)
    item_slug = models.SlugField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    def get_absolute_url(self):
        return reverse("activate_menu", args=(self.item_slug, ))

    def __str__(self):
        return self.item_title

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
