from rest_framework import serializers
from .models import JourneyData
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

        if(obj.is_OnlinePreopElig == True):
            if(obj.isOnMeds == False):
                return "preop_complete"
            if(obj.isOnMeds == True):
                if(obj.image ==""):
                    return "preop_drug_incomplete"
                else:
                    return "preop_drug_complete"

        else:
            return "preop_GotoClinic"



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
            'isSick',
            'isOnMeds',
            'is_OnlinePreopElig',
            'image',

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












