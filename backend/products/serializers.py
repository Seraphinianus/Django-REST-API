from rest_framework import serializers

from .models import Product

# You can have something like a PrimaryProductSerializer and a SecondaryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        print(obj.id)
        return obj.get_discount()