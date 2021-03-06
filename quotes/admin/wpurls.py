"""
Bestrani Quotes App URL Configuration
"""
from django.urls import path
from quotes.admin import wpviews
urlpatterns = [
    path('update',wpviews.update, name='update'),
    path('make-quote',wpviews.makeQuote, name='makeQuote'),
    path('make-bulk-quotes',wpviews.makeBulkQuotes, name='makeBulkQuotes'),
    path('list/<int:isActive>/<int:isUpdated>',wpviews.list, name='list'),
    path('activate',wpviews.activate, name='activate'),
    path('cache-purge', wpviews.cachePurge, name='cachePurge'),
    path('import-quotes-data', wpviews.importQuotes, name='cachePurge'),

    path('saveImagesInDb',wpviews.saveImagesInDb, name='saveImagesInDb'),
    path('saveLocImagesInDb',wpviews.saveLocImagesInDb, name='saveLocImagesInDb'),
    path('list-images/<int:isActive>',wpviews.listImages, name='listImages'),
    path('act-image',wpviews.actImage, name='actImage'),
    path('makeSiteLive',wpviews.makeSiteLive, name='makeSiteLive'),
    path('purgeSite',wpviews.purgeSite, name='purgeSite'),

    path('chk-login',wpviews.chkLogin, name='login'),
    path('chk-logout',wpviews.chkLogout, name='logout'),
]