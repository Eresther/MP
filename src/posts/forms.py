from django import forms

from .models import Post
from .models import Contact
from .models import Order

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title",
			"content"
		]

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
			"email",
			"subject",
			"content",
		]

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = [
			"proc",
			"mobo",
			"mem",
			"stor",
			"gpu",
			"psu",
			"case",
			"email",
		]
	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['proc'].label = "Processor:"
		self.fields['mobo'].label = "Motherboard:"
		self.fields['mem'].label = "Memory:"
		self.fields['stor'].label = "Storage:"
		self.fields['gpu'].label = "Graphics Card:"
		self.fields['psu'].label = "Power Supply:"
		self.fields['case'].label = "Case:"
		self.fields['email'].label = "Email Address:"	