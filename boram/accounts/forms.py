from django import forms
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    _,
)
from django.contrib.auth import get_user_model
from django.urls import reverse


class CustomLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control'}),
    )

    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'customname'}
    #     )
    # )
    # password = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={'class': 'custompass'}
    #     )
    # )

    # class Meta:
    #     model = get_user_model()
    #     fields = "__all__"
    #     widgets = {
    #         'username': forms.CharField(
    #             attrs={
    #                 'class': 'customname'
    #             }
    #         ),
    #         'password': forms.PasswordInput(
    #             attrs={
    #                 'class': 'custompass'
    #             }
    #         )
    #     }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()
        exclude = ["followings"]


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        # fields = "__all__"
        # exclude = ["password", "last_login", "is_superuser", "is_staff", "is_active", "date_joined", "following", "Groups", "User permissions"]
        fields = [
            # "username",
            "first_name",
            "last_name",
            "email",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get("password"):
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text


class PasswordConfirmationForm(AuthenticationForm):

    agree = forms.BooleanField(
        label="탈퇴를 진행하겠습니다.",
        required=True,  # 체크박스를 필수로 설정
        error_messages={
            'required': '계정 삭제에 동의하려면 체크해야 합니다.'
        }
    )

    class Meta:
        model = get_user_model()
        fields = ["password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')
        self.fields['password'].label = "비밀번호"
