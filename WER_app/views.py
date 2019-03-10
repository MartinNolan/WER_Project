<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from WER_app.models import Review, Page
from WER_app.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    return render(request, 'WER_app/index.html')


def search(request):
    return render(request, 'WER_app/search.html')

def about(request):
    return render(request, 'WER_app/about.html')

=======
from django.shortcuts import render
from django.http import HttpResponse
from WER_app.models import Review, Page
from WER_app.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return render(request, 'WER_app/index.html')


def search(request):
    return render(request, 'WER_app/search.html')

def about(request):
    return render(request, 'WER_app/about.html')
    
    
def FAQ(request):
    return render(request, 'WER_app/FAQ.html')

def tAndC(request):
    return render(request, 'WER_app/t&cs.html')
    
def contact(request):
    return render(request, 'WER_app/contact-us.html')

def login(request):
    return render(request, 'WER_app/login.html')

def sign_up(request):
    return render(request, 'WER_app/sign_up.html')    




def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request, 'WER_app/register.html', {'user_form': user_form, 
	'profile_form': profile_form, 'registered': registered})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your West End Restaurant account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	else:
		return render(request, 'WER_app/login.html', {})



@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect(reverse('index'))

>>>>>>> b6402ed78806fcef14bac857afc8a839b50b676a
def review(request, page_name_slug):
    #review_list = Review.objects.order_by('reviewID')[:4] 
    #pages = Page.objects.order_by('title')[:4]
    #context_dict = {'reviews': review_list, 'pages':pages}
    context_dict = {}
    try:
        page = Page.objects.get(slug=page_name_slug)
        pages = Page.objects.filter(title=page.title)
        reviews = Review.objects.filter(title=page.title)
        context_dict['pages'] = pages
        context_dict['page'] = page
        context_dict['reviews'] = reviews
    except Page.DoesNotExist:
        context_dict['page'] = None
        context_dict['pages'] = None 

    return render(request, 'WER_app/review.html', context_dict)    
    
def FAQ(request):
    return render(request, 'WER_app/FAQ.html')

def tAndC(request):
    return render(request, 'WER_app/t&cs.html')
    
def contact(request):
    return render(request, 'WER_app/contact-us.html')

def login(request):
    return render(request, 'WER_app/login.html')

def sign_up(request):
    return render(request, 'WER_app/sign_up.html')    

def review_sample(request):
    review_list = Review.objects.order_by('reviewID')[:4] 
    pages = Page.objects.order_by('title')[:4]
    context_dict = {'reviews': review_list, 'pages':pages}

<<<<<<< HEAD
    return render(request, 'WER_app/review_sample.html', context_dict)



def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request, 'WER_app/register.html', {'user_form': user_form, 
	'profile_form': profile_form, 'registered': registered})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your West End Restaurant account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	else:
		return render(request, 'WER_app/login.html', {})



@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect(reverse('index'))
=======
    return render(request, 'WER_app/review_sample.html', context_dict)
>>>>>>> b6402ed78806fcef14bac857afc8a839b50b676a
