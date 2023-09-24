from rest_framework import serializers
from .models import Invoice, InvoiceDetail


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class CombinedSerializer(serializers.Serializer):
    invoices = InvoiceSerializer(many=True, read_only=True)
    invoice_details = InvoiceDetailSerializer(many=True, read_only=True)

    def create(self, validated_data):
        request_data = self.context['request'].data

        if 'date' and 'customer_name' in request_data:
            invoice_obj = Invoice.objects.create(date=request_data['date'], customer_name=request_data['customer_name'])
            if 'details' in request_data and request_data['details']:
                detail_obj = InvoiceDetail.objects.create(**request_data['details'][0], invoice=invoice_obj)
            return invoice_obj

    def update(self, instance, validated_data):
        request_data = self.context['request'].data

        if 'pk' in request_data:
            if 'customer_name' in request_data:
                instance.customer_name = request_data['customer_name']
            if 'date' in request_data:
                instance.date = request_data['date']
            instance.save()

        if 'details' in request_data and request_data['details']:
            d = request_data['details'][0]
            try:
                instance = InvoiceDetail.objects.update(**d)
            except:
                pass

        return instance

