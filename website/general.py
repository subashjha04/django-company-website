from . models import Settings,Service

def global_data(request):
    data ={
            'settingData': Settings.objects.first(),
            'menuServiceData': Service.objects.all
        }
    
    return data