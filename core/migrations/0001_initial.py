# Generated by Django 4.2.9 on 2024-10-23 07:46

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyRequire',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã yêu cầu')),
                ('desc', models.CharField(max_length=50, verbose_name='Mô tả')),
                ('created_date', models.DateField(verbose_name='Ngày yêu cầu')),
                ('expired_date', models.DateField(blank=True, null=True, verbose_name='Ngày cần')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ghi chú')),
                ('created_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='Người yêu cầu')),
                ('status', models.SmallIntegerField(choices=[(0, 'draft'), (1, 'pending'), (2, 'accepted'), (3, 'rejected')], default=0, verbose_name='Trạng thái yêu cầu')),
            ],
            options={
                'verbose_name': 'Yêu cầu mua',
                'verbose_name_plural': 'Yêu cầu mua',
                'db_table': 'buy_required',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã đơn mua')),
                ('desc', models.CharField(max_length=50, verbose_name='Diễn giải')),
                ('order_date', models.DateField(verbose_name='Ngày hóa đơn')),
                ('deli_date', models.DateField(null=True, verbose_name='Ngày giao hàng')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Pending'), (2, 'Accepted'), (3, 'Canceled')], default=1, verbose_name='Trạng thái đơn hàng')),
            ],
            options={
                'verbose_name': 'Đơn mua',
                'verbose_name_plural': 'Đơn mua',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã chào giá')),
                ('desc', models.CharField(max_length=255, verbose_name='Diễn giải')),
                ('price_date', models.DateField(verbose_name='Ngày chào giá')),
                ('expire', models.IntegerField(default=1, verbose_name='Thời gian hiệu lực (ngày)')),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'pending'), (2, 'accepted'), (3, 'rejected')], default=1, verbose_name='Trạng thái chào giá')),
                ('buy_require', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.buyrequire', verbose_name='Mã yêu cầu')),
            ],
            options={
                'verbose_name': 'Chào giá',
                'verbose_name_plural': 'Chào giá',
                'db_table': 'price',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã hàng hóa')),
                ('name', models.CharField(max_length=50, verbose_name='Tên hàng hóa')),
            ],
            options={
                'verbose_name': 'Hàng hóa',
                'verbose_name_plural': 'Hàng hóa',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã loại hàng')),
                ('name', models.CharField(max_length=50, verbose_name='Tên loại hàng')),
            ],
            options={
                'verbose_name': 'Loại hàng',
                'verbose_name_plural': 'Loại hàng',
                'db_table': 'product_type',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã nhà cung cấp')),
                ('name', models.CharField(max_length=50, verbose_name='Tên nhà cung cấp')),
                ('legal_repr', models.CharField(blank=True, max_length=50, null=True, verbose_name='Người đại diện')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Số điện thoại')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Địa chỉ')),
                ('acc_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Số tài khoản')),
                ('tax_code', models.CharField(blank=True, max_length=15, null=True, verbose_name='Mã số thuế')),
                ('status', models.BooleanField(default=False, verbose_name='Trạng thái hoạt động')),
            ],
            options={
                'verbose_name': 'Nhà cung cấp',
                'verbose_name_plural': 'Nhà cung cấp',
                'db_table': 'provider',
            },
        ),
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã nhận hàng')),
                ('description', models.TextField(verbose_name='Diễn giải')),
                ('receive_date', models.DateField(verbose_name='Ngày nhận')),
                ('sender', models.CharField(max_length=50, verbose_name='Người giao')),
                ('receiver', models.CharField(max_length=50, verbose_name='Người nhận')),
                ('status', models.IntegerField(default=0, verbose_name='Trạng thái thanh toán')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.order', verbose_name='Mã đơn hàng')),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.provider', verbose_name='Nhà cung cấp')),
            ],
            options={
                'verbose_name': 'Nhận hàng',
                'verbose_name_plural': 'Nhận hàng',
                'db_table': 'receive',
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã trả hàng')),
                ('reason', models.CharField(max_length=255, verbose_name='Lý do')),
                ('refund_date', models.DateField(verbose_name='Ngày trả')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ghi chú')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Waiting'), (2, 'Pending'), (3, 'Refunded')], default=0, verbose_name='Trạng thái trả hàng')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.order', verbose_name='Mã đơn hàng')),
            ],
            options={
                'verbose_name': 'Trả hàng',
                'verbose_name_plural': 'Trả hàng',
                'db_table': 'refund',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã đơn vị')),
                ('desc', models.CharField(max_length=50, verbose_name='Mô tả')),
            ],
            options={
                'verbose_name': 'Đơn vị hàng hóa',
                'verbose_name_plural': 'Đơn vị hàng hóa',
                'db_table': 'units',
            },
        ),
        migrations.CreateModel(
            name='RefundDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('quantity', models.IntegerField(default=1, verbose_name='Số lượng')),
                ('price', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Giá')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='% Chiết khấu')),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='% Thuế')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ghi chú')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product', verbose_name='Mã hàng hóa')),
                ('refund', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.refund', verbose_name='Mã trả hàng')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.unit', verbose_name='Đơn vị tính')),
            ],
            options={
                'verbose_name': 'Chi tiết trả hàng',
                'verbose_name_plural': 'Chi tiết trả hàng',
                'db_table': 'refund_detail',
            },
        ),
        migrations.CreateModel(
            name='ReceiveDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('quantity', models.IntegerField(default=1, verbose_name='Số lượng')),
                ('price', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Giá')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='% Chiết khấu')),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='% Thuế')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Phí')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product', verbose_name='Mã hàng hóa')),
                ('receive', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.receive', verbose_name='Mã nhận hàng')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.unit', verbose_name='Đơn vị tính')),
            ],
            options={
                'verbose_name': 'Chi tiết nhận hàng',
                'verbose_name_plural': 'Chi tiết nhận hàng',
                'db_table': 'receive_detail',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.producttype', verbose_name='Loại hàng hóa'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.unit', verbose_name='Đơn vị tính'),
        ),
        migrations.CreateModel(
            name='PriceDetail',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã chi tiết chào giá')),
                ('qty', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Số lượng')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Đơn giá')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Triết khấu (%)')),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Thuế (%)')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Phí')),
                ('price_code', models.ForeignKey(db_column='price_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.price', verbose_name='Mã chào giá')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product', verbose_name='Mã hàng')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.unit', verbose_name='Đơn vị tính')),
            ],
            options={
                'verbose_name': 'Chi tiết chào giá',
                'verbose_name_plural': 'Chi tiết chào giá',
                'db_table': 'price_detail',
            },
        ),
        migrations.AddField(
            model_name='price',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.provider', verbose_name='Mã nhà cung cấp'),
        ),
        migrations.CreateModel(
            name='PaymentSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('start_date', models.DateField(verbose_name='Ngày bắt đầu thanh toán')),
                ('end_date', models.DateField(verbose_name='Ngày kết thúc thanh toán')),
                ('times', models.IntegerField(default=1, unique=True, verbose_name='Số lần thanh toán')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Số tiền')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.order', verbose_name='Mã đơn mua')),
            ],
            options={
                'verbose_name': 'Lịch thanh toán',
                'verbose_name_plural': 'Lịch thanh toán',
                'db_table': 'payment_schedule',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã thanh toán')),
                ('payment_date', models.DateField(verbose_name='Ngày thanh toán')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mô tả')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Số tiền')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Waiting'), (2, 'Pending'), (3, 'Done')], default=0, verbose_name='Trạng thái thanh toán')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.order', verbose_name='Mã đơn hàng')),
                ('times', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.paymentschedule', to_field='times', verbose_name='Số lần thanh toán')),
            ],
            options={
                'verbose_name': 'Thanh toán',
                'verbose_name_plural': 'Thanh toán',
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Mã chi tiết đơn mua')),
                ('qty', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Số lượng')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Đơn giá')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Chiết khấu (%)')),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Thuế (%)')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Phí')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.order', verbose_name='Mã đơn mua')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product', verbose_name='Mã hàng')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.unit', verbose_name='Đơn vị tính')),
            ],
            options={
                'verbose_name': 'Chi tiết đơn mua',
                'verbose_name_plural': 'Chi tiết đơn mua',
                'db_table': 'order_detail',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.price', verbose_name='Mã chào giá'),
        ),
        migrations.AddField(
            model_name='order',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.provider', verbose_name='Nhà cung cấp'),
        ),
        migrations.CreateModel(
            name='BuyRequireDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Thời điểm tạo')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Số lượng')),
                ('buy_require', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.buyrequire', verbose_name='Mã yêu cầu mua')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product', verbose_name='Mã hàng')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.unit', verbose_name='Đơn vị tính')),
            ],
            options={
                'verbose_name': 'Chi tiết yêu cầu mua',
                'verbose_name_plural': 'Chi tiết yêu cầu mua',
                'db_table': 'buy_require_detail',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='user', max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
