from quotes.admin.wpmodels import Images
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone
from quotes.models import Quotes
from quotes import seo
from dqote import env

rows = int(env.get('quotes','ROWS'))
pinRows = int(env.get('quotes','PIN_ROWS'))
urlPrefix = env.get('general','URL_PREFIX')
localeList = eval(env.get('quotes','LOCALE_LIST'))

def index(request):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    filterParam['isPin'] = 0
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    url = urlPrefix + '/'
    metas = seo.setMetas(pinQuotes, url)
    aList = authorListByLocale(1)
    cList = categoryListByLocale(1)
    return render(request, 'index.html', {'quotes': quotes, 'metas' : metas, 'url': url, 'urlPrefix' : urlPrefix, 'localeList': localeList, 'page_obj': page_obj, 'aList' : aList, 'cList' : cList})

def about(request):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('?')[:pinRows/2]
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    url = urlPrefix + '/about/'
    metas = seo.setMetas(pinQuotes, url)
    return render(request, 'about.html', {'metas' : metas, 'url': url, 'urlPrefix' : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def contact(request):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('?')[:pinRows/2]
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    url = urlPrefix + '/contact/'
    metas = seo.setMetas(pinQuotes, url)
    return render(request, 'contact.html', {'metas' : metas, 'url': url, 'urlPrefix' : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def privacyPolicy(request):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('?')[:pinRows/2]
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    url = urlPrefix + '/privacy-policy/'
    metas = seo.setMetas(pinQuotes, url)
    return render(request, 'privacy-policy.html', {'metas' : metas, 'url': url, 'urlPrefix' : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def tnc(request):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('?')[:pinRows/2]
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    url = urlPrefix + '/terms-and-conditions/'
    metas = seo.setMetas(pinQuotes, url)
    return render(request, 'terms-and-conditions.html', {'metas' : metas, 'url': url, 'urlPrefix' : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def category(request, category):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'category' : category, 'locale' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    if not pinQuotes:
        filterParam.pop('category')
        pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    filterParam['isPin'] = 0
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    if not quotes:
        filterParam.pop('category')
        quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]

    url = urlPrefix + '/' + category + '-quotes'
    metas = seo.setMetas(pinQuotes, url)
    return render(request, 'index.html', {'quotes': quotes, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def author(request, authorSlug):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : 1, 'authorSlug' : authorSlug}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    if not pinQuotes:
        filterParam.pop('authorSlug')
        pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    filterParam['isPin'] = 0
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    if not quotes:
        filterParam.pop('authorSlug')
        quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    url = urlPrefix + '/authors/' + authorSlug + '-quotes'
    metas = seo.setMetas(pinQuotes, url)
    return render(request, 'index.html', {'quotes': quotes, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def authorsList(request):
    isActive = request.GET.get('isActive', None)
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'locale' : 1}
    if isActive == '0':
        filterParam.pop('isActive')
        filterParam.pop('publishAt__lt')
    authors = Quotes.objects.values('author').filter(**filterParam).order_by('author').distinct()
    aList = list(authors)
    return JsonResponse(aList, safe=False)

def imageList(request):
    isActive = request.GET.get('isActive', None)
    filterParam = {'isActive' : 1}
    if isActive == '0':
        filterParam.pop('isActive')
    imgs = Images.objects.values('id','tags').filter(**filterParam).order_by('id')
    aList = list(imgs)
    return JsonResponse(aList, safe=False)

def fontList(request):
    fonts = eval(env.get('quotes', 'FONT_LIST'))
    return JsonResponse(fonts, safe=False)

def categoryList(request):
    isActive = request.GET.get('isActive', None)
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now()}
    if isActive == '0':   
        filterParam.pop('isActive')
        filterParam.pop('publishAt__lt')
    category = Quotes.objects.values('category').filter(**filterParam).order_by('category').distinct()
    cList = list(category)
    return JsonResponse(cList, safe=False)

def details(request, quotesSlug, id):
    quote1 = Quotes.objects.filter(id=id).filter(publishAt__lt = timezone.now()).filter(isActive=1).first()
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).exclude(id=id).order_by('-publishAt')
    filterParam['isPin'] = 0
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    quotes = Quotes.objects.filter(**filterParam).exclude(id=id).order_by('-publishAt')[:rows]
 
    url = urlPrefix + '/quotes/' + quotesSlug + '-' + str(id)
    metas = seo.setMetas((quote1,), url)
    return render(request, 'details.html', {'quotes': quotes, 'quote1' : quote1, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def showLogin(request):
    return render(request, 'login.html')

def search(request):
    q = request.GET.get('q', None)

    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'locale' : 1}
    if q:
        filterParam['category__istartswith'] = q
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    
    if not quotes.exists():
        filterParam['quotes__istartswith'] = q
        filterParam.pop('category__istartswith')
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]


    if not quotes.exists():
        filterParam['quotes__icontains'] = q
        filterParam.pop('quotes__istartswith')
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    
    if not quotes.exists():
        filterParam.pop('quotes__icontains')
    
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    url = urlPrefix + '/search?q=' + q
    metas = seo.setMetas(quotes, url)
    return render(request, 'index.html', {'quotes': quotes, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix})

def dynamicHome(request, locale):
    langCode = getLocaleCode(locale)
    print('dynamicHome')
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : langCode}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    filterParam['isPin'] = 0
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    url = urlPrefix + '/' + locale
    metas = seo.setMetas(pinQuotes, url)
    aList = authorListByLocale(langCode)
    cList = categoryListByLocale(langCode)
    return render(request, 'dynamic-home.html', {'locale': locale, 'quotes': quotes, 'metas' : metas, 'url': url, 'urlPrefix' : urlPrefix, 'localeList': localeList, 'page_obj': page_obj, 'aList' : aList, 'cList' : cList})

def dynamicDetails(request, locale, quotesSlug, id):
    langCode = getLocaleCode(locale)
    print('dynamicDetails')
    quote1 = Quotes.objects.filter(id=id).filter(publishAt__lt = timezone.now()).filter(isActive=1).first()
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : langCode}
    pinQuotes = Quotes.objects.filter(**filterParam).exclude(id=id).order_by('-publishAt')
    filterParam['isPin'] = 0
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    quotes = Quotes.objects.filter(**filterParam).exclude(id=id).order_by('-publishAt')[:rows]
 
    url = urlPrefix + '/' + locale + '/quotes/' + quotesSlug + '-' + str(id)
    metas = seo.setMetas((quote1,), url)
    return render(request, 'dynamic-details.html', {'locale': locale, 'quotes': quotes, 'quote1' : quote1, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def dynamicCategory(request, locale, category):
    langCode = getLocaleCode(locale)
    print('dynamicCategory')
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'category' : category, 'locale' : langCode}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    if not pinQuotes:
        filterParam.pop('category')
        pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    filterParam['isPin'] = 0
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    if not quotes:
        filterParam.pop('category')
        quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]

    url = urlPrefix + '/' + locale + '/' + category + '-quotes'
    metas = seo.setMetas(pinQuotes, url)
    return render(request, 'dynamic-home.html', {'locale': locale, 'quotes': quotes, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def dynamicAuthor(request, locale, authorSlug):
    langCode = getLocaleCode(locale)
    print('dynamicAuthor')
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'locale' : langCode, 'authorSlug' : authorSlug}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    if not pinQuotes:
        filterParam.pop('authorSlug')
        pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    filterParam['isPin'] = 0
    paginator = Paginator(pinQuotes, pinRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    if not quotes:
        filterParam.pop('authorSlug')
        quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    url = urlPrefix + '/' + locale + '/authors/' + authorSlug + '-quotes'
    metas = seo.setMetas(pinQuotes, url)
    return render(request, 'dynamic-home.html', {'locale': locale, 'quotes': quotes, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix, 'localeList': localeList, 'page_obj': page_obj})

def authorListByLocale(locale):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'locale' : locale}
    return Quotes.objects.values('author', 'authorSlug', 'locale').filter(**filterParam).order_by('author').distinct()[:7]

def categoryListByLocale(locale):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'locale' : locale}
    return Quotes.objects.values('category', 'categorySlug', 'locale').filter(**filterParam).order_by('category').distinct()[:7]

def getLocaleCode(locale):
    langCode = 1
    for id, name in localeList.items():
        if name[0] == locale:
            langCode = id
    return langCode