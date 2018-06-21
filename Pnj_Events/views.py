from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate,login,get_user_model
# from .forms import signup1,main1,search
# from products.models import product



def index(request):
	# qs=product.objects.all()
	# context={
	# 	"obj":qs
	# }
	return render(request, "index/index.html",{})