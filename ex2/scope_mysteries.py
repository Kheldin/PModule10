from typing import Any, Callable


def mage_counter() -> Callable[..., Any]:
    count = 0

    def count_called() -> int:
        nonlocal count
        count += 1
        return count

    return count_called


def spell_accumulator(initial_power: int) -> Callable[..., Any]:
    total_power = initial_power

    def add_power(givent_amount: int) -> int:
        nonlocal total_power
        total_power += givent_amount
        return total_power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[..., Any]:
    def applied_enchantment(item_name: str) -> str:
        return enchantment_type + " " + item_name

    return applied_enchantment


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory_dict: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory_dict[key] = value

    def recall(key: str) -> Any:
        return memory_dict.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    counter_called = mage_counter()
    print("=============Testing Mage counter=============")
    print(f"Call nb {counter_called()}")
    print(f"Call nb {counter_called()}")
    print(f"Call nb {counter_called()}")

    print()
    print("=============Testing Spell Accumulator=============")
    spell_acc = spell_accumulator(5)
    print(f"current power: {spell_acc(1)}")
    print(f"current power: {spell_acc(2)}")
    print(f"current power: {spell_acc(3)}")

    print()
    print("=============Testing Enchantment factory=============")
    frozing = enchantment_factory("Frozing")
    print(frozing("Sword"))
    flaming = enchantment_factory("Flaming")
    print(flaming("Shield"))

    print()
    print("=============Testing Memory Vault=============")
    onepassword = memory_vault()
    onepassword["store"]("mypass", "qwerty")
    print(onepassword["recall"]("mypass"))
