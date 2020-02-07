from rest_framework.serializers import HyperlinkedModelSerializer
from UserProfile.models import UserModel, UserProfileManager


class UserSerializer(HyperlinkedModelSerializer):
        class Meta:
            model = UserModel
            fields = ( 'email', 'password', 'name')
            # extra_kwargs will enforce additional validations for the model feilds
            extra_kwargs = {
                'password':{
                    'write_only':True,
                    'style':{
                        'input_type':'password'
                    },
                },
            }
        
        # method to create user from the data validated.
        def create(self, validated_data):
            user = UserModel.objects.create(
                email = validated_data['email'],
                password = validated_data['password'],
                name = validated_data['name'],
            )
            return user

        