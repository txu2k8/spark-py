from django.db import models


# Create your models here.
class IndexValuation(models.Model):
    """Index Valuation Table model"""
    title = models.CharField(max_length=30, verbose_name='标题')
    url = models.CharField(max_length=100, verbose_name='网址')
    content = models.CharField(max_length=200, verbose_name='内容')
    pub_date = models.DateTimeField('Time', verbose_name='时间')  # publish date

    class Meta:
        verbose_name_plural = '爬虫银行螺丝钉'

    def __str__(self):
        return self.title

