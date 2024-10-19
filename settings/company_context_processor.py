from .models import company



def get_company_date(request):
    data = company.objects.last()
    return {'company_data': data}