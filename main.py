import functions_framework

# HTTPトリガ
@functions_framework.http
def main(request):
        print("Hello World")
        return "TEST HELLO"
