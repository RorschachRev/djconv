from django.shortcuts import render
from django.http import HttpResponseRedirect


def expo(request):
	expo=""
	return render(request,'pages/expo.html', { 'expo':expo } )
def index(request):
	return render(request,'pages/index.html', { 'index':index } )
def shop(request):
	return render(request,'pages/shop.html', { 'shop':shop } )
def expomap(request):
	return render(request,'pages/expomap.html', { 'map':expomap } )
def edit(request):
	return render(request,'pages/edit.html', { 'edit':edit } )

#@login_required
#@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'pages/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })