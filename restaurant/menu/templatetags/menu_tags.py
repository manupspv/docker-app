from django import template

register = template.Library()

@register.filter
def make_newlist(length):
    n_list = []
    for i in range(length):
        n_list.append(i)
    return n_list
