from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

class UserProfile(models.Model):

    LOW_RANK = 'LR'
    HIGH_RANK = 'HR'
    G_RANK = 'GR'
    G_RANK_PLUS = 'GRP'
    GUILD_MASTER = 'GM'

    ranks = (
            (LOW_RANK, 'Low Rank'),
            (HIGH_RANK, 'High Rank'),
            (G_RANK, 'G-Rank'),
            (G_RANK_PLUS, 'G-Rank 100-998'),
            (GUILD_MASTER, 'G-Rank 999'),
    )

    GREATSWORD = 'GS'
    LONGSWORD = 'LS'
    SWORD_N_SHIELD = 'SNS'
    DUAL_BLADES = 'DB'
    HAMMER = 'HAM'
    HUNTING_HORN = 'HH'
    LANCE = 'LAN'
    GUNLANCE = 'GL'
    SWITCHAXE = 'SA'
    CHARGE_AXE = 'CA'
    INSECT_GLAIVE = 'IG'
    TONFA = 'TON'
    BOW = 'BOW'
    HEAVY_BOWGUN = 'HBG'
    LIGHT_BOWGUN = 'LBG'

    weapons = (
            (GREATSWORD, 'Greatsword'),
            (LONGSWORD, 'Longsword'),
            (SWORD_N_SHIELD, 'Sword & Shield'),
            (DUAL_BLADES, 'Dual Blades'),
            (HAMMER, 'Hammer'),
            (HUNTING_HORN, 'Hunting Horn'),
            (LANCE, 'Lance'),
            (GUNLANCE, 'Gunlance'),
            (SWITCHAXE, 'Switch Axe'),
            (CHARGE_AXE, 'Charge Axe'),
            (INSECT_GLAIVE, 'Insect Glaive'),
            (TONFA, 'Tonfa'),
            (BOW, 'Bow'),
            (HEAVY_BOWGUN, 'Heavy Bowgun'),
            (LIGHT_BOWGUN, 'Light Bowgun'),
    )


    user = models.OneToOneField(User)
    description = models.TextField(max_length=200, null=True, blank=True)
    hunter_name = models.CharField(max_length=30, blank=True, default='')
    nintendo_name = models.CharField(max_length=30, blank=True, default='')
    skype_name = models.CharField(max_length=30, blank=True, default='')
    teamspeak_name = models.CharField(max_length=30, blank=True, default='')
    friend_code = models.CharField(
            max_length=14,
            help_text="Please use the following format: <em>####-####-####</em>.",
            blank=True, default=''
    )
    rank = models.CharField(
            max_length=3,
            choices=ranks,
            default=LOW_RANK,
    )
    weapon = models.CharField(
            max_length=3,
            choices=weapons,
            blank=True,
            null=True,
            default=None,
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)
