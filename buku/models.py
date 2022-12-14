from django.db import models



class Category(models.Model):
   nama = models.CharField(max_length=40)
   def __str__(self):
      return self.nama
   
class Buku(models.Model):
   nama = models.CharField(max_length=50)
   deskripsi = models.TextField()
   jumlah = models.IntegerField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
   
   def __str__(self):
      return self.nama
   
   class meta :
      ordering = ['-id']
      verbose_name_plural = "Buku"
   
# Create your models here.
