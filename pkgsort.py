from enum import auto, StrEnum

class Stack(StrEnum):
    STANDARD = auto(),
    SPECIAL = auto(),   # heavy or bulky
    REJECTED = auto(),  # heavy and bulky

cm, kg = float, float

BULKY_VOLUME = 1_000_000    # cm^3
BULKY_DIMENSION = 150       # cm
HEAVY = 20                  # kg

def sort(width: cm, height: cm, length: cm, mass: kg) -> str:
    assert min(width, height, length, mass) > 0

    volume = width * height * length

    is_heavy = mass >= HEAVY
    is_bulky = (
            volume >= BULKY_VOLUME or
            max(width, height, length) >= BULKY_DIMENSION)

    return (
            Stack.STANDARD if not is_heavy and not is_bulky else
            Stack.SPECIAL if is_heavy ^ is_bulky else
            Stack.REJECTED
            )._name_


cm, kg = 1, 1

assert sort(100 * cm, 100 * cm, 100 * cm, 100 * kg) == 'REJECTED'
assert sort(100 * cm, 100 * cm, 100 * cm, 20 * kg) == 'REJECTED'
assert sort(1000 * cm, 1000 * cm, 1000 * cm, 20 * kg) == 'REJECTED'
assert sort(1000 * cm, 1000 * cm, 1000 * cm, 50 * kg) == 'REJECTED'
assert sort(10 * cm, 10 * cm, 150 * cm, 20 * kg) == 'REJECTED'
assert sort(10 * cm, 10 * cm, 1500 * cm, 20 * kg) == 'REJECTED'

assert sort(100 * cm, 100 * cm, 100 * cm, 15 * kg) == 'SPECIAL'
assert sort(100 * cm, 100 * cm, 99 * cm, 20 * kg) == 'SPECIAL'
assert sort(10 * cm, 150 * cm, 10 * cm, 19 * kg) == 'SPECIAL'

assert sort(99 * cm, 99 * cm, 99 * cm, 19 * kg) == 'STANDARD'
assert sort(100 * cm, 100 * cm, 99 * cm, 19 * kg) == 'STANDARD'
assert sort(100 * cm, 149 * cm, 67 * cm, 19 * kg) == 'STANDARD'

print('All good!')
