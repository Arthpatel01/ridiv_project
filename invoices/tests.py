from _decimal import Decimal
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail


class InvoiceApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2023-09-20', 'customer_name': 'John Doe'}
        self.invoice = Invoice.objects.create(**self.invoice_data)

        self.detail_data = {
            'invoice': self.invoice.id,
            'description': 'Product 1',
            'quantity': 5,
            'unit_price': 10.99,
            'price': 54.95,
        }

    def test_create_invoice(self):
        response = self.client.post('/api/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)

    def test_retrieve_invoice(self):
        response = self.client.get(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        updated_data = {'date': '2023-09-21', 'customer_name': 'Updated Customer'}
        response = self.client.put(f'/api/invoices/{self.invoice.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice.refresh_from_db()
        self.assertEqual(str(self.invoice.date), '2023-09-21')
        self.assertEqual(self.invoice.customer_name, 'Updated Customer')

    def test_delete_invoice(self):
        response = self.client.delete(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)

    def test_list_invoices(self):
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class InvoiceDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2023-09-20', 'customer_name': 'John Doe'}
        self.invoice = Invoice.objects.create(**self.invoice_data)

        self.detail_data = {
            'invoice': self.invoice,
            'description': 'Product 1',
            'quantity': 5,
            'unit_price': 10.99,
            'price': 54.95,
        }

    def test_create_invoice_detail(self):
        invoice_id = self.invoice.id
        self.detail_data['invoice'] = invoice_id

        response = self.client.post('/api/invoice-details/', self.detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 1)

    def test_retrieve_invoice_detail(self):
        invoice_detail = InvoiceDetail.objects.create(**self.detail_data)
        response = self.client.get(f'/api/invoice-details/{invoice_detail.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice_detail(self):
        invoice = Invoice.objects.create(date='2023-09-20', customer_name='John Doe')

        detail_data = {
            'invoice': invoice,
            'description': 'Product 1',
            'quantity': 5,
            'unit_price': 10.99,
            'price': 54.95,
        }

        invoice_detail = InvoiceDetail.objects.create(**detail_data)

        updated_data = {
            'invoice': invoice.id,
            'description': 'Updated Product 1',
            'quantity': 10,
            'unit_price': 15.99,
            'price': 159.90,
        }

        response = self.client.put(f'/api/invoice-details/{invoice_detail.id}/', updated_data, format='json')

        print(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        invoice_detail.refresh_from_db()
        self.assertEqual(invoice_detail.description, 'Updated Product 1')
        self.assertEqual(invoice_detail.quantity, 10)
        self.assertEqual(invoice_detail.unit_price, Decimal('15.99'))
        self.assertEqual(invoice_detail.price, Decimal('159.90'))

    def test_delete_invoice_detail(self):
        invoice_detail = InvoiceDetail.objects.create(**self.detail_data)
        response = self.client.delete(f'/api/invoice-details/{invoice_detail.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(InvoiceDetail.objects.count(), 0)

    def test_list_invoice_details(self):
        response = self.client.get('/api/invoice-details/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
