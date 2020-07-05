from django.db import models


# Create your models here.
class commands(models.Model):
    title = models.CharField('Command title', max_length=300)
    command = models.CharField('command', max_length=2000)
    describe = models.CharField('Command description', max_length=300)
    created_time = models.DateTimeField('Creation time', auto_now_add=True)
    last_mod_time = models.DateTimeField('Modified', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'command'
        verbose_name_plural = verbose_name


class EmailSendLog(models.Model):
    emailto = models.CharField('Recipient', max_length=300)
    title = models.CharField('Mail title', max_length=2000)
    content = models.TextField('Email Content')
    send_result = models.BooleanField('Result', default=False)
    created_time = models.DateTimeField('Time Created', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Email log'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
