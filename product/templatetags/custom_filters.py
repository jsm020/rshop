from django import template

register = template.Library()

@register.filter
def to(value, arg):
    return range(value, arg + 1)
@register.filter
def summ(cart):
    return sum(item.total_price() for item in cart.items.all())
