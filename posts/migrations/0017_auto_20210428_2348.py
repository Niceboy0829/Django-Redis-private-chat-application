# Generated by Django 3.1.7 on 2021-04-28 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0016_auto_20210428_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sharedpost',
            options={'ordering': ['-date_shared']},
        ),
        migrations.AlterField(
            model_name='sharedpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shares', to='posts.post'),
        ),
        migrations.CreateModel(
            name='UserPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.BooleanField(default=True)),
                ('date_shared', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
