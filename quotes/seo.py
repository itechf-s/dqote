import textwrap
from dqote import env

imgPrefix = env.get('quotes', 'IMG_PREFIX')
imgDir = env.get('quotes', 'IMG_DIR')
seoDec = env.get('quotes', 'SEO_DESC')
qHeight = int(env.get('quotes', 'HEIGHT'))
qWidth = int(env.get('quotes', 'WIDTH'))

def setMetas(qots, url):
    desc = seoDec
    metaProps = {}
    metaNames = {}
    if qots:
        qot = qots[0]
        imgPath = imgPrefix + imgDir + qot.imagePath
        title = qot.title
        title = title if title else qot.imageAlt
        metaNames['title'] = qot.imageAlt
        metaProps['og:site_name'] = 'BestRani'
        metaProps['og:title'] = qot.imageAlt
        metaProps['og:type'] = 'article'
        desc = qot.quotes
        desc = qot.desc if qot.desc else desc
        metaNames['description'] = desc
        metaProps['og:description'] = desc
        metaProps['og:url'] = url
        metaProps['og:image'] = imgPath
        metaProps['og:image:alt'] = qot.imageAlt
        metaProps['og:image:type'] = 'image/jpeg'
        metaProps['og:image:width'] = qWidth
        metaProps['og:image:height'] = qHeight
        metaProps['og:locale'] = 'en_US'
        metaProps['og:locale:alternate'] = 'en_IN'
        metaNames['twitter:card'] = 'summary'
        metaNames['twitter:site'] = '@BestRani3'
        metaNames['twitter:url'] = url
        metaNames['twitter:title'] = qot.imageAlt
        metaNames['twitter:description'] = desc
        metaNames['twitter:image'] = imgPath
        metaNames['datePublished'] = qot.publishAt.strftime("%Y-%m-%dT%H:%M:%S%z")
        metaNames['article:published_time'] = qot.publishAt.strftime("%Y-%m-%dT%H:%M:%S%z")
        metaNames['article:author'] = 'Iffat Zia'
        #if qot.updatedAt > qot.publishAt:
        #    metas['dateModified'] = qot.publishAt.strftime("%Y-%m-%dT%H:%M:%S%z")
    return {'metaNames': metaNames, 'metaProps': metaProps}