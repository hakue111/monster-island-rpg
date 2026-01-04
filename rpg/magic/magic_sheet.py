from rpg.magic.magic import Magic, BlackMagic, WhiteMagic, EvilMagic

### ice magic ###
blizzard = BlackMagic(
    name="Blizzard",
    elemental="ice",
    mp_cost=10,
    dmg=10,
    tier=1
            )
blizzara = BlackMagic(
    name="Blizzara",
    elemental="ice",
    mp_cost=20,
    dmg=20,
    tier=2
            )
blizzaga = BlackMagic(
    name="Blizzaga",
    elemental="ice",
    mp_cost=40,
    dmg=40,
    tier=3
            )

### fire magic ###
fire = BlackMagic(
    name="Fire",
    elemental="fire",
    mp_cost=10,
    dmg=10,
    tier=1
            )
fira = BlackMagic(
    name="Fira",
    elemental="fire",
    mp_cost=20,
    dmg=20,
    tier=2
            )
firaga = BlackMagic(
    name="Firaga",
    elemental="fire",
    mp_cost=40,
    dmg=40,
    tier=3
            )

### lightning magic ###
thunder = BlackMagic(
    name="Thunder",
    elemental="lightning",
    mp_cost=10,
    dmg=10,
    tier=1
            )
thundara = BlackMagic(
    name="Thundara",
    elemental="lightning",
    mp_cost=20,
    dmg=20,
    tier=2
            )
thundaga = BlackMagic(
    name="Thundaga",
    elemental="lightning",
    mp_cost=40,
    dmg=40,
    tier=3
            )

### wind magic ###
aero = BlackMagic(
    name="Aero",
    elemental="wind",
    mp_cost=10,
    dmg=10,
    tier=1
            )
aerora = BlackMagic(
    name="Aerora",
    elemental="wind",
    mp_cost=20,
    dmg=20,
    tier=2
            )
aeroga = BlackMagic(
    name="Aeroga",
    elemental="wind",
    mp_cost=40,
    dmg=40,
    tier=3
            )

### water magic ###
water = BlackMagic(
    name="Water",
    elemental="water",
    mp_cost=10,
    dmg=10,
    tier=1
            )
watera = BlackMagic(
    name="Watera",
    elemental="water",
    mp_cost=20,
    dmg=20,
    tier=2
            )
waterga = BlackMagic(
    name="Waterga",
    elemental="water",
    mp_cost=40,
    dmg=40,
    tier=3
            )

dark = EvilMagic(
    name="Dark",
    elemental="darkness",
    mp_cost=30,
    dmg=30,
    tier=1
)

darkra = BlackMagic(
    name="Darkra",
    elemental="darkness",
    mp_cost=60,
    dmg=60,
    tier=2
)

darkga = BlackMagic(
    name="Darkga",
    elemental="darkness",
    mp_cost=90,
    dmg=90,
    tier=3
)


### neutral black magic ###
flare = BlackMagic(
    name="Flare",
    elemental = "neutral",
    mp_cost=50,
    dmg=50,
    tier=3
            )

### white magic ###
cure = WhiteMagic(
    name="Cure",
    elemental = "neutral",
    mp_cost=40,
    heal=40,
    tier=1
            )
cura = WhiteMagic(
    name="Cura",
    elemental = "neutral",
    mp_cost=60,
    heal=60,
    tier=2
            )
curaga = WhiteMagic(
    name="Curaga",
    elemental = "neutral",
    mp_cost=100,
    heal=100,
    tier=3
            )


