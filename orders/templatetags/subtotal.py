from django import template

register=template.Library()

@register.simple_tag(name='subtotal')
def subtotal(cart):
    subtotal = 0
    for item in cart.added_items.all():
        subtotal += item.quantity*item.product.price
    return subtotal