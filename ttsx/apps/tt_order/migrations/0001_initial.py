# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tt_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('update_date', models.DateField(auto_now=True, verbose_name='修改时间')),
                ('add_date', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='单价', max_digits=10)),
                ('comment', models.TextField(default='', verbose_name='评价信息')),
            ],
            options={
                'db_table': 'df_order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('update_date', models.DateField(auto_now=True, verbose_name='修改时间')),
                ('add_date', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('order_id', models.CharField(primary_key=True, max_length=64, verbose_name='订单号', serialize=False)),
                ('total_count', models.IntegerField(default=1, verbose_name='商品总数')),
                ('total_amount', models.DecimalField(decimal_places=2, verbose_name='商品总金额', max_digits=10)),
                ('trans_cost', models.DecimalField(decimal_places=2, verbose_name='运费', max_digits=10)),
                ('pay_method', models.SmallIntegerField(default=1, verbose_name='支付方式', choices=[(1, '货到付款'), (2, '支付宝')])),
                ('status', models.SmallIntegerField(default=1, verbose_name='订单状态', choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')])),
                ('trade_id', models.CharField(unique=True, max_length=100, verbose_name='支付编号', blank=True, null=True)),
                ('address', models.ForeignKey(verbose_name='收获地址', to='tt_user.Address')),
                ('user', models.ForeignKey(verbose_name='下单用户', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'df_order_info',
            },
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(verbose_name='订单', to='tt_order.OrderInfo'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='sku',
            field=models.ForeignKey(verbose_name='订单商品', to='tt_goods.GoodsSKU'),
        ),
    ]
