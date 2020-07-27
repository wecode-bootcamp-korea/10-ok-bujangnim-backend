
from django.shortcuts import render
# Create your views here.
import time
from bs4 import BeautifulSoup
from django.db.models.functions import Now
from django.http import HttpResponse
from selenium import webdriver
from board.models import Product, PriceBySize, Image, FaceType, FaceTypeProduct, HowToUse, Characteristic, Ingredient, \
    Usability
from main.models import Category
from sub.models import Subtitle
def get(request):
    driver = webdriver.Chrome(r'/Users/munyeonglee/chromedriver')
    driver.get('https://www.aesop.com/kr/c/skin/')
    time.sleep(3)
    items = []
    a = []
    for j in range(1,12):
        tt=f"/html/body/div[1]/div[10]/div/section/div[2]/div/div[{j}]/div/div[1]"
        k = driver.find_element_by_xpath(tt)
        t = k.find_element_by_class_name('CPSubcatIntroDescription-name').text
        
        y = k.find_element_by_class_name('CPSubcatIntroDescription-info').text
        
        z = k.find_element_by_class_name('CPSubcatIntroCTA-text').text
        


        #title = soup.find('h2',{'class': 'CPSubcatIntroDescription'})
        #print(len(title))
        #titl = soup.find('h2', {'class' : 'CPSubcatIntroDescription-name'}).text
        #print(len(titl))
    #class="CPSubcatIntroDescription-info"
    #/html/body/div[1]/div[10]/div/section/div[2]/div/div[1]/div/div[1]/div[1]/p
    #2번째 class="CPSubcatIntroDescription-info"
    #/html/body/div[1]/div[10]/div/section/div[2]/div/div[2]/div/div[1]/div[1]/p
    #클렌저
    #/html/body/div[1]/div[10]/div/section/div[2]/div/div[1]/div/div[1]/div[1]/button/h2
    #CPSubcatIntroDescription
    #/html/body/div[1]/div[10]/div/section/div[2]/div/div[1]/div/div[1]/div[1]
   



    #CPSubcatIntro CPBodyRow-intro
    #/html/body/div[1]/div[10]/div/section/div[2]/div/div[1]/div/div[1]
    #CPSubcatIntro CPBodyRow-intro
    #/html/body/div[1]/div[10]/div/section/div[2]/div/div[2]/div/div[1]
   
    
    
    for i in range(1, 12):
        #CPBodyScrollable-wrapper 여기 찍었고
        src = f"/html/body/div[1]/div[10]/div/section/div[2]/div/div[{i}]/div/div[2]/div[1]"
        item = driver.find_element_by_xpath(src)
        items.append(item)
        
    for i in items:
        arr = i.find_elements_by_class_name('CPSubcatProduct-wrapper')
        for b in arr:
            a_src = b.find_element_by_tag_name('a').get_attribute('href')
            a.append(a_src)
    for link in a:
        try:
            driver.get(link)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            type = soup.find('nav', {'class': 'PDP-Breadcrumbs'}).find_all('li')[1].find('a').text


            title = soup.find('h1', {'class': 'PDPHeaderCommonSummary-title'}).text


            description = soup.find('p', {'class': 'PDPHeaderCommonSummary-description'}).text


            size_arr = soup.find('ul', {'class': 'PDPHeaderSolo-productVariants'}).find_all('li')


            size = []
            price = []
            skin_type = []


            if len(size_arr) == 1:
                size.append(size_arr[0].text)
                price_arr = soup.find('span', {'class': 'Btn-label'}).text.split(' — ')
                price.append(price_arr[-1])
            else:
                for c in size_arr:
                    size.append(c.find('span', {'class': 'FormRadio-label'}).text)
                    price_arr = soup.find('span', {'class': 'Btn-label'}).text.split(' — ')
                    price.append(price_arr[-1])
                    checkbox = driver.find_elements_by_class_name('FormRadio-input')
                    checkbox[1].click()
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
            exp_list = soup.find('ul', {'class': 'PDPHeaderCommonProductDetails-list'}).find_all('li')


            skin_types = exp_list[0].find('div', {'class': 'PDPHeaderCommonProductDetails-itemDescription'}).text
            if ',' in skin_types:
                skin_type = skin_types.split(', ')
            else:
                skin_type.append(skin_types)
            usability = exp_list[1].find('div', {'class': 'PDPHeaderCommonProductDetails-itemDescription'}).text
            main_ingredient = exp_list[2].find('div', {'class': 'PDPHeaderCommonProductDetails-itemDescription'}).text
            ingredient_detail = soup.find('p', {'class': 'PDPHeaderCommonIngredientOverlay-list'}).text
            how_to_use = soup.find('h2', {'class': 'PDPExpectationsContentSummary-title'}).text
            how_to_use_arr = soup.find('ul', {'class': 'PDPExpectationsContentList-details'}).find_all('li')
            use_amount = how_to_use_arr[0].find('span', {'class': 'PDPExpectationsContentList-detailDescription'}).text
            texture = how_to_use_arr[1].find('span', {'class': 'PDPExpectationsContentList-detailDescription'}).text
            smell = how_to_use_arr[2].find('span', {'class': 'PDPExpectationsContentList-detailDescription'}).text
            #recommendation = soup.find('p', {'class': 'MCItemCarouselIntro-copyParagraph'}).text
            
            main_img = \
            soup.find('picture', {'class': 'PDPHeaderCommonProductImage-productPicture'}).find_all('source')[-1][
                'srcset']
            
            main_img = 'https://www.aesop.com' + main_img[:-2]
            
            play_btn = soup.find('span', {'class': 'PDPExpectationsVideo-controlsButton'})
            
            if play_btn is not None:
                sub_img = 'https://www.aesop.com' + \
                          soup.find('picture', {'class': 'Picture PDPExpectationsVideo-fauxPosterImage'}).find_all(
                              'source')[2]['srcset']
            else:
                sub_img = 'https://www.aesop.com' + \
                          soup.find('picture', {'class': 'PDPExpectations-fullImage'}).find_all('source')[2]['srcset']
            
            
            if Product.objects.filter(name=title.strip()).exists():
                pass
            else:
                category_id = Category.objects.get(name=type.strip()).id
                product = Product(
                    category_id = category_id,
                    name=title,
                    description=description,
                    is_activated='Y',
                    created_at=Now(),
                    updated_at=Now()
                )
                product.save()
                for a in range(0,11):
                    Subtitle(
                        name = t[a],
                        subscription = y[a],
                        number = z[a],
                        cate = category_id,
                        is_activated='Y',
                        created_at=Now(),
                        updated_at=Now()
                    ).save()
                # for num in range(0, len(size)):
                #     PriceBySize(
                #         product_id=product.id,
                #         price=price[num],
                #         size=size[num].strip(),
                #         is_activated='Y',
                #         created_at=Now(),
                #         updated_at=Now()
                #     ).save()
                # Image(
                #     product_id=product.id,
                #     image_url=main_img,
                #     sub_image_url=sub_img,
                #     is_activated='Y',
                #     created_at=Now(),
                #     updated_at=Now()
                #).save()
                # for face_type in skin_type:
                #     if FaceType.objects.filter(name=face_type.strip()).exists():
                #         pass
                #     else:
                #         FaceType(
                #             name=face_type.strip(),
                #             is_activated='Y',
                #             created_at=Now(),
                #             updated_at=Now()
                #         ).save()
                #     face_id = FaceType.objects.get(name=face_type.strip()).id
                #     FaceTypeProduct(
                #         product_id=product.id,
                #         faceType_id=face_id,
                #         is_activated='Y',
                #         created_at=Now(),
                #         updated_at=Now()
                #     ).save()
                # HowToUse(
                #     product_id=product.id,
                #     method=how_to_use,
                #     amount=use_amount,
                #     is_activated='Y',
                #     created_at=Now(),
                #     updated_at=Now()
                # ).save()
                # Characteristic(
                #     product_id=product.id,
                #     texture=texture,
                #     smell=smell,
                #     is_activated='Y',
                #     created_at=Now(),
                #     updated_at=Now()
                # ).save()
                # Ingredient(
                #     product_id=product.id,
                #     main_ingredient=main_ingredient,
                #     ingredient=ingredient_detail,
                #     is_activated='Y',
                #     created_at=Now(),
                #     updated_at=Now()
                # ).save()
                # Usability(
                #     product_id=product.id,
                #     usability=usability,
                #     is_activated='Y',
                #     created_at=Now(),
                #     updated_at=Now()
                # ).save()
        
        except Exception as ex:
            print(ex)
            continue
    return HttpResponse('a')
