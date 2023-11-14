from models import Product, Category,User
from flask_login import LoginManager
import hashlib
def load_categories():
    return Category.query.all()
    # return [{
    #     "id" : 1,
    #     "name" : 'Mobile'
    # }, {
    #     "id" : 2,
    #     "name" : 'Tablet'
    # }]


def load_products(kw = None):
    # Lấy tất  cả product
    products = Product.query
    # products = [{
    #     "id": 1,
    #     "name": 'Galaxy S30',
    #     "price" : 30000000,
    #     "image" : 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxITEhUSEhIVFRUVFxUVFxUYFRUVFRUVFxUYFhcVFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OEA8NFSsZFR0rLS0tKysrKysrKysrKysrLS03LTcrKy0rKysrKzgrKy0tLSsrLSstLi0rLS0tNy0rN//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAABQYCAwQBBwj/xABNEAACAQIBBQcPCAkDBQAAAAAAAQIDEQQFEiExQQYHUWFxkbMTFyI1VHOBk6GxssHR0vAlMkJSU3KDoxQWIyQzYmOS4YK04hVEosPE/8QAFwEBAQEBAAAAAAAAAAAAAAAAAAECA//EABsRAQEBAQADAQAAAAAAAAAAAAABETEhQXEC/9oADAMBAAIRAxEAPwD7iAAAAAAHDjcr0KTtUqxT2rXJcbirtIDuBAy3Y4JO3Vn4uq/Lmnn65YL7Z+Lq+6BPggP1ywX2z8XV90frlgvtX4qr7oE+CA/XPBfbPxdX3Tz9c8D9s/F1fdAsAK8922B+2fiqvump7v8AJy14i3G6dVRXLLMsgLMCrPfDyX3ZT5pewdcTJfdlPml7ALSCrPfEyX3ZT5peww65WSe7qXO/YBbAVPrlZJ7upc79hn1xMl92U+aXsAtIKt1w8l92U+aXsC3xMl3t+mQ5p+ewFpBE5O3TYOu0qWIpyb1LOs5PgipWv4CWAAAAAAAAAAAAAAK5uyy46EFCD7Oa2a0tStwX06VqtsbTKPjlSoKMsW51K1SLnHD083OUL2dSbk1GnC7+dJpX0K70EpuhqqWVFGfzYZnMqaqeds+PbsMvVKzcr9liJSqze3NUnCjT+7GmkrcOd9ZgWHGbp6LlmrDUVst+kuUvJFaeQ0/9cj3LT8bU9h8+jRdk9j0fCJHC4p5ul/NajfhTTtzZr51wFwW+OWE3ZYSDv/Wqew1ZSxMoa6EqV9XZykn4JxXkODIeUY0q0Jz+anp0Xtoavbba9yybu90mErUI06ElOrKcZPNTzYJXu3dLNunm5vGQQuBykpvNevZxnZJlVjKzzlri1LwXSfnRZVO6TIIvK2MnnKlS+fK+l6VGK1ya4PO+Zxkslpy7K9Sb+lJt+TVYmcl4fOxFaW2NOml/rcpvzHPiayU5cvxympB7h8h0EtME3xpeY6FknDrR1KH9q85pji+PgM1ijSI7LdXD0HGKw8JSld2sklHVfVrv5iLjlij3HT5/+JM5QwtOtbPveN7NOz5NKs0ci3PUPrVP7o+6Sq4lluj3FS517pMZFnhq7knhqcJR02tFpp31NJbfV4OaO5yg/p1P7o+6SmTMDTo3zLty1yelu2patWkRHZDJGH+xh/YmuY2U8j4bR+wp6f5E+L1Mzp1L2+PhnRCRocFbc3Qd3TUqM9koNq3LG9mr7NF+I+h70W6+vOc8nYyWdVpK9Oo/pxte19ujslwWktGhFThrWnl+NphkOWZlnBTjrksx8nVFHzVGifqEfoIAGFAAAAAAAAAAB8q3UO2VKvJ/80T43jsM5Rg1paVrcK16OF3vo234j7DusfynV5F/tkfLMPhJVIpRV7RTbbSjFaryb0L1gQVOLvmpO/BbSZ1WlaCd9N5PZdXSS5Lvybbo6sVQV3FV4y2WU5W5OySRrpYfNelaVsKjuxlaGHioOKnWaTlnPsKV/o2+lLhvx6rJyjYZSu9MYtfyrNa9T+NJhlKb6tKet56npSaepxbT0PRYwqQunOT7OT1cPC2M8K7+qJKfHHRx3cWnzFkpPsFyFOrXjmx2pJPwyk7czXOW+k+wXIQdO5OjnV8Sv6eG8F4zZWcryzatRcEmvKXHcHG+IxPe8N6MyC3w8lulX6ok8yppT49qNehXliTdHFcZFORnGoQTEcSbY1yIjUN8aw0S8Kxtp1mRUKpvp1S6JalWOqlW9vxzIhoVTrpzLqJinVMskSvlbAff/wDbTI+nUOrc9K+VcD95dLTF4P0aADCgAAAAAAAAAA+SbsZWynV5F/tonyTK2Nao06MdCcXOf80rtJPiSVufhZ9O3x5NY+s1rXU3+TD1HyzH0c7VrjdWei8W725b35bvgAjIU5aHdO6vo2aWrPgei/hR10avYq/0WorkabS8Gb/5DDxqRTjGLV9d014WjCs4q0Iu9tLfC9luS75+Ivwb6yTSur21NOzXFxri8xzwqKOmMW3sb0W8Cbv5DZVvmu2s58HF3fBYg2U6Ld5PXr+Oct0PmLkI1ZPcYRUtE6rTUdsaa050uDO2LgSe0lJKyAldwkl+k4rjhhtWr5s/IWTL+T416Uqc9up8D2SXBq85VdxLtiMSno7DDejPQXKtU0G5xHxXLeR6mHm4yV1fRK2hr1PiIxH2XKOHhUi4zipJ31+18p8/y5uVnBudG84a7fSS12S26yWGq2pG2NQ55JoKRlXbCodFOqR0Jm+EwJSlUO2lIiKNQ7qNQok6bO7cz21wP310tMjKUyR3Lv5VwX349JTLR+kwAZAAAAAAAAAAAfF98Z/v9b8PooFFyjklT7KLsy4bu3+/4j766KmQFyCqVci1tV00bcPkma1xT8NvUWVsXAg/0Cf2a/uZvwuFqRaahBNam7ytxpPbxkrcXA00qFm5Sk5TlpcnpbPaupmxs1VQOvcrO2IxP3MP5plkq4j4+PDzFT3NT/b13/Tw/ozJevWOk4jprV/V5uE0vEez16ufnOCdfSaXieMaGVch0a1382Wm0lo51tRTsq5Bq0dLWdH6y4ONbC4vFfHBo4fCbVi7q2zz7fjlGD5qjZCRcspZBpVbuFqcuL5rb2NevjKpjsn1KLtOPJJaYvkfqM2Lr2nI7KMyMhM66UyKmKNQmNycr5VwX349LArlGZL7l5/KWE+/DpqZUfqEAEAAAAAAAAAAAfC93b/f8R3xdFTIC5YN38HHH4i+2cWuR0qdiu3IMrnlzy55cDK4uY3FwPWzVVegzbNVXUBnkaX7xiH/ACUPNM7sRUI/IOmtXf8AJh/Rmd2LiaHDUqGiVUyrM5JyKN3VjJ1zhlI8VQIko4s2utGcXGaTT1rZw+ciFVM4VfjwDRHZWyU6fZw0w8seXhXGcFKZaY1rqz0pq2ng8PgK9lLB9Tlo1PVxcRLFbaNQnNyMvlHCffp9NTK1RmWLcQnLKWFS19Uh01NkH6pAAAAAAAAAAAAAfEd8vthW/D6KBVrlo3zX8oVvw+igVS5BlcXMbi4GVzxzXCYVJ2TfAmyHlK+l6WUScpyz9LzYrjtnMzmyHbJKnDNikB2bmo3rV+94f0Zkpi4EduU/jV+94f0Zkxi4hVfxMSPqslMWiLrsDmmzW5CozTKRUbc89UznzjJSA66VQzxSU4NeFcN1p8uk41I2wqc3xwFRGQRZd7ztphO+Q6SBBVodk3x3J3e+7aYTvkOkgRX6nABAAAAAAAAAAAHw7fO7YVvw+igVS5at8/thW/D6KBU7kHtxcxuLgeyV01w6CGmmm09aJi5qq0Iyd2vUURTZ34WbcdPIuQ2TwsH9HmbPZarASW5D+NX73hvRmTOMIXck/wBriO94b0ZkvjJayKhMYRFdkpjJERiGByVGaJSM6rOeUijJyPVI05x4pBHRnG2EtOv48JyqRuo6yjdNX+P8kzuBXyphO+Q6WBGuOi/F5NhKbg18qYTvkOlgB+owAQAAAAAAAAAAB8M30O2Nb8PooFSuWvfS7Y1vw+igVK5Blc8ueXFwMrnlzy4uAbNc2ZtmubA7dzErVa/e8P6MiUxdQhMgztVrd7w/oyOzF1wrjxcyJryOjFViNrVANVWRzykZTkaZMD24TMLhMqN0Wd2Dp3aOClG5ZsmYTNjnSWvV8eEo0V420fHgO7cJ21wnfIdJA48S18es7dw3bXCd8h0kBR+oQAQAAAAAAAAAAB8J30+2NX8PooFRuW3fUfyjV5KfRQKhcgyFzG4uBlcXMbi4HtzXMybMJsDzJ9S1Wp3uh6MjLFVzjhO1Wfe6Pos04isFa8RWOKpMVahocij1sxbPLgDxmUI31HfkvI9Wu7Qi7bZakvCXXJW5qlQtKdpzWm/0VbyFxELkLc+7KpVVlsWi75VsJTHTSutmr/B3Y3Fa/jzFfxeIvrKjmxEiQ3DP5VwnfIdJAhK1UltwEr5UwnfIdLAiv1MACAAAAAAAAAAAPg++q/lGtyU+igU+5bt9btjW5KfRQKfcgyuLmNxcDK4uY3FwPWzCbPbmE2BH4idqku90vROKtUN+Ol+0fe6XonDNlGMmeWO7JWSquImoUoOT2v6MeOT2I+i5E3CUaNpYhqrP6tv2afBo+d4dZcHz/JWQa9f+HB5v1n2Medl2yVuHpUrSrS6pL6qVop349aLVWxMYq0c1LgSUVbbexE4vH635dHk5vIXEbaleNOKjC0YrZZ21bFfWQ+LxvH5zRi8Xfb5yHxeJvtAzxeK1/wCCKxFc8rVTjqTIr2dQnd7qXyphe+Q6SBWZzLFvav5UwvfKfSwIP1eAAAAAAAAAAAAA+Cb6/bKtyU+igU+5bt9h/KVbkp9FAp5B6LngA9ue3MQB6zCZ6zCQETlD+J+HT9Ekdyu52WLqWvm042c521J7Fxuz5DixMb1X9yl6J9DyJBYfDQirJtZ0noveVuPZq+NGoJyhGjh6cadGEYx4rXk9GmTelvRt9Rw4vKbe3XwefyIisZlLW+X1EXiMX8eDa+YqJPFY699Ptt8esjK2M4WcFbEvh/wckqxB0Vq5xVpnk6hzVJhWNSZy1JGc5GhsDGTLLvZdtML32n0sCtWLNvbK2VMJ32n0sCD9YAAAAAAAAAAAAAPg2+9Sccozb+nCnNcmbmeemylH3TfS3IzxlKNagr16KfY/aU3pcU/rJ6VytbT4bUpyi3GUXFp2aaaaa1pp6nxAYnp5cXIPQeXFwBhIzMWBz4SGdWtwwhzRk4snMqY9p21JLR69nEQNTOjKNSFs6Lur6mnolFvYnw7HzrLKmPpzSk86nPbCafklazWrSaHTPG3d7mieIIj9MX1lzhYxfWQEjOqaZVDleJj9Zc5reIj9ZAdMqhqnM09XjwodVj9ZAeyMLHvVI/WR51SPCucDKKLVvY0HPKuFUdalGT/0yU35IMqtNuTtFOT4EvO9h943ldwdTDXx2Kjm1JxtTptWcYvXNp6U7aEuByvrRB9aAAAAAAAAAAAAACOylkLC13etQpzlqznFZ1uDOWm3hJEAVl7gMmv/ALb82t7551v8m9zfm1vfLOAKx1v8m9zfm1vfHW/yb3N+bW98s4ArHW/yb3N+bW98db7Jvc35tb3yzgCrve9yZ3N+bW98wW9zktasL+bXtzZ5awBVXvc5L7lXjK3vjrc5L7lXjK3vlqAFV63OS+5V4yt7463OS+5V4yt75agBVetzkvuVeMre+OtzkvuVeMre+WoAVXrc5L7lXjK3vhb3WS+5V4yt75agBEZN3MYOg1KjhqcZLVLNzpLklK7RLgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAf/9k='
    # }, {
    #     "id": 2,
    #     "name": 'iPhone 15',
    #     "price" : 15000000,
    #     "image" : 'data:image/jpeg;base64,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'
    # }, {
    #     "id": 3,
    #     "name": 'iPhone 15 Promax',
    #     "price" : 25000000,
    #     "image" : 'data:image/jpeg;base64,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'
    # }, {
    #     "id": 4,
    #     "name": 'iPad Pro',
    #     "price" : 29000000,
    #     "image" : 'data:image/jpeg;base64,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'
    # }, {
    #     "id": 4,
    #     "name": 'Tablet GLX',
    #     "price" : 24000000,
    #     "image" : 'data:image/jpeg;base64,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'
    # }]

    if kw:
        products = products.filter(Product.name.contains(kw))
    # products = products lọc ra 'name' có chứa keywork và return về giá trị cần tìm
    return products.all()

def get_user_id(id):
    return User.query.get(id);

def auth_user(username,password):
    password=str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),User.password.__eq__(password.strip())).first()