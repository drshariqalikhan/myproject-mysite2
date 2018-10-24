import sys, os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'mysite2.settings'
django.setup()

from myop_app.models import JourneyData
from pyfcm import FCMNotification

allPats = JourneyData.objects.all()
push_service = FCMNotification(api_key= "AAAA3Ac3JAQ:APA91bEX8mtHeWClfBA4oi3QPO7dsjW0epeC0PoaEMf0ucRIqFHYrEIKpNiAgP8yiW617Ol92gPT4Z_yC6EmQwYxHu5fDtdTJ9SUgaTP1EP-n2UUiwBxxfM6TVv7c0hziJnhj-azo8uk")

# registration_id = " fDzo5HHT4FI:APA91bEzvlGyJ8-5Pw_IgRLQo4boR9XWoTPHOj6UtsAd4GFCRPF8F_ozlERS3yOFHmoaXxR6VpAQovU6aC-BMVlJyHHatI3xIKK4ChX_H3bmjohoR-ODSn3F-PqbHda8PQeNO53XG2ts"
registration_id = "exepQSOBR_g:APA91bGMgioVP1mRPVZtO_G0oRvXaE0Vz0wkB_Ydx03Zd30CcTPEOgTqWO7jIGZgrPh-0r2ZL7RaJJgViuv52JD-tc_4ueD7rUEs03SU4gfvZxgyD0EepgUvwEeuXgaV3ak89pPbR4S7"
message_title = str(allPats[0].journey_point)
message_body = "My First PushNotification:"+str(allPats[0].op_date)

# message_body = "My First PushNotification"+str(allPats[0].patient_name)
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)