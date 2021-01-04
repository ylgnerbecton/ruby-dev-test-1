from django.db import models
from model_utils.models import SoftDeletableModel


class BestPraticesModel(SoftDeletableModel):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SubPath(BestPraticesModel):
    sub_path = models.CharField(verbose_name="Caminho", max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Sub Diretórios"

    def __str__(self):
        return "{}".format(self.sub_path)


class Directories(BestPraticesModel):
    path = models.CharField(verbose_name="Caminho", max_length=254, null=True, blank=True)
    sub_path = models.ForeignKey(SubPath, on_delete=models.DO_NOTHING, verbose_name="Sub Diretório", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Diretórios"

    def __str__(self):
        return "{}".format(self.path)


class Files(BestPraticesModel):
    name = models.CharField(verbose_name="Nome", max_length=254, null=True, blank=True)
    directory = models.ForeignKey(Directories, on_delete=models.DO_NOTHING, verbose_name="Diretório", blank=True, null=True)
    upload = models.FileField(verbose_name="Arquivo", upload_to='', max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Arquivos"

    def __str__(self):
        return "{}".format(self.name)
