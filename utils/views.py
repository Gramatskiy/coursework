from django_countries.fields import CountryField


def get_coutry_choices(request):
    choices = CountryField().get_choices()
