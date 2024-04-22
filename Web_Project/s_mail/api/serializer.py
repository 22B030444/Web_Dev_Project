from rest_framework import serializers
from . import models


class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField(max_length=255)
    body = serializers.CharField()
    sender = serializers.PrimaryKeyRelatedField(queryset=models.User.objects.all())
    recipient = serializers.PrimaryKeyRelatedField(queryset=models.User.objects.all())
    sent_at = serializers.DateTimeField(read_only=True)
    read = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return models.Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.body = validated_data.get('body', instance.body)
        instance.sender = validated_data.get('sender', instance.sender)
        instance.recipient = validated_data.get('recipient', instance.recipient)
        instance.read = validated_data.get('read', instance.read)
        instance.save()
        return instance

