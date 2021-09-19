#Import required libraries
import textwrap, time
from django.utils.text import slugify
from quotes.admin.wpmodels import Images
from quotes.admin import utils
from dqote import env

pinMod = int(env.get('quotes', 'PIN_MOD'))
autoPinMaxChar = int(env.get('quotes', 'AUTO_PIN_MAX_CHAR'))

def updateQuotesImage(quotesObj):

    for obj in quotesObj:
        
        if not obj.quotesTxt:
            obj.quotesTxt = obj.quotes
        imgText = textwrap.wrap(obj.quotesTxt, width=45)[0]
        today = time.strftime('%Y%m%d')
        obj.imagePath = today + '/' + slugify(imgText) + '-' + str(obj.id) + '.jpg'
        obj.imagePathPin = today + '/' + slugify(imgText) + '-pin-' + str(obj.id) + '.jpg'
        obj.imageAlt = imgText
        if not obj.authorSlug:
            obj.authorSlug = slugify(obj.author)
        if not obj.categorySlug:
            obj.categorySlug = slugify(obj.category)
        obj.title = textwrap.wrap(obj.quotes, width=100)[0]
        if not obj.title:
            obj.title = textwrap.wrap(obj.quotesTxt, width=100)[0]
        obj.isUpdated = 1
        img = utils.findOneImage()
        fontObj = utils.findFont(obj)
        obj.fontName = fontObj['name']
        obj.fontSize = fontObj['size']
        if obj.locale == 3:
            obj.fontSize = obj.fontSize + 15
        obj.wordWrap = fontObj['wrap']
        obj.rawImage = img.previewURL
        obj.fontColor = img.views
        obj.imageId = img.id
        obj.save()
        autoCreateQuotes(obj)
        
def autoCreateQuotes(quote):
    param = ('', '', '', '', '')
    quote.isAuto = 1
    utils.writeQuotesOnImage(quote, param)
    if quote.id % pinMod == 0 and quote.quotes.__len__() < autoPinMaxChar:
        quote.isPin = 1
        utils.writeQuotesOnImagePin(quote, param)