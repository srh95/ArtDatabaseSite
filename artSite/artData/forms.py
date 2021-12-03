from django import forms
from .models import(
    CustomerModel,
    ArtWorkModel,
    ArtShowModel,
    ArtistModel,
    CollectorModel,
    BuyerModel,
    RenterModel,
    RentModel,
    SaleModel)
    # RentedModel,
    # SoldModel,
    # DisplayedModel)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        #fields = ["customer_id", "first_name", "last_name", "street_num","street_name", "city", "state", "zip_code", "preferred_style", "preferred_medium", "phone_num", "artist_id"]
        exclude = ['customer_id']

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = ArtWorkModel
        fields = '__all__'

class ArtistForm(forms.ModelForm):
    class Meta:
        model = ArtistModel
        exclude = ['artist_id']

class ArtshowForm(forms.ModelForm):
    class Meta:
        model = ArtShowModel
        fields = '__all__'

class CollectorForm(forms.ModelForm):
    class Meta:
        model = CollectorModel
        exclude = ['collector_id']

class BuyerForm(forms.ModelForm):
    class Meta:
        model = BuyerModel
        exclude = ['buyer_id']

class RenterForm(forms.ModelForm):
    class Meta:
        model = RenterModel
        exclude = ['renter_id']

class SaleForm(forms.ModelForm):
    class Meta:
        model = SaleModel
        fields = '__all__'

class RentForm(forms.ModelForm):
    class Meta:
        model = RentModel
        fields = '__all__'