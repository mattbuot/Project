import pandas as pd
import re
import requests


# Selecting labels with an organic label
def organic_labels(df):
    return df['labels'][
        df['labels'].str.contains('Bio', na = False, flags = re.IGNORECASE)
        | df['labels'].str.contains('Organic', na = False, flags = re.IGNORECASE)
        |  df['labels'].str.contains('\bAB\b', na = False, flags = re.IGNORECASE)
        ].unique()


# Selecting products with an organic label
def organic_products(df):
    return df[
        df['labels'].str.contains('Bio', na = False, flags = re.IGNORECASE)
        | df['labels'].str.contains('Organic', na = False, flags = re.IGNORECASE)
        |  df['labels'].str.contains('\bAB\b', na = False, flags = re.IGNORECASE)
        ]


# Retrieving front image url from barcode
def get_image_url(code):
    url = 'https://world.openfoodfacts.org/api/v0/product/' + str(code) + '.json'
    r = requests.get(url)
    json = r.json()
    if r.status_code == 200 and json['status_verbose'] == 'product found':
        try:
            return json['product']['image_url']
        except KeyError:
            try:
                return json['product']['selected_images']['front']['display']['fr']
            except KeyError:
                return 'No image available'
    else:
        return 'No image available'
    
    
# Saving image locally from url to an 'images' folder which needs to be created beforehand
def save_image(name, image_url):
    image_data = requests.get(image_url).content
    images_folder = 'images/'
    file_name = name + '.jpg'
    with open(images_folder + file_name, 'wb') as handler:
        handler.write(image_data)
        
        
# Downloading n images (all by default) to an 'images' folder which needs to be created beforehand
# Images are pictures of the appearance of organic products
def download_organic_images(n=0):
    i = 0

    if n > 0:
        barcodes = organic_products(df).tail(n)['code']
    else:
        barcodes = organic_products(df)['code']
    
    length = len(barcodes)

    for code in barcodes:
        url = get_image_url(code)
    
        if url != 'No image available':
            save_image(code, url)
            i = i + 1
    
        progress = str(i) + '/' + str(length)
        print(progress, end='\r')
    
    print('Download completed!')