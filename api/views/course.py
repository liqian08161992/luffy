from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
from api.serializers.course import CourseSerializer,CourseDetailSerializer
from rest_framework.throttling import SimpleRateThrottle
from api.auth.auth import LuffyAuth


class CourseView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'data':None}

        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}

        try:
            # 课程ID=2
            pk = kwargs.get('pk')

            # 课程详细对象
            obj = models.CourseDetail.objects.filter(course_id=pk).first()

            ser = CourseDetailSerializer(instance=obj,many=False)

            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

def test(request,*args,**kwargs):
    from django.shortcuts import HttpResponse
    obj = models.Course.objects.filter(id=2).first()
    print(obj.title)
    print(obj.level) #
    print(obj.get_level_display() ) #
    return HttpResponse('...')



class MicroView(APIView):
    authentication_classes = [LuffyAuth,]

    def get(self,request,*args,**kwargs):
        ret = {'code':1000,'title':'微职位'}
        return Response(ret)


#######################################


from django.shortcuts import render,HttpResponse
from django.contrib.contenttypes.models import ContentType

def test(request):
    # 1.在价格策略表中添加一条数据
    # models.PricePolicy.objects.create(
    #     valid_period=7,
    #     price=6.6,
    #     content_type=ContentType.objects.get(model='SubjectCourse'),
    #     object_id=1
    # )
    #这是第二种方式，
    # models.PricePolicy.objects.create(
    #     valid_period=14,
    #     price=9.9,
    #     content_object=models.Course.objects.get(id=1)
    # )

    # 2. 根据某个价格策略对象，找到他对应的表和数据，如：管理课程名称
    # price = models.PricePolicy.objects.get(id=2)
    # print(price.content_object.name) # 自动帮你找到

    # 3.找到某个课程关联的所有价格策略
    # obj = models.Course.objects.get(id=1)
    # for item in obj.policy_list.all():
    #     print(item.id,item.valid_period,item.price)
    #
    return HttpResponse('...')









