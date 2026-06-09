from django.db import models

class Record(models.Model):
    create_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=14)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)


    class Meta:
        ordering = ['-id']
        verbose_name= 'record'
        verbose_name_plural= 'records'

    def __str__(self):
        return(f'{self.first_name} {self.last_name}')
