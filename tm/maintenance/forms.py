from django import forms
from django import forms
from django.forms import formset_factory

class ManualInputForm(forms.Form):
    ALTITUDE = forms.FloatField(label='Altitude')
    ENGINE_LOAD = forms.FloatField(label='Engine Load (%)')
    BAROMETRIC_PRESSURE = forms.FloatField(label='Barometric Pressure (kPa)')
    ENGINE_COOLANT_TEMP = forms.FloatField(label='Engine Coolant Temperature (C)')
    AMBIENT_AIR_TEMP = forms.FloatField(label='Ambient Air Temperature (C)')
    ENGINE_RPM = forms.FloatField(label='Engine RPM')
    INTAKE_MANIFOLD_PRESSURE = forms.FloatField(label='Intake Manifold Pressure (kPa)')
    MAF = forms.FloatField(label='MAF (g/s)')
    AIR_INTAKE_TEMP = forms.FloatField(label='Air Intake Temperature (C)')
    SPEED = forms.FloatField(label='Speed (km/h)')
    THROTTLE_POS = forms.FloatField(label='Throttle Position (%)')
    ENGINE_RUNTIME = forms.CharField(label='Engine Runtime (HH:MM:SS)')

ManualInputFormSet = formset_factory(ManualInputForm, extra=1)

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Insert your data here')
