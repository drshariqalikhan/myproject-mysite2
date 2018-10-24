from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from .models import JourneyData
from .serializers import JourneyDataSerializer,PreopSerializer,ImageSerializer,PutImageSerializer,SyncWithServerSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from myop_app.forms import RegistrationFrom,JourneyDataFrom
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login
from rest_framework.authtoken.models import Token


######APP FUNCTION VIEWS HERE###############################
@login_required
def index(request):
    return render (request, 'myop_app/index.html')

@login_required
def alert(request):
    return render (request, 'myop_app/alert.html')


@login_required
def register(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/dash/')
    else:
        form = RegistrationFrom()
        args = {'form': form}
        return render(request,'myop_app/reg_form.html', args)

def home(request):
    return render (request, 'myop_app/login.html')

@login_required
def add_jd(request):
    if request.method == "POST":
        form = JourneyDataFrom(request.POST)
        if form.is_valid():
            jd_item = form.save(commit = False)
            jd_item.save()
            return redirect('/api/dash/')

    else:
        form = JourneyDataFrom()
    return render(request,'myop_app/jd_form.html',{'form':form})

@login_required
def edit_jd(request, id= None):
    item = get_object_or_404(JourneyData, id=id)
    form = JourneyDataFrom(request.POST or None, instance = item)
    if form.is_valid():
        form.save()
        return redirect('/api/dash/')
    return render(request,'myop_app/jd_form.html',{'form':form})
















#API Class VIEWS HERE#######################################
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request,user)
        token, created = Token.objects.get_or_create(user= user)
        return Response({"token":token.key}, status = 200)





class GetUpClassView(APIView):

    def post(self, request, format=None):
        # snippets = JourneyData.objects.all()
        snippets = JourneyData.objects.all().filter(patient_username=self.request.user).order_by('-created')[:1]
        # snippets = JourneyData.objects.get().filter(patient_name=self.request.user)
        # serializer = JourneyDataSerializer(snippets, many=True)
        serializer = SyncWithServerSerializer(snippets, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        snippets = JourneyData.objects.all().filter(patient_username=self.request.user).latest()
        serializer = SyncWithServerSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,200)
        return Response(serializer.errors, 400)

    def patch(self, request, format=None):
        snippets = JourneyData.objects.all().filter(patient_username=self.request.user).latest()
        serializer = SyncWithServerSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,200)
        return Response(serializer.errors, 400)

class PreopClassView(APIView):
     def put(self, request, format=None):
        snippets = JourneyData.objects.all().filter(patient_username=self.request.user).latest()
        serializer = PreopSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['journey_point'],200)
            # return Response(serializer.data,200)

        return Response(serializer.errors, 400)



class MedPicClassView(APIView):

    def post(self, request, format=None):
        filename = JourneyData.objects.all().filter(patient_username=self.request.user).order_by('-created')[:1]
        serializer = ImageSerializer(filename, many=True)
        return Response(serializer.data)

    def put(self,request, format=None):
        snippets = JourneyData.objects.all().filter(patient_username=self.request.user).latest()
        serializer = PutImageSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response([{'saved':'done',}],200)
        return Response(serializer.errors, 400)


class DashView(APIView):

    def post(self, request, format=None):
        # snippets = JourneyData.objects.all()
        snippets = JourneyData.objects.all().order_by('-created')
        # snippets = JourneyData.objects.get().filter(IsActiveSession = "True").order_by('-created')
        # serializer = JourneyDataSerializer(snippets, many=True)
        serializer = JourneyDataSerializer(snippets, many=True)
        return Response(serializer.data)

