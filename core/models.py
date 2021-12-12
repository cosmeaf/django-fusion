import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created_at = models.DateField('Criado', auto_now_add=True)
    updated_at = models.DateField('Atualizado', auto_now=True)
    status = models.BooleanField('Status', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Cog'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    service = models.CharField('Serviços', max_length=100)
    description = models.TextField('Descrição', max_length=200)
    icon = models.CharField('Icone', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.service


class OfficePost(Base):
    office = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.office


class Staff(Base):
    name = models.CharField('Nome', max_length=100)
    office = models.ForeignKey('core.OfficePost', verbose_name='Empregado', on_delete=models.CASCADE)
    biography = models.TextField('Biography', max_length=200)
    image = StdImageField('Image', upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Empregado'
        verbose_name_plural = 'Empregados'

    def __str__(self):
        return self.name
