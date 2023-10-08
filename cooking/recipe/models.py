from django.db import models
from users.models import Profile


class Recipe(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    data_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    steps = models.TextField(max_length=2000, blank=True, null=True)
    ingredients = models.TextField(max_length=2000, blank=True, null=True)
    tags = models.ManyToManyField('Tags', blank=True)
    like = models.PositiveIntegerField(default=0, blank=True)
    mark = models.PositiveIntegerField(default=0, blank=True)
    main_image = models.ImageField(upload_to='recipe/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-like', '-mark']

    def commentator(self):
        queryset = self.comment_set.all().values_list('owner__id', flat=True)
        return queryset

    def get_vote_count(self):
        com = self.comment_set.all()
        up = com.filter(value='up').count()

        self.like = up

        self.save()

    def get_mark_count(self, recipe):
        total_marks = Comment.objects.filter(recipe_id=recipe).count()
        five = Comment.objects.filter(mark='5', recipe_id=recipe).count()
        four = Comment.objects.filter(mark='4', recipe_id=recipe).count()
        three = Comment.objects.filter(mark='3', recipe_id=recipe).count()
        two = Comment.objects.filter(mark='2', recipe_id=recipe).count()
        one = Comment.objects.filter(mark='1', recipe_id=recipe).count()

        self.mark = int(5 * five + 4 * four + 3 * three + 2 * two + one)/int(total_marks)

        self.save()


class Tags(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    VOTE_TYPE = (
        ('up', 'Нравится'),
        ('down', 'Не нравится'),
    )
    MARK_TYPE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, blank=True, null=True)
    value = models.CharField(max_length=100, choices=VOTE_TYPE)
    mark = models.CharField(max_length=100, choices=MARK_TYPE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['owner', 'recipe']]
