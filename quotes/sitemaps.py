from django.utils.text import Truncator, slugify
from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from quotes.models import Quotes
from dqote import env

localeList = eval(env.get('quotes','LOCALE_LIST'))

class QuotesDetailsSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now()}
        return Quotes.objects.filter(**filterParam).order_by('-publishAt')[:50]

    def lastmod(self, obj):
        return obj.publishAt

    def location(self, item):
        langStr = getLocaleStr(item.locale)
        titleTxt = item.quotesTxt
        if not titleTxt:
            titleTxt = item.quotes

        authorTxt = item.authorSlug
        if not authorTxt:
            authorTxt = item.author

        slugTxt = slugify(Truncator(titleTxt).words(5))

        return langStr + '/quotes/' + slugTxt + '-by-' + slugify(authorTxt) + '-' + str(item.id)

class QuotesAuthorSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now()}
        return Quotes.objects.values('author', 'authorSlug', 'locale').filter(**filterParam).order_by('author').distinct()

    def location(self, item):
        langStr = getLocaleStr(item['locale'])
        authorTxt = item['authorSlug']
        if not authorTxt:
            authorTxt = item['author']
        return langStr + '/authors/' + slugify(authorTxt) + '-quotes'
    
class QuotesCategorySitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'locale' : 1}
        return Quotes.objects.values('category', 'categorySlug', 'locale').filter(**filterParam).order_by('category').distinct()

    def location(self, item):
        langStr = getLocaleStr(item['locale'])
        categoryTxt = item['categorySlug']
        if not categoryTxt:
            categoryTxt = item['category']
        return langStr + '/' + slugify(categoryTxt) + '-quotes'

def getLocaleStr(locale):
    langStr = None
    for id, name in localeList.items():
        if id == locale:
            langStr = '/' + name[0]
    if langStr == '/':
        langStr = ''
    return langStr