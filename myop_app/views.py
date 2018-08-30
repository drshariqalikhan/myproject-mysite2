from django.shortcuts import get_object_or_404, render
from .models import JourneyData
from .serializers import JourneyDataSerializer,PreopSerializer,ImageSerializer,PutImageSerializer,SyncWithServerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from myop_app.forms import RegistrationFrom
class GetUpClassView(APIView):

    def post(self, request, format=None):
        # snippets = JourneyData.objects.all()
        snippets = JourneyData.objects.all().filter(patient_name=self.request.user).order_by('-created')[:1]
        # snippets = JourneyData.objects.get().filter(patient_name=self.request.user)
        # serializer = JourneyDataSerializer(snippets, many=True)
        serializer = SyncWithServerSerializer(snippets, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        snippets = JourneyData.objects.all().filter(patient_name=self.request.user).latest()
        serializer = SyncWithServerSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,200)
        return Response(serializer.errors, 400)

    def patch(self, request, format=None):
        snippets = JourneyData.objects.all().filter(patient_name=self.request.user).latest()
        serializer = SyncWithServerSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,200)
        return Response(serializer.errors, 400)

class PreopClassView(APIView):
     def put(self, request, format=None):
        snippets = JourneyData.objects.all().filter(patient_name=self.request.user).latest()
        serializer = PreopSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,200)
        return Response(serializer.errors, 400)



class MedPicClassView(APIView):

    def post(self, request, format=None):
        filename = JourneyData.objects.all().filter(patient_name=self.request.user).order_by('-created')[:1]
        serializer = ImageSerializer(filename, many=True)
        return Response(serializer.data)

    def put(self,request, format=None):
        snippets = JourneyData.objects.all().filter(patient_name=self.request.user).latest()
        serializer = PutImageSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response([{'saved':'done',}],200)
        return Response(serializer.errors, 400)


class DashView(APIView):

    def post(self, request, format=None):
        # snippets = JourneyData.objects.all()
        snippets = JourneyData.objects.all().order_by('-created')
        # snippets = JourneyData.objects.get().filter(patient_name=self.request.user)
        # serializer = JourneyDataSerializer(snippets, many=True)
        serializer = JourneyDataSerializer(snippets, many=True)
        return Response(serializer.data)


def index(request):
    # return HttpResponse("Hello, world")
    return render (request, 'myop_app/index.html')


def register(request):
    if request.method =='POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myop_app/index.html')
        else:
            form = RegistrationFrom()
            args ={'form':form}
            return render(request, '/myop_app/reg_form.html', args)

