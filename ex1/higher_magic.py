from typing import Callable

def fireball(target: str) -> str:
    return f"Fireball hits {target}"

def heal(target: str) -> str:
    return f"Heals {target}"

def spell_combiner(spell1: Callable[..., str],
                   spell2: Callable[..., str]
                   )-> Callable[..., tuple[str, str]]:
    def combination(*args: str) -> tuple[str, str]:
        try:
            res1: str = spell1(*args)
            res2: str = spell2(*args)
            return (res1, res2)
        except Exception as e:
            return (f"Error: {e}", f"Error: {e}")
    return combination

def power_amplifier(base_spell: Callable[..., int],
                    multiplier: int
                    ) -> Callable[..., int]:
    return lambda *args: base_spell(*args) * multiplier

def base_spell() -> int:
    return 4

if __name__ == "__main__":
    print("=============Testing spell combiner=============")
    combined: Callable[..., tuple[str, str]] = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon')}\n")

    print("=============Power amplifier=============")
    power_multiplier = power_amplifier(base_spell, 5)
    print(power_multiplier())