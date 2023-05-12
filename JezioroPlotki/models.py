from django.db import models
from ckeditor.fields import RichTextField


class Link(models.Model):
    title = models.CharField(max_length=50)
    link = models.TextField()

    def str(self):
        return self.title

    def get_absolute_url(self):
        return self.link


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    categoryChoices = (
        ('Strona-Glowna', 'Strona Główna'),
        ('Informacje', 'Informacje'),
        ('Hydrobiologia', 'Hydrobiologia'),
        ('Obszar-Natura-2000', 'Obszar Natura 2000'),
        ('Hydrologia-Jeziora', 'Hydrologia Jeziora'),
    )

    category = models.CharField(
        max_length=256,
        choices=categoryChoices,
        default='Index',
    )

    image = models.ImageField(upload_to='articles')

    def __str__(self):
        return self.title


class Temperature(models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    edit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        p = str(self.edit_date.strftime('%Y-%m-%d %H:%M'))
        l = str(self.temperature)
        return (p + " ; " + l + "\N{DEGREE SIGN}C")
