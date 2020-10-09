from django.contrib import admin
from .models import RakutenApiItemInsert

# Register your models here.

# 사이트 타이틀
admin.site.site_header = "FFX ADMIN v2"
admin.site.site_title = "FFX ADMIN v2"
admin.site.index_title = "FFX ADMIN v2"
admin.empty_value_display = '데이터가 없습니다! ^^;'


@admin.register(RakutenApiItemInsert)
class RakutenApiItemInsertAdmin(admin.ModelAdmin):
    list_display = ['itemUrl', 'itemNumber', 'itemName', 'itemPrice', 'genreId', 'catalogId', 'catalogIdExemptionReason']
    list_display_links = ['itemUrl', 'itemNumber', 'itemName', 'itemPrice', 'genreId', 'catalogId', 'catalogIdExemptionReason']
    list_filter = ['itemNumber', 'itemName']
    search_fields = ['itemNumber', 'itemName']

    class Meta:
        model = RakutenApiItemInsert
