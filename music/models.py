from django.contrib.auth.models import User
from django.db import models
import barcode as brcode
from io import BytesIO
from io import StringIO
# import sengo
from django.core.files.uploadedfile import InMemoryUploadedFile
from barcode.writer import ImageWriter


class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=None)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


class product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    review = models.ForeignKey('feedback', on_delete=models.SET_DEFAULT, null=True, default="NA")

    def __str__(self):
        return self.title


class feedback(models.Model):
    SCORE_CHOICES = zip(range(6), range(6))
    user = models.CharField(max_length=50, null=True, default='anonymous user')
    item = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    rating = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, blank=False)

    def __str__(self):
        return 'Rating(Item =' + str(self.item) + ', Stars =' + str(self.rating) + ')'


class barcode(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    code = models.IntegerField(blank=True,null=True)
    qrcode = models.ImageField(upload_to='static', blank=True, null=True)


    def save(self, *args, **kwargs):
        super(barcode, self).save(*args, **kwargs)
        if not self.qrcode:
            ean = brcode.get('ean13', self.title, writer=ImageWriter())
            buffer = ByteIO()
            ean.write(buffer)
            filename = 'bar%a.jpg' % self.id
            filebuffer = InMemoryUploadedFile(buffer, None, filename, 'image/png', buffer.__sizeof__(), None)
            self.qrcode.save(filename, filebuffer)
