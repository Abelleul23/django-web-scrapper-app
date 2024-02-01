from django.db import models

class NewsSource(models.Model):
    name = models.CharField(max_length=100)
    #url = models.URLField(unique=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    #content = models.TextField()
    #publication_date = models.DateTimeField()
    #source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    url = models.URLField()
    image_src =  models.URLField(default='https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F929047972%2Fvector%2Fworld-news-flat-vector-icon-news-symbol-logo-illustration-business-concept-simple-flat.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3D5jpcJ7xejjFa2qKCzeOXKJGeUl7KZi9qoojZj1Kq_po%3D&tbnid=Cxjv8zVKBQfVpM&vet=1&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fnews-logo&docid=4TkW8YibVvooqM&w=612&h=612&source=sh%2Fx%2Fim%2Fm1%2F1&shem=uvafe2')
    def __str__(self):
        return self.title