
from django.db.models import Q
from rest_framework import serializers

from main.models import *


class AboutUsImageSerializer(serializers.ModelSerializer):
    """О нас"""

    class Meta:
        model = AboutUsImage
        fields = ('image',)


class AboutUsSerializer(serializers.ModelSerializer):
    """О нас"""
    images = AboutUsImageSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = ('title', 'text', 'images')


class BenefitSerializer(serializers.ModelSerializer):
    """Наши преимущества"""

    class Meta:
        model = Benefit
        fields = ('icon', 'title', 'description')



class NewsSerializer(serializers.ModelSerializer):
    """Новости"""
    class Meta:
        model = News
        fields = ('title', 'description', 'image')



class OferroSerializer(serializers.ModelSerializer):
    """Публичная оферта"""
    class Meta:
        model = Oferro
        fields = ('title', 'description')



class ImageHelpSerializer(serializers.ModelSerializer):
    """Фотография для помощи"""
    class Meta:
        model = ImageHelp
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    """Помощь"""
    class Meta:
        model = Help
        fields = '__all__'



class CollectionSerializer(serializers.ModelSerializer):
    """Коллекция"""
    class Meta:
        model = Collection
        fields = ('id', 'image', 'title')



class SliderSerializer(serializers.ModelSerializer):
    """Слайдер"""
    class Meta:
        model = Slider
        fields = '__all__'


class BackCallSerializer(serializers.ModelSerializer):
    """Обратный звонок"""
    class Meta:
        model = BackCall
        fields = ('id','name', 'number_of_phone')

class BackCallPostSerializer(serializers.ModelSerializer):
  class Meta:
        model = BackCall
        fields = ('name', 'number_of_phone', 'date_of_call', 'status')


class ProductImageColorSerializer(serializers.ModelSerializer):
    """Фотография и цвет для товара"""
    class Meta:
        model = ProductImageColor
        fields = ('image', 'color')



class ProductSerializer(serializers.ModelSerializer):
    """Товар"""
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('collection', 'title', 'article', 'old_price', 'discount', 'new_price',
                  'description', 'size', 'line_of_size', 'compound', 'amount', 'material', 'favorite', 'images')


class SimilarProductSerializer(serializers.ModelSerializer):
    """Похожие товары"""
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'discount', 'new_price',
                  'size', 'favorite', 'images')


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)
    similar = serializers.SerializerMethodField('get_similar_product')

    class Meta:
        model = Product
        fields = ('collection', 'title', 'article', 'old_price', 'discount', 'new_price',
                  'description', 'size', 'line_of_size', 'compound', 'amount', 'material', 'favorite', 'images',
                  'similar')

    def get_similar_product(self, obj):
        similar = Product.objects.filter(Q(collection=obj.collection) & ~Q(id=obj.id))[:5]
        similar_data = SimilarProductSerializer(similar, many=True)
        return similar_data.data


# Детализация коллекции
class CollectionProductSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Collection
        fields = ('id', 'image', 'title', 'products')

    def get_products(self, obj):
        products = Product.objects.filter(collection=obj.id)
        products_data = ProductSerializer(products, many=True)
        return products_data.data


# Новинки
class NewProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'new_price', 'discount', 'size', 'favorite', 'images')


# Хит продаж
class HitProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'new_price', 'discount', 'size', 'favorite', 'images')


class FavoriteSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)
    count_favorite = serializers.SerializerMethodField('get_favorite_count')

    class Meta:
        model = Product
        fields = ('id', 'discount', 'old_price', 'new_price', 'title', 'size', 'favorite', 'images', 'count_favorite')

    def get_favorite_count(self, obj):
        count_fav = Product.objects.filter(favorite=True)
        count_fav_data = ProductSerializer(count_fav, many=True)
        return len(count_fav_data.data)


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ('logo','imformation', 'number')


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ('number',)


class SecondFooterSerializer(serializers.ModelSerializer):

    class Meta:
        model = SecondFooter
        fields = ('messen', 'link')





