from django.db import models


class Link(models.Model):
    title = models.CharField(max_length=50)
    link = models.TextField()

    def str(self):
        return self.title

    def get_absolute_url(self):
        return self.link


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1024)
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

# article = Article(title='Zarybianie jeziora',content='W zeszłym tygodniu przeprowadziliśmy zarybianie jeziora rybami z gatunku sandacza i szczupaka. Liczymy, że w ciągu kilku lat populacja ryb w jeziorze znacznie się zwiększy.',pub_date='2022-05-01 10:30:00',image='HydrobiologyPage_1.jpg',category='hydrobiologia')
# article.save()