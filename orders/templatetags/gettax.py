from django import template

register=template.Library()

@register.simple_tag(name='gettax')
def gettax(cart):
    total = 0
    tax = 0
    for item in cart.added_items.all():
        total += item.quantity*item.product.price
        tax = (total * 9)/100
    return tax