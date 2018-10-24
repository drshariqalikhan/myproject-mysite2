from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.timezone import now
# from dateutil.relativedelta import relativedelta

#
#preop-(preopMedPhoto)-->Reminder1--->Reminder2--->UnkwnOpStatus--->POD1--->POD3---->POD5--->POD10--->POD15-->X


# DAYS_to_OP:
# >8(12)--------------------10-------------------------9--------------------------5-----------------3---------------------0----------------------------------------------------------1--2-------3----4------5--6-7-8-9-10--11-12-13-14-15----X
# <----preop------11><---------preopMedPhoto----------9>                         <5--Rem1--4>      <3--Rem2--2>                                        <1pm--UnkwnOpStatus-----5pm> <R>       <R>         <R>         <R>             <R>
#                                                                         UNFIT_OPCancel
#                 preop GotoClinic---------------------------------------<               PT_OPCancel/UNFIT_OPCancel
# preop----------<                      /---------------------------------->Reminder1----<                 |
#                 preop ok-<-----------<                                  /               \-----Reminder2--<                     PT_OPCancel/UNFIT_OPCancel
#                           preopMedPhoto -------------------------------/                                  \---UnkwnOpStatus--<                               PostOpHome------->  POD1------->POD3------->POD5------->POD10------->POD15--->X
#                                                                                                                               \-----------------------------<              |             |           |            |           |
#                                                                                                                                                       |      PosyOpHosp-------------------------------------------------------------------->X
#                                                                                                                                                      DEAD

# JOURNEY POINTS:

# preop<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# preop_GotoClinic
# preop_ok
# preopMedPhoto<<<<<<<<<<<<<<<<<<<<<
# UNFIT_OPCancel
# PT_OPCancel
# DEAD
# Reminder1<<<<<<<<<<<<<<<<<<<<<<<<
# Reminder2<<<<<<<<<<<<<<<<<<<<<<<<
# UnkwnOpStatus<<<<<<<<<<<<<<<<<<<<reminder to staff
# POD1<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# POD3<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# POD5<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# POD10<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# POD15<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# Create your models here.
class JourneyData(models.Model):
    PREOP = 'preop'
    PREOP_GOTOCLINIC = 'preop_GotoClinic'
    PREOPMEDPHOTO = 'preopMedPhoto'
    REMINDER1 = 'Reminder1'
    REMINDER2 = 'Reminder2'
    UNKNOWNOPSTATUS = 'UnkwnOpStatus'
    POD1 = 'POD1'
    POD3 = 'POD3'
    POD5 = 'POD5'
    POD10 = 'POD10'
    POD15 = 'POD15'
    SUPERSYNC = 'SuperSync'
    DEAD = 'DEAD'

    JOURNEY_PT = (
        (PREOP, 'preop'),
        (PREOP_GOTOCLINIC, 'preop_GotoClinic'),
        (PREOPMEDPHOTO, 'preopMedPhoto'),
        (REMINDER1, 'Reminder1'),
        (REMINDER2, 'Reminder2'),
        (UNKNOWNOPSTATUS, 'UnkwnOpStatus'),
        (POD1, 'POD1'),
        (POD3, 'POD3'),
        (POD5, 'POD5'),
        (POD10, 'POD10'),
        (POD15, 'POD15'),
        (SUPERSYNC, 'SuperSync'),
        (DEAD, 'DEAD'),
    )
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_username = models.CharField(max_length=50, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    op_date = models.DateField(blank = True)
    op_name = models.CharField(max_length=50, blank = True)
    journey_point = models.CharField(max_length=100, blank = True, choices=JOURNEY_PT,default=PREOP)
    UnixTimeOfLastSync = models.IntegerField(default = 1, blank = True)
    IsActiveSession =  models.BooleanField(default=False )

    FCM = models.CharField(max_length=100, blank = True)


    #Alert boolean and Alert CharField
    IsAlertFromServToPt = models.BooleanField(default=False )
    AlertMsgFromServToPt = models.CharField(max_length=1000,blank = True)

    IsAlertFromPtToServ = models.BooleanField(default=False )
    AlertMsgFromPtToServ = models.CharField(max_length=1000,blank = True)

    is_Alert_toHosp = models.BooleanField(default=False )
    Alert_msg_toHosp = models.CharField(max_length=1000,blank = True)


    #patient demographic :Race,DOB, Age(calc),gender,Ht,Wt,SBP,DBP
    patient_firstname = models.CharField(max_length=50, blank = True)
    patient_lastname = models.CharField(max_length=50, blank = True)
    patient_mobile_number = models.IntegerField(default = 0, blank = True)
    race = models.CharField(max_length=50, blank = True)
    gender = models.CharField(max_length=10, blank = True)
    date_of_birth = models.DateField(default=now, blank = True)
    age_at_op = models.IntegerField(default=0, blank = True)
    height = models.IntegerField(default=0, blank = True)
    weight_at_op = models.IntegerField(default= 0, blank = True)
    sbp_at_op = models.IntegerField(default=0,blank = True)
    dbp_at_op =models.IntegerField(default=0,blank = True)
    heartrate_at_op = models.IntegerField(default=0,blank = True)



    #planned post op location : [ds/ssw/sda/ip]
    planned_postop_location = models.CharField(max_length=10, blank = True)




    #About Surgery ,anaesthesia , phyio and wound care video
    SurgeryVideoLink = models.URLField(max_length=200, blank = True)
    AnesthVideoLink = models.URLField(max_length=200, blank = True)
    PhysioVideoLink = models.URLField(max_length=200, blank = True)
    WoundCareVideoLink = models.URLField(max_length=200, blank = True)

    #About Surgery ,anaesthesia , phyio and wound care reading material
    AboutOpSurgeryLinks = models.TextField(blank=True, null=True)
    AboutAnesLinks = models.TextField(blank=True, null=True)
    AboutPhysioLinks = models.TextField(blank=True, null=True)
    AboutWoundCareLinks = models.TextField(blank=True, null=True)


    #preop instructions
    PreopInstructions = models.TextField(blank=True, null=True)


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
    HasAdeqMouthOpening = models.BooleanField(default=False)
    HasAdeqNeckMov = models.BooleanField(default=False)
    CanClimbStairs = models.BooleanField(default=False)
    HasFeverInfec = models.BooleanField(default=False)
    HasLooseTeeth = models.BooleanField(default=False)
    HasDentalImplant = models.BooleanField(default=False)
    IsPregnant = models.BooleanField(default=False)
    HasSobAtRest = models.BooleanField(default=False)
    HasHeartAttacks = models.BooleanField(default=False)
    HasChestPain = models.BooleanField(default=False)
    HasIrregHR = models.BooleanField(default=False)
    HasHtn = models.BooleanField(default=False)
    HasDiabetes = models.BooleanField(default=False)
    HasThyroidDs = models.BooleanField(default=False)
    HasKidneyDs = models.BooleanField(default=False)
    HasLiverDs = models.BooleanField(default=False)
    HasGastricReflux = models.BooleanField(default=False)
    HasStroke = models.BooleanField(default=False)
    HasEpilepsy = models.BooleanField(default=False)
    HasPsychDs = models.BooleanField(default=False)
    HasBloodDs = models.BooleanField(default=False)
    HasCtOrMsDs = models.BooleanField(default=False)
    HasAllergies = models.BooleanField(default=False)
    HasOsaOrRespDs = models.BooleanField(default=False)
    HasLoudSnore = models.BooleanField(default=False)
    HasDaySomno = models.BooleanField(default=False)
    HasSleepApneaEpisodes = models.BooleanField(default=False)
    IsSmoker = models.BooleanField(default=False)
    IsAlcoholic = models.BooleanField(default=False)
    IsOnTcm = models.BooleanField(default=False)
    IsOnMeds = models.BooleanField(default=False)
    HasFHOAnesRxn = models.BooleanField(default=False)
    HasPrevOps = models.BooleanField(default=False)
    HasPONV = models.BooleanField(default=False)
    HasUploadedMedPhoto = models.BooleanField(default=False)

    #preop drugs
    def _upload_path(instance,filename):
        return instance.get_upload_path(filename)

    image = models.ImageField(upload_to=_upload_path, blank = True)

    def get_upload_path(self,filename):
        return str(self.patient_name)+"/"+str(self.created)+"/drugs/"+filename

    #postop wound photos
    def _upload_path(instance,filename):
        return instance.get_upload_path(filename)

    wound = models.ImageField(upload_to=_upload_path, blank = True)

    def get_upload_path(self,filename):
        return str(self.patient_name)+"/"+str(self.created)+"/wound/"+filename




    #Reminder1 questions with QOL
    HasFeverInfecRem1 = models.BooleanField(default=False)
    HasLooseTeethRem1 = models.BooleanField(default=False)
    IsPregnantRem1 = models.BooleanField(default=False)
    IsHavingOpRem1 = models.BooleanField(default=False)
    PainScoreRem1 = models.IntegerField(default = -1)
    MobilityScoreRem1 = models.IntegerField(default = -1)
    ADL_ScoreRem1 = models.IntegerField(default = -1)
    MoodScoreRem1 = models.IntegerField(default = -1)


    #Reminder2 questions
    HasFeverInfecRem2 = models.BooleanField(default=False)
    HasLooseTeethRem2 = models.BooleanField(default=False)
    IsPregnantRem2 = models.BooleanField(default=False)
    IsHavingOpRem2 = models.BooleanField(default=False)


    #pod1 questions
    SatisfactionScorePOD1 = models.IntegerField(default = -1)
    PainScoreRestPOD1 = models.IntegerField(default = -1)
    PainScoreMovPOD1 = models.IntegerField(default = -1)
    PONVScorePOD1 = models.IntegerField(default = -1)
    SoreThroatScorePOD1 = models.IntegerField(default = -1)
    ItchyScorePOD1 = models.IntegerField(default = -1)
    HasDentalDamagePOD1 = models.BooleanField(default=False)
    HasUploadedWoundPhotoPOD1 = models.BooleanField(default=False)
    HasCalfTenderPOD1 = models.BooleanField(default=False)
    HasSOBPOD1 = models.BooleanField(default=False)
    HasFeverPOD1 = models.BooleanField(default=False)
    HasDysuriaRetenPOD1 = models.BooleanField(default=False)
    HasNumbnessPOD1 = models.BooleanField(default=False)
    IsDischargedHomePOD1 = models.BooleanField(default=False)#from sever


    #pod3 questions
    PainScoreRestPOD3 = models.IntegerField(default = -1)
    PainScoreMovPOD3 = models.IntegerField(default = -1)
    HasDysuriaRetenPOD3 = models.BooleanField(default=False)
    HasNumbnessPOD3 = models.BooleanField(default=False)
    HasCalfTenderPOD3 = models.BooleanField(default=False)
    HasSOBPOD3 = models.BooleanField(default=False)
    HasFeverPOD3 = models.BooleanField(default=False)
    HasWoundRedOrDischargePOD3 = models.BooleanField(default=False)
    HasNeededToVisitAePOD3 = models.BooleanField(default=False)
    HasNeededToReadmitPOD3 = models.BooleanField(default=False)
    HasUploadedWoundPhotoPOD3 = models.BooleanField(default=False)
    IsDischargedHomePOD3 = models.BooleanField(default=False)#from server


    #pod5 questions
    PainScorePOD5 = models.IntegerField(default = -1)
    HasCalfTenderPOD5 = models.BooleanField(default=False)
    HasSOBPOD5 = models.BooleanField(default=False)
    HasFeverPOD5 = models.BooleanField(default=False)
    HasDysuriaPOD5 = models.BooleanField(default=False)
    HasWoundRedOrDischargePOD5 = models.BooleanField(default=False)
    HasNeededToVisitAePOD5 = models.BooleanField(default=False)
    HasNeededToReadmitPOD5 = models.BooleanField(default=False)
    HasUploadedWoundPhotoPOD5 = models.BooleanField(default=False)
    IsDischargedHomePOD5 = models.BooleanField(default=False)#from server


    #pod10 questions
    PainScorePOD10 = models.IntegerField(default = -1)
    HasCalfTenderPOD10 = models.BooleanField(default=False)
    HasSOBPOD10 = models.BooleanField(default=False)
    HasFeverPOD10 = models.BooleanField(default=False)
    HasDysuriaPOD10 = models.BooleanField(default=False)
    HasWoundRedOrDischargePOD10 = models.BooleanField(default=False)
    HasNeededToVisitAePOD10 = models.BooleanField(default=False)
    HasNeededToReadmitPOD10 = models.BooleanField(default=False)
    HasUploadedWoundPhotoPOD10 = models.BooleanField(default=False)
    IsDischargedHomePOD10 = models.BooleanField(default=False)#from server

    #pod15 questions with QOL
    PainScorePOD15 = models.IntegerField(default = -1)
    MobilityScorePOD15 = models.IntegerField(default = -1)
    ADL_ScorePOD15 = models.IntegerField(default = -1)
    MoodScorePOD15 = models.IntegerField(default = -1)
    SatisfactionScorePOD15 = models.IntegerField(default = -1)

    HasNeededToVisitAePOD15 = models.BooleanField(default=False)
    HasNeededToReadmitPOD15 = models.BooleanField(default=False)
    HasReturnedToDailyWorkPOD15 = models.BooleanField(default=False)

    HasUploadedWoundPhotoPOD5 = models.BooleanField(default=False)
    IsDischargedHomePOD5 = models.BooleanField(default=False)#from server

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

#logic to get age from date of birth and date of operation
    @property
    def get_age_at_op(self):
        delta = int(self.op_date.year - self.date_of_birth.year)
        return delta

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
        self.age_at_op = self.get_age_at_op
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





