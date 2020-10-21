from django import template

from recipes.models import Wishlist

register = template.Library()


@register.filter
def wishlist_count(user):
    """Вычисляет колличество рецептов в списке покупок"""
    return Wishlist.objects.filter(user_id=user.id).count()
