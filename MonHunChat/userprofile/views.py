from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

from userprofile.models import UserProfile

from forms import UserProfileForm

def roster(request):
    roster_list = UserProfile.objects.order_by('user')
    context_dict = {'members': roster_list}
    return render(request, 'userprofile/roster.html', context_dict)


@login_required
def update_profile(request):
    userProfile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(initial={
        'description': userProfile.description,
        'rank': userProfile.rank,
        'weapon': userProfile.weapon,
        'friend_code': userProfile.friend_code,
        'hunter_name': userProfile.hunter_name,
        'nintendo_name': userProfile.nintendo_name,
        'skype_name': userProfile.skype_name,
        'teamspeak_name': userProfile.teamspeak_name
    })
    return render_to_response(
            'userprofile/update_profile.html',
            {'form': form},
            RequestContext(request)
    )


@login_required
def send_update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            userProfile = UserProfile.objects.get(user=request.user)
            description = form.cleaned_data['description']
            rank = form.cleaned_data['rank']
            weapon = form.cleaned_data['weapon']
            friend_code = form.cleaned_data['friend_code']
            hunter_name = form.cleaned_data['hunter_name']
            nintendo_name = form.cleaned_data['nintendo_name']
            skype_name = form.cleaned_data['skype_name']
            teamspeak_name = form.cleaned_data['teamspeak_name']
            userProfile.description = description
            userProfile.rank = rank
            userProfile.weapon = weapon
            userProfile.friend_code = friend_code
            userProfile.hunter_name = hunter_name
            userProfile.nintendo_name = nintendo_name
            userProfile.skype_name = skype_name
            userProfile.teamspeak_name = teamspeak_name
            userProfile.save()
            return redirect('/roster/profile/' + str(userProfile.id))

        else:
            form = UserProfileForm()

    return redirect('/roster/send_update_profile/')


@login_required
def profile(request, profile_id):
    if profile_id == "0":
        if request.user.is_authenticated:
            userProfile = UserProfile.objects.get(user=request.user)
    else:
        userProfile = UserProfile.objects.get(pk=profile_id)

    return render_to_response(
            'userprofile/profile.html',
            {'userProfile': userProfile},
            RequestContext(request)
    )
