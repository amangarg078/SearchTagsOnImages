from clarifai.rest import ClarifaiApp
import os
import sqlite3

path='./static/images'

CLIENT_ID='diMzfKqYf5MHVbhRkslsJCw8Isqu27csWDRtzrwx'
CLIENT_SECRET='OZI78AHiE4-9ffp-dhPfOj5AjksUIVOPHA0d7Aoh'

clarifai_api=ClarifaiApp(CLIENT_ID,CLIENT_SECRET)
model = clarifai_api.models.get('general-v1.3')
result={}
for image in os.listdir(path):
    try:
        image_tags= model.predict_by_filename(image)
        temp_list=[]
        for i in image_tags['outputs'][0]['data']['concepts']:
            temp_list.append(i['name'])
        result[image]=temp_list
        print result[image]
    except:
        pass


inverted_dict={}
for k,v in result.items():
    for x in v:
	inverted_dict.setdefault(x,[]).append(k)

os.chdir('../')
conn=sqlite3.connect("tags.sqlite3")
c=conn.cursor()

for i in result:
    c.execute('insert into searchengine_image(image_name,image_tags) values(?,?)',(i,','.join(result[i])))

for i inverted_dict:
    c.execute('insert into searchengine_tags(tag_name,tag_images) values(?,?)',(i,','.join(nverted_dict[i])))

conn.commit()
c.close()
conn.close()
