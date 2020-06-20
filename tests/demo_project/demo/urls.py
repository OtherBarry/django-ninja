from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from someapp.api import router


api_v1 = NinjaAPI()
api_v1.add_router("events", router)
# TODO: check ^ for possible mistakes like `/events` `evetns/``


api_v2 = NinjaAPI(version="2.0.0")


@api_v2.get("events")
def newevents2(request):
    return "events are gone"


api_v3 = NinjaAPI(version="3.0.0")


@api_v3.get("events")
def newevents3(request):
    return "events are gone 3"


@api_v3.get("foobar")
def foobar(request):
    return "foobar"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api_v1.urls),
    path("api/v2/", api_v2.urls),
    path("api/v3/", api_v3.urls),
]