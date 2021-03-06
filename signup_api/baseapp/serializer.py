from rest_framework import serializers
from .models import Courses, User , CoursesInstances

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','name','email','password','branch','cgpa']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#         def create(self, validated_data):
#             password = validated_data.pop('password', None)
#             instance = self.Meta.model(**validated_data)
#             if password is not None:
#                 instance.set_password(password)
#             instance.save()
#             return instance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class CourseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesInstances
        fields = '__all__'


class CourseNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('courseName',)