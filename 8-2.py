from PIL import Image
holiday_cards ={'8 марта': '8_march.jpg',
                'День Победы': '9_may.jpg',
                'День Рождения': 'hb.jpeg'
                }
x = input('Введите праздник: ')
for key in holiday_cards:
    if key == x:
        y = Image.open(holiday_cards[key])
        y.show()

