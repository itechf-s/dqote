from quotes.admin.wpmodels import Images
import os, shutil, time
from dqote import env

imgFilePath = env.get('quotes', 'LOC_IMG_FILE_PATH')
app_root = env.get('quotes', 'APP_ROOT')
image_path = env.get('quotes', 'IMG_DIR')

# custom image search
def saveImagesInDb(username):
    imgFile = os.listdir(imgFilePath)
    for imgFileName in imgFile:
        print('img: ', imgFileName)
        imgDict = imageData(username)
        imgObj = Images(**imgDict)
        imgObj.save()
        srcPath = imgFilePath + imgFileName
        imgArr = os.path.splitext(imgFileName)
        dstUrl = image_path + 'raw/'  + str(imgObj.id) + imgArr[1]
        shutil.move(srcPath, app_root + dstUrl)
        imgObj.pageURL = dstUrl
        imgObj.previewURL = dstUrl
        imgObj.webformatURL = dstUrl
        imgObj.tags = imgArr[0].replace('-', ', ')
        imgObj.save()

def imageData(username):
    img = {}
    randomNum = str(time.time()).split('.')[1]
    img['imageId'] = int(randomNum)
    img['pageURL'] = ''
    img['type'] = 'photo'
    img['tags'] = 'back'
    img['previewURL'] = ''
    img['previewWidth'] = 150
    img['previewHeight'] = 100
    img['webformatURL'] = ''
    img['webformatWidth'] = 640
    img['webformatHeight'] = 430
    img['largeImageURL'] = ''
    img['imageWidth'] = 0
    img['imageHeight'] = 0
    img['imageSize'] = 0
    img['views'] = 'black'
    img['downloads'] = 0
    img['collections'] = 0
    img['likes'] = 0
    img['comments'] = 0
    img['user_id'] = 0
    img['user'] = username
    img['userImageURL'] = 0
    img['isActive'] = 1
    img['isDeleted'] = 0
    img['isPin'] = 0
    return img




#         pageURL: https://pixabay.com/photos/egret-flying-fog-dawn-sunrise-5937499/
#            type: photo
#            tags: egret, flying, fog
#      previewURL: https://cdn.pixabay.com/photo/2021/01/21/14/10/egret-5937499_150.jpg
#    previewWidth: 150
#   previewHeight: 100
#    webformatURL: https://pixabay.com/get/g116a90bc9567e2e9b5a96bd89d45d2b75e439b4388ed3a2348ba1a053c4f65a1fa4f94ba560259f765a35f5b01c52b82b731e7eb32dff21cb7351e622fae06c8_640.jpg
#  webformatWidth: 640
# webformatHeight: 427
#   largeImageURL: https://pixabay.com/get/g7cf23e35ebddf22c80f207e042835bfcb51dfabeda062457b9b7b575d8ae9194ba34212713025f90fec5e899346c6942d0e81e36e347010d3611b32c415cd482_1280.jpg
#      imageWidth: 5000
#     imageHeight: 3333
#       imageSize: 5569633
#           views: 352515
#       downloads: 331648
#     collections: 377
#           likes: 428
#        comments: 88
#         user_id: 7703165
#            user: KIMDAEJEUNG
#    userImageURL: https://cdn.pixabay.com/user/2021/04/19/20-00-29-813_250x250.jpg
#       createdAt: 2021-08-06 16:55:28.714924
#        isActive: 1
#       updatedAt: 2021-08-06 16:55:28.714975
#       isDeleted: 0
#           isPin: 0
