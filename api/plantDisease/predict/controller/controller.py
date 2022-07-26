from rest_framework.generics import GenericAPIView
from django.http import JsonResponse

from predict.implementation.implementation import PredictImageImplementation
from django.core.files.storage import FileSystemStorage


class PredictImage(GenericAPIView):
    def post(self, requests):
        response = {"status": 200, "payload": "", "message": "", "error": ""}
        try:
            requests = requests.FILES.get('imgFile')
            fss = FileSystemStorage()
            file = fss.save(requests.name, requests)
            file_url = fss.url(file)
            print(file_url)
            predictImage_implementation = PredictImageImplementation(requests)
            payload = predictImage_implementation.predict_image(requests.name)

            if payload:
                response['payload'] = payload
                response['message'] = "Success"
        except Exception as e:
            print(e)
            response['message'] = "Failed"
            response['error'] = str(e)
        finally:
            return JsonResponse(response)

