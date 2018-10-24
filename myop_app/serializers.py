from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import JourneyData
# from .algorithms import isElig
from django.core.files import File
import base64


class JourneyDataSerializer(serializers.ModelSerializer):
    # patient_name =serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = JourneyData
        fields = '__all__'

class PreopSerializer(serializers.ModelSerializer):
    journey_point = serializers.SerializerMethodField()



    def get_journey_point(self,obj):
        #Algorithm here
        # if(obj.is_OnlinePreopElig == True):#redflags
        # if(isElig() == True):
        # if(isElig):#using alogrithm.py
        if(isElig(120,79,70,24,getStopBang("F",obj.HasLoudSnore,obj.HasSleepApneaEpisodes,obj.HasDaySomno,obj.HasHtn,41),obj.HasAdeqMouthOpening,obj.HasAdeqNeckMov,obj.CanClimbStairs,obj.HasFeverInfec,obj.HasLooseTeeth,obj.IsPregnant,obj.HasSobAtRest,obj.HasHeartAttacks,obj.HasChestPain,obj.HasIrregHR,obj.HasDiabetes,obj.HasThyroidDs,obj.HasKidneyDs,obj.HasLiverDs,obj.HasStroke,obj.HasEpilepsy,obj.HasPsychDs,obj.HasBloodDs,obj.HasCtOrMsDs,obj.HasOsaOrRespDs) == True):
            if(obj.IsOnMeds == False):
                return "Reminder1"
            if(obj.IsOnMeds == True):
                if(obj.image ==""):
                    return "preopMedPhoto"
                else:
                    return "Reminder1Q"

        else:
            return "preop_GotoClinic"



    class Meta:
        model = JourneyData
        # fields = '__all__'

        fields = (
            'journey_point',
            'HasAdeqMouthOpening',
            'HasAdeqNeckMov',
            'CanClimbStairs',
            'HasFeverInfec',
            'HasLooseTeeth',
            'HasDentalImplant',
            'IsPregnant',
            'HasSobAtRest',
            'HasHeartAttacks',
            'HasChestPain',
            'HasIrregHR',
            'IsOnMeds',
            'HasHtn',
            'image',
            'HasDiabetes',
            'HasThyroidDs',
            'HasKidneyDs',
            'HasLiverDs',
            'HasGastricReflux',
            'HasStroke',
            'HasEpilepsy',
            'HasPsychDs',
            'HasBloodDs',
            'HasCtOrMsDs',
            'HasAllergies',
            'HasOsaOrRespDs',
            'HasLoudSnore',
            'HasDaySomno',
            'HasSleepApneaEpisodes',
            'IsSmoker',
            'IsAlcoholic',
            'IsOnTcm',
            'HasFHOAnesRxn',
            'HasPrevOps',
            'HasPONV',

            )

class ReminderOneSerializer(serializers.ModelSerializer):
    pass

class ReminderTwoSerializer(serializers.ModelSerializer):
    pass

class OperationSerializer(serializers.ModelSerializer):
    pass

class PodSerializer(serializers.ModelSerializer):
    pass

class SyncWithServerSerializer(serializers.ModelSerializer):
     class Meta:
        model = JourneyData
        fields = (
            'journey_point',
            'UnixTimeOfLastSync',
            'op_date',
            'op_name',
            'AboutOpSurgeryLinks',
            'AboutAnesLinks',
            'AboutPhysioLinks',
            'AboutWoundCareLinks',
            'IsAlertFromServToPt',
            'AlertMsgFromServToPt',
            'MsgFromServToPt',
            'IsAlertFromPtToServ',
            'AlertMsgFromPtToServ',


            )


class ImageSerializer(serializers.ModelSerializer):
    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = JourneyData
        fields = ('base64_image',)


    def get_base64_image(self,obj):
         f= open(obj.image.path,'rb')
         img = File(f)
         data = base64.b64encode(img.read())
         f.close()
         return data

class PutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JourneyData
        fields = ('image',)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        username = data.get('username','')
        password = data.get('password','')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data["user"] = user
            else:
               raise exceptions.ValidationError("does not exist UN and PW")
        else:
            raise exceptions.ValidationError("provide UN and PW")

        return data


# #Algorithm to assess eligibility for online assessment
def isElig(SBP,DBP,HR,BMI,getStopBang,HasAdeqMouthOpening,HasAdeqNeckMov,
CanClimbStairs,HasFeverInfec,HasLooseTeeth,IsPregnant,HasSobAtRest,HasHeartAttacks,
HasChestPain,HasIrregHR,HasDiabetes,HasThyroidDs,HasKidneyDs,HasLiverDs,HasStroke,
HasEpilepsy,HasPsychDs,HasBloodDs,HasCtOrMsDs,HasOsaOrRespDs):
    if(SBP>140 or DBP>89 or HR<50 or HR>100 or BMI>34 or
    getStopBang > 3 or HasAdeqMouthOpening == False or HasAdeqNeckMov == False
    or CanClimbStairs == False or HasFeverInfec == True or HasLooseTeeth == True
    or IsPregnant == True or HasSobAtRest == True or HasHeartAttacks == True
    or HasChestPain == True or HasIrregHR == True or HasDiabetes == True
    or HasThyroidDs == True or HasKidneyDs == True or HasLiverDs == True
    or HasStroke == True or HasEpilepsy == True or HasPsychDs == True
    or HasBloodDs == True or HasCtOrMsDs == True or HasOsaOrRespDs == True):
        return False
    else:
        return True

    #isElig is False if:
    #SBP>140, DBP>89, HR<50 or >100 , BMI>34: TODO values from webapp
    #Redflags :
    #   getStopBang > 3
    #   !HasAdeqMouthOpening
    #   !HasAdeqNeckMov
    #   !CanClimbStairs
    #   HasFeverInfec
    #   HasLooseTeeth
    #   IsPregnant
    #   HasSobAtRest
    #   HasHeartAttacks
    #   HasChestPain
    #   HasIrregHR
    #   HasDiabetes
    #   HasThyroidDs
    #   HasKidneyDs
    #   HasLiverDs
    #   HasStroke
    #   HasEpilepsy
    #   HasPsychDs
    #   HasBloodDs
    #   HasCtOrMsDs
    #   HasOsaOrRespDs


def getStopBang(Gender,HasLoudSnore,HasSleepApneaEpisodes,HasDaySomno,HasHtn,Age):
    score = 0
    if(Gender == "F"):
        score = score + 1
    if(HasLoudSnore == True):
        score = score + 1
    if(HasSleepApneaEpisodes ==True):
        score = score + 1
    if(HasDaySomno == True):
        score = score + 1
    if(HasHtn == True):
        score = score + 1
    if(Age > 50):
        score = score + 1

    return score








