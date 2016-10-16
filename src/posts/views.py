from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import F

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

# Create your views here.
# Post is the Table 

from django.core.mail import send_mail
from .forms import PostForm
from .forms import ContactForm
from .forms import OrderForm
from .models import Post
from .models import Processor
from .models import Motherboard
from .models import Memory
from .models import Storage
from .models import GPU
from .models import PSU
from .models import Case
from .models import Order

def post_contact(request):
    form_class = ContactForm
    if request.method == 'POST':
    	form = form_class(data=request.POST)
    	if form.is_valid():
    		contact_subject = request.POST.get('subject','')
    		contact_email = request.POST.get('email','')
    		form_content = request.POST.get('content','')

    		instance = form.save(commit=False)
    		instance.save()
    		messages.success(request, "Thank You. Your message has been sent")
    
    return render(request, 'Contact.html', {
        'form': form_class,
    })

#PUT ALERT MESSAGE
def post_home(request):
	form_class = OrderForm
	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			email = request.POST.get('email','')
			proc = request.POST.get('proc','')
			mobo = request.POST.get('mobo','')
			mem = request.POST.get('mem','')
			stor = request.POST.get('stor','')
			gpu = request.POST.get('gpu','')
			psu = request.POST.get('psu','')
			case = request.POST.get('case','')

			template = get_template('PCBUILDER_SHEET.txt')
			context = Context({
				'email':email,
				'proc':proc,
				'mobo':mobo,
				'mem':mem,
				'stor': stor,
				'gpi': gpu,
				'psu': psu,
				'case': case,
				})
			content = template.render(context)

			email = EmailMessage(
				"PC BUILDER FORM SHEET",
				content,
				"PC BUILDER" + '',
				['eresther1110@gmail.com'],
				headers = {'Reply-To': email}
				)
			email.send()

			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "Thank You For Using PC BUILDER")

	return render(request, "index.html", {'form':form_class})

def post_case(request):
	case = Case.objects.all().order_by("-case_qty")

	context ={
		"items": case,
	}
	return render(request, "case.html", context)

def post_ddr3(request):
	mem = Memory.objects.all().filter(mem_socket=1150)
	context ={
		"items": mem,
	}
	return render(request, "ddr3.html", context)

def post_ddr4(request):
	mem = Memory.objects.all().filter(mem_socket=1151)
	context ={
		"items": mem,
	}
	return render(request, "ddr4.html", context)

def post_gpu(request):
	gpu = GPU.objects.all()
	context ={
		"items": gpu,
	}
	return render(request, "gpu.html", context)

def post_moth1150(request):
	mobo = Motherboard.objects.all().filter(mobo_socket=1150)
	context ={
		"items": mobo,
	}
	return render(request, "moth1150.html", context)

def post_moth1151(request):
	mobo = Motherboard.objects.all().filter(mobo_socket=1151)
	context ={
		"items": mobo,
	}
	return render(request, "moth1151.html", context)

def post_proc1150(request):
	proc = Processor.objects.all().filter(proc_socket=1150)
	context ={
		"items": proc,
	}
	return render(request, "proc1150.html", context)

def post_proc1151(request):
	proc = Processor.objects.all().filter(proc_socket=1151)
	context ={
		"items": proc,
	}
	return render(request, "proc1151.html", context)

def post_store(request):
	store = Storage.objects.all()
	context ={
		"items": store,
	}
	return render(request, "store.html",context)

def post_psu(request):
	psu = PSU.objects.all()
	context ={
		"items": psu,
	}
	return render(request, "psu.html", context)