from rpg.magic.magic import Magic, BlackMagic, WhiteMagic

ice = BlackMagic(
    name="Ice",
    elemental="ice",
    mp_cost=10,
    dmg=5
            )

fire = BlackMagic(
    name="Fire",
    elemental="fire",
    mp_cost=10,
    dmg=5
            )

lightning = BlackMagic(
    name="Lightning",
    elemental="lightning",
    mp_cost=20,
    dmg=10
            )

wind = BlackMagic(
    name="Wind",
    elemental="wind",
    mp_cost=20,
    dmg=10
            )

water = BlackMagic(
    name="Water",
    elemental="water",
    mp_cost=10,
    dmg=10
            )


flare = BlackMagic(
    name="Flare",
    elemental = "neutral",
    mp_cost=50,
    dmg=25
            )


cure = WhiteMagic(
    name="Cure",
    elemental = "neutral",
    mp_cost=20,
    heal=30
            )



