# Cached property

# the model
#from django.utils.functional import cached_property
#
#
#class Person(models.Model):
#
#    @cached_property
#    def friends(self):
#        # expensive computation
#        ...
#        return friends

# in the view:
#if person.friends():
#    ...
#
#{% for friend in friends %}
#    do something
#{% endfor %}


##
# persons.count()
# len(persons)
##



# >>> entry = Entry.objects.get(id=1)
# >>> entry.blog   # Blog object is retrieved at this point
# >>> entry.blog   # cached version, no DB access
#
#
# >>> entry = Entry.objects.get(id=1)
# >>> entry.authors.all()   # query performed
# >>> entry.authors.all()   # query performed again