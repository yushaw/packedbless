import Amazon.gifts as gifts
import re
import csv
import dataProcess.llmApi as llm
import requests
from PIL import Image
from io import BytesIO
import os

def process_product_links_and_generate_csv(product_links, csv_file="products_data.csv"):
    products_data = []
    for link in product_links:
        product_data = grab_link(link)
        products_data.append(product_data)

    # 将数据写入 CSV 文件
    csv_columns = list(products_data[0].keys()) if products_data else []

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in products_data:
            writer.writerow(data)

    print(f"CSV file '{csv_file}' has been created with product data.")
    

def grab_link(product_link):
    details = gifts.get_details(product_link)
    SKU = details["SKU"]
    Name = llm.generateShortTitleAPI(details["标题"])
    Short_description = llm.generateShortDescriptionAPI(details["描述"])
    
    url_formatted_text = Name.lower()
    url_formatted_text = re.sub(r'[^\w\s]', ' ', url_formatted_text)
    url_formatted_text = re.sub(r'\s+', ' ', url_formatted_text).strip()
    url_formatted_text = url_formatted_text.replace(" ", "-")
    
    images = "https://www.packedbless.com/wp-content/uploads/"+ url_formatted_text + ".jpg"
    
    
    img_url = details["image_product"]  # 这里应替换为实际的图片URL变量
    print(img_url)
    img_response = requests.get(img_url)

    if img_response.status_code == 200:
        # 创建 images 目录（如果不存在）
        if not os.path.exists('images'):
            os.makedirs('images')

        # 提取图片名称和格式
        img_name = url_formatted_text # 您可以根据需要更改图片名称
        img_format = img_url.split('.')[-1].lower()

        # 检查格式并进行必要的转换
        if img_format not in ['jpg', 'jpeg']:
            try:
                # 将非JPG图片转换为JPG
                img = Image.open(BytesIO(img_response.content))
                img.convert('RGB').save(f'images/{img_name}.jpg', 'JPEG')
            except Exception as e:
                print(f"Error converting image to JPG: {e}")
        else:
            # 直接保存为JPG
            with open(f'images/{img_name}.jpg', 'wb') as f:
                f.write(img_response.content)
    else:
        print(f"Error downloading image: HTTP {img_response.status_code}")
        
        
    Description = details["描述"]
    Regular_price = details["价格"]
    # Categories = f"{details['分类1']}>{details['分类2']}>{details['分类3']}"
    External_URL = details["地址"]
    Button_text = "Check it out"
    Type = "external"
    Published = 0
    Is_featured = 0
    Visibility_in_catalog = "visible"
    Tax_status = "taxable"
    In_stock = 1
    Backorders_allowed = 0
    Sold_individually = 0
    Allow_customer_reviews = 0
    Position = 0
    Meta_wp_page_template = "default"
    Meta_rh_woo_product_layout = "global"
    Meta_yoast_wpseo_metadesc = Short_description
    
    return {
        "SKU": SKU,
        "Type": Type,
        "Name": Name,
        "Short description": Short_description,
        "Description": Description,
        "Regular price": Regular_price,
        "Categories": "",
        "External URL": External_URL,
        "Button text": Button_text,
        "Published": Published,
        "Tags": "",
        "Images": images,
        "Is featured?": Is_featured,
        "Visibility in catalog": Visibility_in_catalog,
        "Tax status": Tax_status,
        "In stock?": In_stock,
        "Backorders allowed?": Backorders_allowed,
        "Sold individually?": Sold_individually,
        "Allow customer reviews?": Allow_customer_reviews,
        "Position": Position,
        "Meta_wp_page_template": Meta_wp_page_template,
        "Meta_rh_woo_product_layout": Meta_rh_woo_product_layout,
        "Meta_yoast_wpseo_metadesc": Meta_yoast_wpseo_metadesc
    } 

# Type,SKU,Name,Published,"Is featured?","Visibility in catalog",
# "Short description",Description,
# "Tax status","In stock?",
# "Backorders allowed?","Sold individually?","Allow customer reviews?",
# "Regular price",Categories,Tags,Images,
# "External URL","Button text",Position,
# "Meta: _wp_page_template", "Meta: _yoast_wpseo_focuskw",
# "Meta: _yoast_wpseo_metadesc",




product_links = ["https://www.amazon.com/Viva-Naturals-Organic-Virgin-Coconut/dp/B00DS842HS/ref=sr_1_1?qid=1699717697&sr=8-1&srs=82836043011&th=1"]  # 替换为实际链接
csv_file_name = "products_data.csv"
process_product_links_and_generate_csv(product_links, csv_file_name)
