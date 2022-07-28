from django import forms

from branches.models import Branch


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = [
            "name",
            "postcode",
            "address1",
            "address2",
            "phone1",
            "phone2",
        ]
        labels = {
            "name": "지점명",
            "postcode": "우편번호",
            "address1": "도로명 주소",
            "address2": "상세 주소",
            "phone1": "전화번호 1",
            "phone2": "전화번호 2",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "postcode": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "disabled": "",
                    "readonly": "",
                    "aria-describedby": "id_postcode",
                }
            ),
            "address1": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "disabled": "",
                    "readonly": "",
                    "aria-describedby": "id_address1",
                }
            ),
            "address2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "disabled": "",
                    "readonly": "",
                    "aria-describedby": "id_address2",
                }
            ),
            "phone1": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "phone2": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
