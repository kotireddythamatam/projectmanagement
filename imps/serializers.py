
# get model name from meta class model
from django.contrib.auth import get_user_model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username','email','password')
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance