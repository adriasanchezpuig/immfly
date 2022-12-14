from django.db import models

# Create your models here.
class Channel(models.Model):
    title = models.CharField(max_length=60)
    language = models.CharField(max_length=60)
    picture = models.BinaryField()
    parent_channel = models.ForeignKey('self', related_name='subchannels', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    file = models.BinaryField()
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    genere = models.CharField(max_length=60)
    rating = models.IntegerField()
    parent_channel = models.ForeignKey(Channel, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Group(models.Model):
    name = models.CharField(max_length=60)
    channels = models.ManyToManyField(Channel, related_name='channels', blank=True)

    def __str__(self):
        return self.name
