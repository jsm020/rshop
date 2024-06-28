import os
from django.db import models
from members.models import CustomUser
from PIL import Image
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Kategoriya(models.Model):
    nomi = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriya"
    
    def __str__(self):
        return self.nomi
class Mahsulot(models.Model):
    kategoriya = models.ForeignKey(Kategoriya, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulot"
    
    def __str__(self):
        return self.nomi

class mahsulotRasmlari(models.Model):
    nomi = models.ForeignKey(Mahsulot, related_name="Mahsulot", on_delete=models.CASCADE)
    rasmi = models.ImageField(upload_to='Mahsulot/')

    class Meta:
        verbose_name = "Mahsulot rasmlari"
        verbose_name_plural = "Mahsulot rasmlari"


    def save(self, *args, **kwargs):
        super(mahsulotRasmlari, self).save(*args, **kwargs)

        img = Image.open(self.rasmi.path)
        
        if img.height != 300 or img.width != 300:
            output_size = (300, 300)
            img = img.resize(output_size, Image.Resampling.LANCZOS)
            img.save(self.rasmi.path)

@receiver(post_delete, sender=mahsulotRasmlari)
def delete_image_files(sender, instance, **kwargs):
    if instance.rasmi:
        if os.path.isfile(instance.rasmi.path):
            os.remove(instance.rasmi.path)

class ReviewProducts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    mahsulot_nomi = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    izoh = models.CharField(max_length=250)
    time  = models.DateField(auto_now=True)
    reyting = models.PositiveIntegerField(default=0)  # Rating out of 5
    def __str__(self):
        return f"{self.izoh} - {self.reyting} stars"
    

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.nomi}"

    def total_price(self):
        return self.quantity * self.product.narxi