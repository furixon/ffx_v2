# Generated by Django 3.1.2 on 2020-10-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemUploadInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_no', models.CharField(max_length=128, verbose_name='상품관리번호')),
                ('directory', models.CharField(max_length=128, verbose_name='디렉토리')),
                ('brand_en', models.CharField(max_length=256, verbose_name='브랜드(EN)')),
                ('brand_jp', models.CharField(max_length=256, verbose_name='브랜드(JP)')),
                ('name_en', models.CharField(max_length=512, verbose_name='상품명(JP')),
                ('name_jp', models.CharField(max_length=512, verbose_name='상품명(EN)')),
                ('qty', models.CharField(max_length=256, verbose_name='중량 및 수량')),
                ('keyword', models.CharField(max_length=512, verbose_name='키워드')),
                ('feature_pc', models.CharField(max_length=512, verbose_name='특징(PC)')),
                ('feature_sp', models.CharField(max_length=512, verbose_name='특징(SP)')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='상품설명')),
                ('footer', models.CharField(max_length=256, verbose_name='Footer')),
                ('price', models.IntegerField(default=0, verbose_name='판매가격')),
                ('delivery_free', models.CharField(max_length=32, verbose_name='송료무료여부')),
                ('max_buy_qty', models.IntegerField(default=0, verbose_name='최대구입수량')),
                ('category_1', models.CharField(max_length=128, verbose_name='카테1')),
                ('category_2', models.CharField(blank=True, max_length=128, null=True, verbose_name='카테2')),
                ('category_3', models.CharField(blank=True, max_length=128, null=True, verbose_name='카테3')),
                ('category_4', models.CharField(blank=True, max_length=128, null=True, verbose_name='카테4')),
                ('options', models.CharField(max_length=128, verbose_name='옵션')),
                ('visible_yn', models.CharField(max_length=32, verbose_name='노출(Y/N)')),
            ],
            options={
                'verbose_name': '상품정보',
                'verbose_name_plural': '상품정보',
            },
        ),
        migrations.CreateModel(
            name='RakutenApiItemInsert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemUrl', models.CharField(max_length=255, verbose_name='관리번호')),
                ('itemNumber', models.CharField(max_length=32, verbose_name='상품번호')),
                ('itemName', models.CharField(max_length=255, verbose_name='상품명')),
                ('itemPrice', models.IntegerField(default=0, verbose_name='판매가격')),
                ('genreId', models.IntegerField(default=0, verbose_name='디렉토리')),
                ('catalogId', models.CharField(max_length=30, verbose_name='카탈로그ID')),
                ('catalogIdExemptionReason', models.IntegerField(default=0, verbose_name='사유')),
                ('whiteBgImageUrl', models.CharField(max_length=255, verbose_name='이미지URL')),
                ('images', models.TextField(blank=True, null=True, verbose_name='상세이미지')),
                ('imageAlt', models.CharField(max_length=255, verbose_name='이미지이름')),
                ('descriptionForPC', models.TextField(blank=True, null=True, verbose_name='상품설명(PC)')),
                ('descriptionForMobile', models.TextField(blank=True, null=True, verbose_name='상품설명(Mo)')),
                ('descriptionForSmartPhone', models.TextField(blank=True, null=True, verbose_name='상품설명(SP)')),
                ('movieUrl', models.CharField(max_length=1024, verbose_name='영상URL')),
                ('options', models.TextField(blank=True, null=True, verbose_name='옵션')),
                ('tagIds', models.CharField(blank=True, max_length=200, null=True, verbose_name='태그ID')),
                ('catchCopyForPC', models.CharField(blank=True, max_length=174, null=True, verbose_name='태그ID')),
                ('catchCopyForMobile', models.CharField(blank=True, max_length=60, null=True, verbose_name='태그ID')),
                ('descriptionBySalesMethod', models.TextField(blank=True, null=True, verbose_name='판매설명(PC)')),
                ('isSaleButton', models.BooleanField(default=True, verbose_name='주문버튼')),
                ('isDocumentButton', models.BooleanField(default=True, verbose_name='정보신청버튼')),
                ('isInquiryButton', models.BooleanField(default=True, verbose_name='제품문의버튼')),
                ('isStockNoticeButton', models.BooleanField(default=False, verbose_name='재입고알림버튼')),
                ('displayMakerContents', models.BooleanField(default=False, verbose_name='제조사표시')),
                ('itemLayout', models.IntegerField(default=4, verbose_name='레이아웃')),
                ('isIncludedTax', models.BooleanField(default=True, verbose_name='소비세')),
                ('isIncludedPostage', models.BooleanField(default=False, verbose_name='송료')),
                ('isIncludedCashOnDeliveryPostage', models.BooleanField(default=False, verbose_name='반품수수료')),
                ('displayPrice', models.IntegerField(default=0, verbose_name='표시가격')),
                ('orderLimit', models.IntegerField(default=-1, verbose_name='주문접수수')),
                ('postage', models.IntegerField(default=0, verbose_name='개별배송비')),
                ('postageSegment1', models.IntegerField(default=0, verbose_name='배송구분1')),
                ('postageSegment2', models.IntegerField(default=0, verbose_name='배송구분2')),
                ('isNoshiEnable', models.BooleanField(default=False, verbose_name='작동대응')),
                ('isTimeSale', models.BooleanField(default=False, verbose_name='세일')),
                ('timeSaleStartDateTime', models.DateTimeField(verbose_name='시작일시')),
                ('timeSaleEndDateTime', models.DateTimeField(verbose_name='종료일시')),
                ('isUnavailableForSearch', models.BooleanField(default=False, verbose_name='검색숨기기')),
                ('limitedPasswd', models.CharField(blank=True, max_length=60, null=True, verbose_name='제한비번')),
                ('isAvailableForMobile', models.BooleanField(default=True, verbose_name='모바일표시')),
                ('isDepot', models.BooleanField(default=False, verbose_name='창고지정')),
                ('detailSellType', models.IntegerField(default=0, verbose_name='')),
                ('releaseDate', models.DateField(verbose_name='예약출시일')),
                ('pointRate', models.IntegerField(default=0, verbose_name='포인트배율')),
                ('pointRateStart', models.DateTimeField(verbose_name='포인트시작일시')),
                ('pointRateEnd', models.DateTimeField(verbose_name='포인트종료일시')),
                ('inventoryType', models.IntegerField(default=1, verbose_name='재고유형')),
                ('inventories', models.TextField(blank=True, null=True, verbose_name='재고정보')),
                ('asurakuDeliveryId', models.CharField(blank=True, max_length=10, null=True, verbose_name='배송관리번호')),
                ('overseasDeliveryId', models.IntegerField(verbose_name='해외배송관리번호')),
                ('deliverySetId', models.IntegerField(verbose_name='배송방법세트관리번호')),
                ('sizeChartLinkCode', models.CharField(blank=True, max_length=10, null=True, verbose_name='사이즈차트관리번호')),
                ('reviewDisp', models.IntegerField(default=2, verbose_name='리뷰보기')),
                ('medicine', models.TextField(verbose_name='의약품정보')),
                ('displayPriceId', models.IntegerField(default=0, verbose_name='이중가격표시')),
                ('categoryInfo', models.TextField(blank=True, null=True, verbose_name='카테고리정보')),
                ('itemWeight', models.IntegerField(default=999999999, verbose_name='우선순위')),
                ('layoutCommonId', models.IntegerField(default=0, verbose_name='왼쪽내비')),
                ('layoutMapId', models.IntegerField(default=0, verbose_name='표시항목순서')),
                ('textSmallId', models.IntegerField(default=0, verbose_name='공통설명(소)템플릿')),
                ('lossLeaderId', models.IntegerField(default=0, verbose_name='인기상품템플릿')),
                ('textLargeId', models.IntegerField(default=0, verbose_name='공통설명(대)템플릿')),
                ('shopAreaSoryoPatternId', models.IntegerField(default=0, verbose_name='공통설명(소)템플릿')),
                ('taxRate', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='소비세율')),
                ('isSingleItemShipping', models.BooleanField(default=False, verbose_name='단품배송설정')),
                ('singleItemShippingReason', models.IntegerField(default=0, verbose_name='설정사유')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='등록일시')),
            ],
            options={
                'verbose_name': '상품정보R',
                'verbose_name_plural': '상품정보R',
            },
        ),
    ]