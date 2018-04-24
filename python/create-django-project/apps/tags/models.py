from django.db import models

# Create your models here.


class Tag(models.Model):
    """
    标签Model
    """
    tag = models.SlugField(verbose_name="Tag", max_length=40, db_index=True)
    name = models.CharField(verbose_name="标签", max_length=40)
    description = models.CharField(verbose_name="描述", max_length=256, blank=True,
                                   null=True)
    is_deleted = models.BooleanField(verbose_name="删除", default=False, blank=True)

    def __str__(self):
        return self.tag

    def __del__(self):
        self.is_deleted = True
        self.save()

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
        ordering = ("id",)


class TagValue(models.Model):
    """
    标签值Model
    """
    tag = models.ForeignKey(to=Tag, verbose_name="标签", on_delete=models.CASCADE)
    value = models.CharField(verbose_name="值", max_length=128)

    def __str__(self):
        return "{}:{}".format(self.tag.tag, self.value)

    class Meta:
        verbose_name = "标签值"
        verbose_name_plural = verbose_name
        unique_together = ("tag", "value")


class ObjectTag(models.Model):
    """
    对象的标签 Model
    """
    tag = models.ForeignKey(verbose_name="标签", to=Tag, on_delete=models.CASCADE)
    app_label = models.CharField(verbose_name="App", max_length=40)
    model = models.CharField(verbose_name="Model", max_length=40)
    object_id = models.IntegerField(verbose_name="对象ID")

    def __str__(self):
        return "{}_{}".format(self.model, self.tag.tag)

    class Meta:
        verbose_name = "对象标签"
        verbose_name_plural = verbose_name
