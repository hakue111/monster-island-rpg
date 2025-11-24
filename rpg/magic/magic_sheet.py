from rpg.magic.magic import Magic, BlackMagic, WhiteMagic, EvilMagic

### ice magic ###
ice = BlackMagic(
    name="Ice",
    elemental="ice",
    mp_cost=10,
    dmg=10
            )
ice_2 = BlackMagic(
    name="Ice2",
    elemental="ice",
    mp_cost=20,
    dmg=20
            )
ice_3 = BlackMagic(
    name="Ice3",
    elemental="ice",
    mp_cost=40,
    dmg=40
            )

### fire magic ###
fire = BlackMagic(
    name="Fire",
    elemental="fire",
    mp_cost=10,
    dmg=10
            )
fire_2 = BlackMagic(
    name="Fire2",
    elemental="fire",
    mp_cost=20,
    dmg=20
            )
fire_3 = BlackMagic(
    name="Fire3",
    elemental="fire",
    mp_cost=40,
    dmg=40
            )

### lightning magic ###
lightning = BlackMagic(
    name="Lightning",
    elemental="lightning",
    mp_cost=10,
    dmg=10
            )
lightning_2 = BlackMagic(
    name="Lightning2",
    elemental="lightning",
    mp_cost=20,
    dmg=20
            )
lightning_3 = BlackMagic(
    name="Lightning3",
    elemental="lightning",
    mp_cost=40,
    dmg=40
            )

### wind magic ###
wind = BlackMagic(
    name="Wind",
    elemental="wind",
    mp_cost=10,
    dmg=10
            )
wind_2 = BlackMagic(
    name="Wind2",
    elemental="wind",
    mp_cost=20,
    dmg=20
            )
wind_3 = BlackMagic(
    name="Wind3",
    elemental="wind",
    mp_cost=40,
    dmg=40
            )

### water magic ###
water = BlackMagic(
    name="Water",
    elemental="water",
    mp_cost=10,
    dmg=10
            )
water_2 = BlackMagic(
    name="Water2",
    elemental="water",
    mp_cost=20,
    dmg=20
            )
water_3 = BlackMagic(
    name="Water3",
    elemental="water",
    mp_cost=40,
    dmg=40
            )

darkness = EvilMagic(
    name="Darkness",
    elemental="darkness",
    mp_cost=30,
    dmg=30
)

darkness_2 = BlackMagic(
    name="Darkness",
    elemental="darkness",
    mp_cost=60,
    dmg=60
)

darkness_3 = BlackMagic(
    name="Darkness",
    elemental="darkness",
    mp_cost=90,
    dmg=90
)


### neutral black magic ###
flare = BlackMagic(
    name="Flare",
    elemental = "neutral",
    mp_cost=50,
    dmg=50
            )

### white magic ###
cure = WhiteMagic(
    name="Cure",
    elemental = "neutral",
    mp_cost=40,
    heal=40
            )
cure_2 = WhiteMagic(
    name="Cure2",
    elemental = "neutral",
    mp_cost=60,
    heal=60
            )
cure_3 = WhiteMagic(
    name="Cure3",
    elemental = "neutral",
    mp_cost=100,
    heal=100
            )



