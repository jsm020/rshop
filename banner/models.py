# models.py
from django.utils.html import format_html
from django.db import models

class SliderRasm(models.Model):
    img = models.ImageField(upload_to='Slider/')
    text = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Slider uchun rasm"
        verbose_name_plural = "Slider uchun rasm"

    def __str__(self):
        return f"Slider Image {self.id}"


class CategoryRasm(models.Model):
    img = models.ImageField(upload_to='Category/')
    text = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Category uchun rasm"
        verbose_name_plural = "Category uchun rasm"

    def __str__(self):
        return f"Category Image {self.id}"


class LogoRasmlar(models.Model):
    img_link = models.URLField()

    class Meta:
        verbose_name = "Logo linklari"
        verbose_name_plural = "Logo linklari"

    def __str__(self):
        return f"Image {self.id}"

    def img_link_display(self):
        return format_html('<a href="{}" target="_blank">{}</a>', self.img_link, self.img_link)

    img_link_display.short_description = 'Image Link'
