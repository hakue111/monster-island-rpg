import typing

if typing.TYPE_CHECKING:
    from rpg.character.character import Character
    from rpg.item.effect import Effect


class Item:
    def __init__(self,
                 name: str,
                 description: str,
                 amount: int
                 ) -> None:
        self.name = name
        self.description = description
        self.amount = amount


class ConsumableItem(Item):
    def __init__(self,
                 name: str,
                 description: str,
                 amount: int
                 ) -> None:
        super().__init__(name, description, amount)
        self.effects = []

    def add_effect(self, effect: 'Effect') -> None:
        self.effects.append(effect)

    def consume_item(self, character: 'Character'):
        for effect in self.effects:
            effect.apply_effect(character, self)


class KeyItem(Item):
    def __init__(self,
                 name: str,
                 description: str,
                 amount: int
                 ) -> None:
        super().__init__(name, description, amount)
