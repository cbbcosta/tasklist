from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400, null=True)
    status = models.ForeignKey('SubCategory')
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()
#     owner = models.ForeignKey('User')
    
    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        db_table = 'tasklist_task'
        
    def __str__(self):
        return self.title
    

class Category (models.Model):
    description = models.CharField(max_length=140)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'tasklist_category'
        
    def __str__(self):
        return self.description


class SubCategory(models.Model):
    description = models.CharField(max_length=140)
    category = models.ForeignKey('Category')
    
    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'
        db_table = 'tasklist_subcategory'
    
    def __str__(self):
        return self.description