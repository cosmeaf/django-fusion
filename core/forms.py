from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Menssagem', widget=forms.Textarea)

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        data = f'Nome: {name}\n E-mail: {email} \n Assunto: {subject} \n Menssagem: {message}'

        mail = EmailMessage(
            subject=subject,
            body=data,
            from_email='contato@lexlam.com.br',
            to=['cosme.alex@gmail.com',],
            headers={'Reply-To: ': email}
        )
        mail.send()
