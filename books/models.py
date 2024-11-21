from django.db import models 

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pdfLink = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)
    publicationDate = models.DateField()
    coverImage = models.ImageField(upload_to='covers/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    download_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'book')
        
    def __str__(self):
        return (self.book.title )
    
    def get_object(self, queryset=None):
        book_pk = self.kwargs.get('pk')
        return Favorite.objects.get(book_id=book_pk, user=self.request.user)


