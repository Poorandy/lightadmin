import uuid
import json

from django.db import models
from django.contrib.auth.models import User
from django.db.models import base
from django.utils import timezone
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# Create your models here.


class Monster(models.Model):
    id = models.UUIDField(
        verbose_name='ID', default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name="单位名", max_length=50)
    summary = models.TextField(verbose_name="单位描述")
    health = models.IntegerField(verbose_name="血量")
    sync = models.IntegerField(verbose_name="体力")
    attack = models.IntegerField(verbose_name="攻击力")
    defend = models.IntegerField(verbose_name="防御力")
    img = models.ImageField(
        verbose_name='封面', upload_to='img/monster/%Y/%m/%d/', null=True, blank=True)
    # "@absDamage(5)|@consDamage(2,4)|absHeal(5)"
    behavior = models.TextField(verbose_name="单位行为")
    behavior_script = models.TextField(
        verbose_name="单位行为代码", null=True, blank=True)
    unit_flag = models.IntegerField(verbose_name="单位标记", default=0)
    editor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="编辑人", null=True, blank=True, default=None)
    update_time = models.DateTimeField(
        verbose_name="更新时间", auto_now=True)
    create_time = models.DateTimeField(
        verbose_name="创建时间", default=timezone.now)
    delete_flag = models.SmallIntegerField(verbose_name="删除标记", default=0)

    class Meta:
        verbose_name = "怪物单位"

    def __str__(self):
        return json.dumps({'id': str(self.id), 'name': self.name}, ensure_ascii=False)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.event_year = int(str(self.event_date).split('-')[0])
    #     super(Monster, self).save()


class BattleField(models.Model):
    name = models.CharField(
        verbose_name="战斗名", max_length=255, primary_key=True)
    summary = models.TextField(verbose_name="战斗描述", blank=True)
    editor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="编辑人", null=True, blank=True, default=None)
    combat_log = models.TextField(verbose_name="战斗日志", blank=True)
    monster = models.TextField(verbose_name="怪物列表", blank=True)
    character = models.TextField(verbose_name="角色", blank=True)
    card = models.TextField(verbose_name="卡牌列表", blank=True)
    loop = models.TextField(verbose_name="模拟次数", blank=True)
    update_time = models.DateTimeField(
        verbose_name="更新时间", auto_now=True)
    create_time = models.DateTimeField(
        verbose_name="创建时间", default=timezone.now)
    delete_flag = models.SmallIntegerField(verbose_name="删除标记", default=0)

    class Meta:
        verbose_name = "战斗"


class Card(models.Model):
    id = models.UUIDField(
        verbose_name='ID', default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name="卡牌名", max_length=30)
    summary = models.TextField(verbose_name="卡牌描述")
    card_choice = (("Spells", "法术牌"), ("Unit", "单位牌"))
    type = models.CharField(
        choices=card_choice, verbose_name="卡牌类型", default="法术牌", max_length=16)
    power = models.IntegerField(verbose_name="费用", default=1)
    material = models.CharField(
        verbose_name="施法材料", default='undefined', max_length=25)
    waiver = models.TextField(
        verbose_name="豁免判定", default='undefined')
    img = models.ImageField(
        verbose_name='封面', upload_to='img/card/%Y/%m/%d/', null=True, blank=True)
    behavior = models.TextField(verbose_name="单位行为")
    behavior_script = models.TextField(
        verbose_name="单位行为代码", null=True, blank=True)
    editor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="编辑人", null=True, blank=True, default=None)
    update_time = models.DateTimeField(
        verbose_name="更新时间", auto_now=True)
    create_time = models.DateTimeField(
        verbose_name="创建时间", default=timezone.now)
    delete_flag = models.SmallIntegerField(verbose_name="删除标记", default=0)

    class Meta:
        verbose_name = "卡牌"


class Character(models.Model):
    id = models.UUIDField(
        verbose_name='ID', default=uuid.uuid4, primary_key=True)

    name = models.CharField(verbose_name="角色名", max_length=30)
    summary = models.TextField(verbose_name="角色描述")
    health = models.IntegerField(verbose_name="血量")
    sync = models.IntegerField(verbose_name="体力")
    attack = models.IntegerField(verbose_name="攻击力")
    defend = models.IntegerField(verbose_name="防御力")
    img = models.ImageField(
        verbose_name='封面', upload_to='img/character/%Y/%m/%d/', null=True, blank=True)
    # "@absDamage(5)|@consDamage(2,4)|absHeal(5)"
    behavior = models.TextField(verbose_name="单位行为")
    behavior_script = models.TextField(
        verbose_name="单位行为代码", null=True, blank=True)
    editor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="编辑人", null=True, blank=True, default=None)
    update_time = models.DateTimeField(
        verbose_name="更新时间", auto_now=True)
    create_time = models.DateTimeField(
        verbose_name="创建时间", default=timezone.now)
    delete_flag = models.SmallIntegerField(verbose_name="删除标记", default=0)

    class Meta:
        verbose_name = "角色"


class Aura(models.Model):
    id = models.UUIDField(
        verbose_name='ID', default=uuid.uuid4, primary_key=True)

    name = models.CharField(verbose_name="BUFF名称", max_length=30)
    summary = models.TextField(verbose_name="BUFF描述")
    img = models.ImageField(
        verbose_name='封面', upload_to='img/buffs/%Y/%m/%d/', null=True, blank=True)
    # "@absDamage(5)|@consDamage(2,4)|absHeal(5)"
    behavior = models.TextField(verbose_name="单位行为")
    behavior_script = models.TextField(
        verbose_name="单位行为代码", null=True, blank=True)
    editor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="编辑人", null=True, blank=True, default=None)
    update_time = models.DateTimeField(
        verbose_name="更新时间", auto_now=True)
    create_time = models.DateTimeField(
        verbose_name="创建时间", default=timezone.now)
    delete_flag = models.SmallIntegerField(verbose_name="删除标记", default=0)

    class Meta:
        verbose_name = "光环"


class ArmorArms(models.Model):
    id = models.UUIDField(
        verbose_name='ID', default=uuid.uuid4, primary_key=True)

    name = models.CharField(verbose_name="装备名称", max_length=30)
    summary = models.TextField(verbose_name="装备描述")
    img = models.ImageField(
        verbose_name='封面', upload_to='img/armor/%Y/%m/%d/', null=True, blank=True)
    # "@absDamage(5)|@consDamage(2,4)|absHeal(5)"
    slot = models.IntegerField(verbose_name="装备槽位")
    behavior = models.TextField(verbose_name="单位行为")
    behavior_script = models.TextField(
        verbose_name="单位行为代码", null=True, blank=True)
    editor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="编辑人", null=True, blank=True, default=None)
    update_time = models.DateTimeField(
        verbose_name="更新时间", auto_now=True)
    create_time = models.DateTimeField(
        verbose_name="创建时间", default=timezone.now)
    delete_flag = models.SmallIntegerField(verbose_name="删除标记", default=0)

    class Meta:
        verbose_name = "装备"
