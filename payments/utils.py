import stripe
from django.conf import settings


class Payment:
    stripe.api_key = settings.STRIPE_KEY_SECRET

    def createSession(self, amount, user):
        payment_method_types, success_url,  cancel_url, line_items, mode, product_id = self.construct_item(
            user.get_full_name(), user.avatar.url, amount)
        session = self.createStripeSession(
            success_url, cancel_url, payment_method_types, line_items, mode)
        return session['id'], product_id

    def createStripeSession(self, success_url, cancel_url, payment_method_types, line_items, mode):
        return stripe.checkout.Session.create(
            success_url=success_url,
            cancel_url=cancel_url,
            payment_method_types=payment_method_types,
            line_items=line_items,
            mode=mode,
        )

    def createProduct(self, name, avatar):
        return stripe.Product.create(name=name)['id']

    def createPrice(self, product_id, amount, currency,):
        return stripe.Price.create(
            unit_amount=amount,
            currency=currency,
            product=product_id,
        )['id']

    def construct_item(self, name, avatar, amount):
        product_id = self.createProduct(name, avatar)
        price_id = self.createPrice(product_id, amount, "gbp")
        return (["card"],
                f'{settings.DOMAIN}/payments/paymentsuccessfull/{product_id}/',
                f'{settings.DOMAIN}/payments/paymentcancel/{product_id}/',
                [
                    {
                        "price": price_id,
                        "quantity": 1,
                    },
        ], "payment", product_id)
