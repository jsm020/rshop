from django.db import models

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


class mahsulotReyting(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, related_name="reytinglar", on_delete=models.CASCADE)
    reytin = models.IntegerField()

    class Meta:
        verbose_name = "Mahsulot reytingi"
        verbose_name_plural = "Mahsulot reytingi"
    
    def __str__(self):
        return f"Reyting for {self.mahsulot.nomi}: {self.reytin}"
    

class ReviewProducts(models.Model):
    mahsulot_nomi = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    izoh = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.izoh