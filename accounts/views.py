from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def signup(request):
    # POST일 때
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # 유저가 이미 있을 때 ()
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': '이미 존재하는 아이디입니다'})

            # 유저가 없을 때 (새로 가입)
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1']
                )
                auth.login(request, user)
                return redirect('blog')  # 이렇게 써도 되나?
        # POST이지만 패스워드 confirm이 일치하지 않을 때
        else:
            return render(request, 'accounts/signup.html', {'error': '패스워드와 패스워드 확인이 일치하지 않습니다'})
    # GET일 때
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 입력받은 정보로 일치하는 정보가 있는지 확인 (authenticate)
        user = auth.authenticate(request, username=username, password=password)
        # 정보가 있다면 로그인하고 홈으로 redirect
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        # 정보가 없다면 에러메시지 출력
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect..'})
    return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog')
    return render(request, 'accounts/signup.html')
