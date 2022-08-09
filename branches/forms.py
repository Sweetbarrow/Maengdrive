from django import forms
from django.forms import ModelForm

from branches.models import Branch


class BranchForm(ModelForm):
    def format_phone_number(self, field_name):
        phone_number = self.cleaned_data.get(field_name)
        phone_number = phone_number.replace("-", "")

        if len(phone_number) == 0:
            return phone_number
        elif phone_number[0:2] == "02" and len(phone_number) == 9:
            phone_number = [phone_number[0:2], phone_number[2:5], phone_number[5:]]
            phone_number = "-".join(phone_number)
        elif phone_number[0:2] == "02" and len(phone_number) == 10:
            phone_number = [phone_number[0:2], phone_number[2:6], phone_number[6:]]
            phone_number = "-".join(phone_number)
        elif phone_number[0] != 0 and len(phone_number) == 8:
            phone_number = [phone_number[0:4], phone_number[4:]]
            phone_number = "-".join(phone_number)
        elif len(phone_number) == 10:
            phone_number = [phone_number[0:3], phone_number[3:6], phone_number[6:]]
            phone_number = "-".join(phone_number)
        elif len(phone_number) == 11:
            phone_number = [phone_number[0:3], phone_number[3:7], phone_number[7:]]
            phone_number = "-".join(phone_number)

        return phone_number

    def clean_phone1(self):
        return self.format_phone_number("phone1")

    def clean_phone2(self):
        return self.format_phone_number("phone2")

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
                    "placeholder": "'점'을 포함한 지점명을 입력하세요.",
                }
            ),
            "postcode": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "주소 검색을 이용하세요.",
                    "readonly": "",
                    "aria-describedby": "id_postcode",
                }
            ),
            "address1": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "주소 검색을 이용하세요.",
                    "readonly": "",
                    "aria-describedby": "id_address1",
                }
            ),
            "address2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "상세 주소를 입력하세요.",
                    "aria-describedby": "id_address2",
                }
            ),
            "phone1": forms.TextInput(
                attrs={
                    "type": "tel",
                    "class": "form-control",
                    "placeholder": "전화번호를 입력하세요.",
                }
            ),
            "phone2": forms.TextInput(
                attrs={
                    "type": "tel",
                    "class": "form-control",
                    "placeholder": "전화번호를 입력하세요.",
                }
            ),
        }
