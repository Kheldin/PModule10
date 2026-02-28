from typing import Any, Callable

def spell1() -> None:
    return "Fireball hits dragon"

def spell2() -> None:
    return "Heals dragon"

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return (spell1(), spell2())


if __name__ == "__main__":
    print("=============Testing spell combiner=============")
    combined = spell_combiner(spell1, spell2)
    print(f"Combined spell result: {combined}")