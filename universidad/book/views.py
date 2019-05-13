from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Video
from .serializer import VideoSerializer
from django.http import Http404

# Create your views here.


def home(request):
    return HttpResponse('Hola mundo')


class ListVideo(APIView):

    def get(self, request):
        video = Video.objects.all()
        video_json = VideoSerializer(video, many=True)
        return Response(video_json.data)

    def post(self, request):
        video_jeson = VideoSerializer(data=request.data)
        if(video_jeson.is_valid()):
            video_jeson.save()
            return Response(video_jeson.data, status=201)
        else:
            return Response(video_jeson.errors, status=400)


class DetailVideo(APIView):
    def get_object(self, id):
        try: 
            return Video.objects.get(id=id)
        except Video.DoesNotExist:
            raise Http404("No existe atributo")

    def get(self, request, id):
        video = self.get_object(id)
        video_json = VideoSerializer(video)
        return Response({
            "ok": True,
            "message": video_json.data
        })

    def put(self, request, id):
        video = self.get_object(id)
        video_json = VideoSerializer(video, request.data)
        if(video_json.is_valid()):
            video_json.save()
            return Response(video_json.data, status=201)
        else:
            return Response(video_json.errors, status=400)

    def delete(self, request, id):
        video = self.get_object(id)
        video.delete()
        return Response(status=204)
