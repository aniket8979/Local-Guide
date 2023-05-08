from rest_framework import serializers
#from . models import *
from . models import React


class ReactSerializer(serializers.ModelSerializer):
	class Meta:
		model = React
		fields = ['name', 'detail']
