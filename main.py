import functions_framework
import requests

# HTTPトリガ
@functions_framework.http
def main(request):
        requests.post("https://asia-northeast1-android-picture-1816c.cloudfunctions.net/cloudfunction1")
        print("Hello World")
        return "TEST HELLO"
