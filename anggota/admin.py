# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.core.validators import EMPTY_VALUES
# from django.utils.translation import gettext_lazy as _
# from unfold.admin import ModelAdmin
# from unfold.contrib.filters.admin import TextFilter, FieldTextFilter
# from .models import anggotaPosyandu

# class CustomTextFilter(TextFilter):
#     title = _("Custom filter")
#     parameter_name = "query_param_in_uri"

#     def queryset(self, request, queryset):
#         if self.value() not in EMPTY_VALUES:
#             # Here write custom query
#             return queryset.filter(your_field=self.value())

#         return queryset



# class MyAdmin(ModelAdmin):
#     list_display = ["NamaAnggota"]
#     list_filter_submit = True  # Submit button at the bottom of the filter
#     list_filter = [
#         ("model_charfield", FieldTextFilter),
#         CustomTextFilter
#     ]