from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models import Count
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)
    # price = models.IntegerField()
    like = models.PositiveIntegerField(default=0)
    search = models.IntegerField(default=0)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )

    # Star 모델과의 관계 설정
    # star = models.OneToOneField('StarLike', on_delete=models.CASCADE, related_name='articles')
    # Star 모델과의 관계 설정
    # star = models.ForeignKey('Star', on_delete=models.CASCADE, related_name='articles')

    @classmethod
    def get_articles_with_comments(cls):
        return cls.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')

    def __str__(self):
        return self.title

    def time_dif(self):
        difftotal = timezone.now()-self.created_at
        day = difftotal.days
        second = difftotal.seconds
        if day > 0:
            if day < 7:
                print(day)
                return f'{day}일 전'
            elif day < 30:
                return f'{day//7}주 전'
            elif day < 365:
                return f'{day//30}달 전'
            else:
                return f'{day//365}년 전'
        elif second > 3599:
            return f'{second//3600}시간 전'
        elif second > 59:
            return f'{second//60}분 전'
        else:
            return f'{second}초 전'


@receiver(m2m_changed, sender=Article.like_users.through)
def update_like_count(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.like = instance.like_users.count()
        instance.save()

# @receiver(m2m_changed, sender=Article.like_users.through)
# def update_star_like_count(sender, instance, action, **kwargs):
#     if action in ['post_add', 'post_remove', 'post_clear']:
#         # 연결된 Star 인스턴스 가져오기
#         star = instance.star

#         # like_users 수를 Star의 like 필드에 반영
#         if star:
#             star.like = instance.like_users.count()
#             star.save()


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updaetd_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
