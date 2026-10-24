import json
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from buybooks.models import CartItem
from checkoutbook.models import Checkout
from registerbook.models import Book


def make_book(price):
    return Book.objects.create(
        title="Bring Me Back", author="B A Paris", rating=Decimal("3.8"), voters=1,
        price=Decimal(price), currency="SAR", description="-", publisher="-",
        page_count=1, genres="-",
    )


class CheckoutFlutterTest(TestCase):
    def test_total_keeps_cents(self):
        user = User.objects.create_user("buyer")
        CartItem.objects.create(user=user, book=make_book("30.71"), quantity=2, is_ordered=True)
        self.client.force_login(user)

        response = self.client.post(
            reverse("checkoutbook:checkout_flutter"),
            data=json.dumps({"alamat": "Jl. Test", "metode_pembayaran": "Transfer Bank", "total_harga": 61.42}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Checkout.objects.get(user=user).total_price, Decimal("61.42"))


class OrderJsonAllTest(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user("alice")
        bob = User.objects.create_user("bob")
        Checkout.objects.create(user=self.alice, alamat="Alamat Alice", metode_pembayaran="E-Wallet", total_price=Decimal("61.42"))
        Checkout.objects.create(user=bob, alamat="Alamat Bob", metode_pembayaran="Transfer Bank", total_price=Decimal("10.00"))

    def test_requires_login(self):
        response = self.client.get(reverse("checkoutbook:get_order_json_all"))
        self.assertEqual(response.status_code, 401)
        self.assertNotIn("Alamat", response.content.decode())

    def test_returns_only_own_orders(self):
        self.client.force_login(self.alice)
        response = self.client.get(reverse("checkoutbook:get_order_json_all"))

        self.assertEqual(response.status_code, 200)
        orders = response.json()
        self.assertEqual([order["fields"]["user"] for order in orders], ["alice"])
        self.assertEqual(orders[0]["fields"]["total_price"], 61.42)
