from django.shortcuts import render, redirect
from django.http import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import wikipedia
from django.core.paginator import Paginator

# Create your views here.

def kitoblar_list(request):
    kitoblar = Kitob.objects.all()
    paginator = Paginator(kitoblar, 1)  # Sahifadagi kitoblar soni
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'p.html', {'page_obj': page_obj})


def HomePage(request):

    if request.method == "POST":
        return SearchPage(request)
        
    else:
        all = Category.objects.all()
        down = BookDownloads.objects.filter(id=1)
        kitob = Kitob.objects.all()
        
        paginator = Paginator(kitob, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            "index.html",
            {
                "category": all if all.exists() else False,
                "kitob_soni": Kitob.objects.count(),
                "down": down,
                "books": kitob if kitob.exists() else False,
                "page_obj": page_obj,
            },
        )


def SearchPage(request):
    if request.method == 'POST':
        text = request.POST.get("Search")
        results = Kitob.objects.filter(name__icontains=text)
        print(results)

        all = Category.objects.all()
        down = BookDownloads.objects.filter(id=1)
        kitob = Kitob.objects.all()
        return render(
            request,
            "search.html",
            {
                "result": results,
                "results": results if results.exists() else False,
                "txt": text,
                "category": all if all.exists() else False,
                "kitob_soni": Kitob.objects.count(),
                "down": down,
            },
        )
    else:
        return redirect("category")


def CategorysPage(request):
    if request.method == "POST":
        return SearchPage(request)

    category = Category.objects.all()
    return render(
        request,
        "category.html",
        {
            "category": category if category.exists() else False,
        },
    )


def BooksPage(request, slug):

    if request.method == "POST":
        return SearchPage(request)

    categ = Category.objects.all()
    book = Kitob.objects.all()

    return render(
        request,
        "books.html",
        {"slug": slug, "category": categ, "books": book if book.exists() else False},
    )


def Book(request, category, slug):

    if request.method == "POST":
        return SearchPage(request)

    categ = Category.objects.all()
    book = Kitob.objects.filter(id=slug)
    try:
        for i in book:
            a = i.name
        wikipedia.set_lang("uz")
        haqida = wikipedia.summary(f"{a} haqida")
    except:
        haqida = "Hozircha mavjud emas"

    for i in book:
        t = int(i.view) + 1
        book.update(view=t)
    g = Kitob.objects.filter(id=slug)
    return render(
        request,
        "book.html",
        {
            "haqida": haqida,
            "slug": slug,
            "categ": category,
            "category": categ,
            "books": g if g.exists() else False,
        },
    )


def LogoutPage(request):
    logout(request)
    return redirect("home")


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("user")
            password = request.POST.get("pass")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(
                    request,
                    "login.html",
                    {
                        "text": "Login yoki parol noto'g'ri",
                        "color": "red",
                        "v1": username,
                        "v2": password,
                    },
                )

        return render(
            request,
            "login.html",
            {"text": "Kirish uchun kirish ma'lumotlarini kiriting"},
        )


def SignupPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            lname = request.POST.get("lname")
            fname = request.POST.get("fname")
            pass1 = request.POST.get("pass1")
            pass2 = request.POST.get("pass2")
            email = request.POST.get("email")
            if pass1 == pass2:
                print(User.objects.filter(username=username).exists())
                if User.objects.filter(username=username).exists():
                    return render(
                        request,
                        "signup.html",
                        {
                            "text": "Ushbu user band, boshqa o'ylab toping",
                            "color": "red",
                            "fn": fname,
                            "ln": lname,
                            "em": email,
                            "us": username,
                            "p1": pass1,
                            "p2": pass2,
                        },
                    )
                elif User.objects.filter(email=email).exists():
                    return render(
                        request,
                        "signup.html",
                        {
                            "text": "Ushbu email band, boshqa email kiriting",
                            "color": "red",
                            "fn": fname,
                            "ln": lname,
                            "em": email,
                            "us": username,
                            "p1": pass1,
                            "p2": pass2,
                        },
                    )
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=pass1
                    )
                    user.save()
                    login(request, user)
                    return redirect("home")
            else:
                return render(
                    request,
                    "signup.html",
                    {
                        "text": "Parollar mos kelmayabdi",
                        "color": "red",
                        "fn": fname,
                        "ln": lname,
                        "em": email,
                        "us": username,
                        "p1": pass1,
                        "p2": pass2,
                    },
                )
        return render(
            request,
            "signup.html",
            {"text": "Ro'yxatdan o'tish uchun shaxsiy ma'lumotlaringizni kiriting"},
        )
