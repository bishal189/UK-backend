from store.models import Collection

def collections_list_header(request):
    return {'collections_list_header': Collection.objects.all()}  # Assuming Collection is your model
