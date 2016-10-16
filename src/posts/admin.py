from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Processor
from .models import Motherboard
from .models import Memory
from .models import Storage
from .models import GPU
from .models import PSU
from .models import Case
from .models import Contact
from .models import Order

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'last_updated' , 'timestamp']
	list_filter = ['last_updated', 'timestamp']
	search_fields = ['title', 'content']
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)

class OrderAdmin(admin.ModelAdmin):
	list_display = ['email', 'timestamp']
	list_filter = ['email', 'timestamp']
	search_fields = ['email']
	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)

class ContactAdmin(admin.ModelAdmin):
	list_display = ['email', 'subject', 'timestamp']
	list_display_links = ['email']
	list_filter = ['email', 'timestamp']
	search_fields = ['email', 'subject']
	class Meta:
		model = Contact

admin.site.register(Contact, ContactAdmin)

class ProcessorAdmin(admin.ModelAdmin):
	list_display = ['proc_model', 'proc_socket' , 'proc_watts', 'proc_content','proc_cost', 'proc_qty']
	list_display_links = ['proc_model']
	list_filter = ['proc_model', 'proc_socket']
	search_fields = ['proc_model', 'proc_socket']
	class Meta:
		model = Processor

admin.site.register(Processor, ProcessorAdmin)

class MotherboardAdmin(admin.ModelAdmin):
	list_display = ['mobo_model', 'mobo_socket' , 'mobo_watts', 'mobo_content','mobo_cost', 'mobo_qty']
	list_display_links = ['mobo_model']
	list_filter = ['mobo_model', 'mobo_socket']
	search_fields = ['mobo_model', 'mobo_socket']
	class Meta:
		model = Motherboard

admin.site.register(Motherboard, MotherboardAdmin)

class MemoryAdmin(admin.ModelAdmin):
	list_display = ['mem_model', 'mem_socket' , 'mem_watts', 'mem_content','mem_cost', 'mem_qty']
	list_display_links = ['mem_model']
	list_filter = ['mem_model', 'mem_socket']
	search_fields = ['mem_model', 'mem_socket']
	class Meta:
		model = Memory

admin.site.register(Memory, MemoryAdmin)

class StorageAdmin(admin.ModelAdmin):
	list_display = ['store_model', 'store_watts', 'store_content','store_cost', 'store_qty']
	list_display_links = ['store_model']
	list_filter = ['store_model',]
	search_fields = ['store_model']
	class Meta:
		model = Storage

admin.site.register(Storage, StorageAdmin)

class GPUAdmin(admin.ModelAdmin):
	list_display = ['GPU_model', 'GPU_watts', 'GPU_content','GPU_cost', 'GPU_qty']
	list_display_links = ['GPU_model']
	list_filter = ['GPU_model']
	search_fields = ['GPU_model']
	class Meta:
		model = GPU

admin.site.register(GPU, GPUAdmin)

class PSUAdmin(admin.ModelAdmin):
	list_display = ['PSU_model', 'PSU_watts', 'PSU_content','PSU_cost', 'PSU_qty']
	list_display_links = ['PSU_model']
	list_filter = ['PSU_model']
	search_fields = ['PSU_model']
	class Meta:
		model = PSU

admin.site.register(PSU, PSUAdmin)

class CaseAdmin(admin.ModelAdmin):
	list_display = ['case_model', 'case_content','case_cost', 'case_qty']
	list_display_links = ['case_model']
	list_filter = ['case_model']
	search_fields = ['case_model']
	class Meta:
		model =Case

admin.site.register(Case, CaseAdmin)