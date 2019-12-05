from api import models

from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    """
    课程序列化
    """
    level = serializers.CharField(source='get_level_display')
    class Meta:
        model = models.Course
        fields = ['id','title','course_img','level']


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    课程详细序列化
    """
    # one2one/fk/choice
    title = serializers.CharField(source='course.title')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')
    # 上面是自定义字段，后面的source是和哪一个表的哪一个字段进行绑定，
    # 这样下面的返回的字段就很多了，
    # 这就是可以实现跨表返回数据，
    # get_level_display这一句，可以实现不是只拿一个数字，而是数字代表的汉字，
    # 注意，一定把字段放到中间，


    # m2m
    recommends = serializers.SerializerMethodField()
    # SerializerMethodField，写了这个，需要在下面写一个函数，
    # 这是拿推荐课程，注意：这种多对多的不能使用source了，
    chapter = serializers.SerializerMethodField()
    # 这是拿章节，


    class Meta:
        model = models.CourseDetail
        fields = ['course','title','img','level','slogon','why','recommends','chapter']


    def get_recommends(self,obj):
        # 获取推荐的所有课程
        queryset = obj.recommend_courses.all()

        return [{'id':row.id,'title':row.title} for row in queryset]

    def get_chapter(self,obj):
        # 获取推荐的所有课程
        queryset = obj.course.chapter_set.all()

        return [{'id':row.id,'name':row.name} for row in queryset]
