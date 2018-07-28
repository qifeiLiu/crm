from .models import Coloumn

nav_display_columns = Coloumn.objects.filter(nav_display=True)


def nav_column(request):
    return {'nav_display_columns': nav_display_columns}