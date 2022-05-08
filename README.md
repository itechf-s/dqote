# quotes
Quotes Blog Site created in Python Django

You can use this code to generate quotes and write on images
This project also import images from pixabay api for quotes

You can check Live in below URL
https://dqote.com

If any Question feel free to contact us 
https://itechf.com/contact/

# db table copy
`mysqldump --user=root quotes quotes_images --password=t00r --compact --add-drop-table | mysql -u root --password=t00r dqote`

## Query
select * from quotes_images order by id desc limit 2 \G
select * from quotes_quotes order by id desc limit 2 \G
select * from quotes_quotes where isActive = 1 order by id desc limit 1 \G
select * from quotes_quotes where id = 5376 order by id desc limit 1 \G
select * from quotes_quotes where id = 5377 order by id desc limit 1 \G
select * from quotes_quotes where id = 190 order by id desc limit 1 \G
Schd : isActive = 0 and isUpdated = 1 and isSchd = 1 and isAuto = 1
Draft : isActive = 0 and isUpdated = 1 and isSchd = 0 and isAuto = 1



## Quotes Published but not Schedule
select count(*) from quotes_quotes where  isActive = 1 and isUpdated = 1 and isSchd = 0 and isAuto = 0 order by id desc limit 1 \G
select * from quotes_quotes where  isActive = 1 and isUpdated = 1 and isSchd = 0 and isAuto = 0 order by id desc limit 1 \G

## Quotes Present in Draft
select count(*) from quotes_quotes where isActive = 0 and isUpdated = 1 and isSchd = 0 and isAuto = 1 order by id desc limit 1 \G

## Quotes sent from Draft to Schedule
update quotes_quotes set isSchd = 1 where isActive = 0 and isUpdated = 1 and isSchd = 0 and isAuto = 1 order by id desc limit 1 \G
update quotes_quotes set isSchd = 1 where isActive = 0 and isUpdated = 1 and isSchd = 0 and isAuto = 1;

## Quotes Present in Schedule
select Count(*) from quotes_quotes where isActive = 0 and isUpdated = 1 and isSchd = 1 and isAuto = 1 order by id desc limit 1 \G


update quotes_images set views = 'white';