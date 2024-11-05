class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'