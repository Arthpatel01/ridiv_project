# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Invoice, InvoiceDetail
# from .serializers import InvoiceSerializer, InvoiceDetailSerializer
#
#
# # Create your views here.
#
#
# class InvoiceViewSet(viewsets.ModelViewSet):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer
#
#
# class InvoiceDetailViewSet(viewsets.ModelViewSet):
#     queryset = InvoiceDetail.objects.all()
#     serializer_class = InvoiceDetailSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import CombinedSerializer

class InvoiceAPIView(APIView):
    def get(self, request, *args, **kwargs):
        invoices = Invoice.objects.all()
        invoice_details = InvoiceDetail.objects.all()

        serializer = CombinedSerializer({'invoices': invoices, 'invoice_details': invoice_details})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CombinedSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            try:
                instance = InvoiceDetail.objects.get(pk=kwargs['pk'])
            except InvoiceDetail.DoesNotExist:
                return Response({'error': 'InvoiceDetail not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                instance = Invoice.objects.get(pk=request.data['pk'])
            except Invoice.DoesNotExist:
                return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CombinedSerializer(instance, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        invoice_id = request.query_params.get('invoice')
        if 'pk' in kwargs:
            try:
                instance = Invoice.objects.get(pk=kwargs['pk'])
            except Invoice.DoesNotExist:
                return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)

        else:
            try:
                instance = InvoiceDetail.objects.get(pk=kwargs['pk'])
            except InvoiceDetail.DoesNotExist:
                return Response({'error': 'InvoiceDetail not found'}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
