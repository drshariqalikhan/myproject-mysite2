from django.shortcuts import redirect


def login_redirect(request):
    return redirect('/api/login')


def logout_redirect(request):
    return redirect('/api/logout')
