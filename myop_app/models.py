from django.db import models
from django.contrib.auth.models import User
from datetime import date
# from dateutil.relativedelta import relativedelta

# journey_point = [#complete/incomplete
# 'preop',
# 'preop_GotoClinic',
# 'preop_drug',
# 'reminder1',
# 'reminder2',
# 'op',
# 'op_cancelled',
# 'dead',
# 'dis_home',
# 'pod1',
# 'pod2'
# 'pod5'
# 'pod10'
# 'pod15'
# ]
# Create your models here.
class JourneyData(models.Model):
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_username = models.CharField(max_length=50, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    op_date = models.DateField(blank = True)
    op_name = models.CharField(max_length=50, blank = True)
    journey_point = models.CharField(max_length=100, blank = True, default="preop_incomplete")
    UnixTimeOfLastSync = models.CharField(max_length=100,default = "1", blank = True)


    #Alert boolean and Alert CharField
    IsAlertFromServToPt = models.BooleanField(default=False )
    AlertMsgFromServToPt = models.CharField(max_length=1000,blank = True)

    IsAlertFromPtToServ = models.BooleanField(default=False )
    AlertMsgFromPtToServ = models.CharField(max_length=1000,blank = True)

    is_Alert_toHosp = models.BooleanField(default=False )
    Alert_msg_toHosp = models.CharField(max_length=1000,blank = True)


    #patient demographic :Race,DOB, Age(calc),gender,Ht,Wt,SBP,DBP



    #planned post op location : [ds/ssw/sda/ip]



    #About Surgery ,anaesthesia , phyio and wound care video
    AboutOpSurgeryLinks = models.URLField(max_length=200, blank = True)
    AboutAnesLinks = models.URLField(max_length=200, blank = True)
    AboutPhysioLinks = models.URLField(max_length=200, blank = True)
    AboutWoundCareLinks = models.URLField(max_length=200, blank = True)

    #boolean outcomes
    is_OnlinePreopElig= models.BooleanField(default=False)
    is_PatientNoShow = models.BooleanField(default=False)
    is_OpCancelled = models.BooleanField(default=False)
    is_PostOpInpatient = models.BooleanField(default=False)
    is_PostOpReadmission = models.BooleanField(default=False)
    is_PostOpSti = models.BooleanField(default=False)
    is_PostOpDvt = models.BooleanField(default=False)
    is_PostOpUti = models.BooleanField(default=False)
    is_PostOpLrti = models.BooleanField(default=False)
    is_PostOpArf = models.BooleanField(default=False)
    is_PostOpComplication = models.BooleanField(default=False)

    #patient mobilization outcomes: Preop_Daily_distance, Postop_Daily_distance,ratio_preTopost(calc)
    isSick = models.BooleanField(default=False);


    #preop questions



    #preop drugs
    isOnMeds = models.BooleanField(default=False);
    def _upload_path(instance,filename):
        return instance.get_upload_path(filename)

    image = models.ImageField(upload_to=_upload_path, blank = True)

    def get_upload_path(self,filename):
        return str(self.patient_name)+"/"+str(self.created)+"/drugs/"+filename




    #Reminder1 questions with QOL




    #Reminder2 questions





    #pod1 questions
    pod1_satisfaction_score = models.IntegerField(default = -1)


    #pod2 questions


    #pod3 questions


    #pod5 questions


    #pod10 questions


    #pod15 questions with QOL
    pod15_satisfaction_score = models.IntegerField(default = -1)

    #Chat patient-Hospital
    MsgFromServToPt = models.CharField(max_length=1000,blank = True)
    MsgFromPtToServ = models.CharField(max_length=1000,blank = True)


    class Meta:
        get_latest_by = 'created'

    def __str__(self):
        return str(self.patient_name)


#logic to determine is online preop elig:
    @property
    def get_is_OnlinePreopElig(self):
        if(self.isSick):
            return False
        else:
            return True


# logic to get User.username
    @property
    def get_patient_username(self):
        return str(self.patient_name)

#logic to determine is post op other complication :
    # @property
    # def get_is_PostOpComplication(self):
    #     if(self.is_PostOpSti or self.is_PostOpDvt or self.is_PostOpUti or self.is_PostOpLrti ):
    #         return True
    #     else:
    #         return False

#logic to change journey point with args : time to op , previous journey point
    @property
    def get_days_to_op(self):
        now = date.today()
        delta = self.op_date - now
        return delta.days

    @property
    def get_days_after_op(self):
        now = date.today()
        delta = now - self.op_date
        return delta.days

    # def get_journey_point(self):
    #     if(self.is_OnlinePreopElig == True):
    #         if(self.isOnMeds == False):
    #             return "preop_complete"
    #         if(self.isOnMeds == True):
    #             if(self.image ==""):
    #                 return "preop_drug_incomplete"
    #             else:
    #                 return "preop_drug_complete"

    #     if(self.is_OnlinePreopElig == False ):
    #         return "preop_GotoClinic"


#         #7 days preop
#         if(self.days_to_op < 7 and self.journey_point == "preop_incomplete"):
#             #send alert to patient to book in-person appointment
#             #send alert to hospital to contact patient for appointment
#             pass
#         #4 days preop
#         if(self.days_to_op == 4  and (self.journey_point == "preop_complete" or self.journey_point != "reminder1_complete")):
#             return "reminder1_incomplete"

#         #3 days preop
#         if(self.days_to_op == 3 and self.journey_point != "reminder1_complete"):
#             #send alert to hospital to contact patient
#             pass

#         # 2 days preop
#         if(self.days_to_op == 2  and (self.journey_point == "reminder1_complete" or self.journey_point != "reminder2_complete")):
#             return "reminder2_incomplete"

#         # 1 day preop
#         if(self.days_to_op == 1  and (self.journey_point == "reminder2_complete" or self.journey_point != "op_incomplete")):
#             return "reminder2_incomplete"


#         # 1 day postop

#         # 2nd day postop

#         # 3rd day postop

#         # 5th day postop

#         # 10th day postop

#         else:
#             return "preop_incomplete"










    def save (self,*args,**kwargs):

    #     self.is_PostOpComplication =self.get_is_PostOpComplication
        self.is_OnlinePreopElig =self.get_is_OnlinePreopElig
        self.patient_username = self.get_patient_username
        # self.journey_point = self.get_journey_point

        super(JourneyData,self).save(*args,**kwargs)



#TODO: create new Model for Messages & Images from and to patients
    def _upload_path_msg(instance,filename):
        return instance.get_upload_path_msg(filename)

    msg_FromPatient = models.TextField(blank=True)
    msg_ToPatient = models.TextField(blank=True)

    msg_image = models.ImageField(upload_to=_upload_path_msg, blank = True)

    def get_upload_path_msg(self,filename):
        return str(self.patient_name)+"/"+str(self.created)+"/Msg/"+filename





