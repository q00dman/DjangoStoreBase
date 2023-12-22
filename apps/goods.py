class Goods:
    def __init__(self):
        self.author = input('author: ')
        self.genre = input('genre: ')
        self.technique = input('technique: ')
        self.price = input('price: ')

    def dict_transform(self):
        goods_dict = {'author': self.author, 'genre': self.genre, 'technique': self.technique, 'price': self.price}
        return goods_dict

    def set_author(self, another_author):
        self.author = another_author

    def set_genre(self, another_genre):
        self.genre = another_genre

    def set_technique(self, another_technique):
        self.technique = another_technique

    def set_price(self, another_price):
        self.price = another_price

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def get_technique(self):
        return self.technique

    def get_price(self):
        return self.price
