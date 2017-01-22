from django.contrib import admin

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
	def get(self, request):
		return redirect('/')