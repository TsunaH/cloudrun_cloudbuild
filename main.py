import functions_framework
import requests

# HTTPトリガ
@functions_framework.http
def main(request):
        response = requests.post("https://asia-northeast1-android-picture-1816c.cloudfunctions.net/cloudfunction1")
        print(f"{response.status_code}")
        print(f"{response.text}")
        return "TEST HELLO"
