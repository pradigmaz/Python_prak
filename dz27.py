# 1 скриншот

class Counter:
    def __init__(self, value=0):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

c1 = Counter(1)
c3 = Counter(3)

print(f"c3 > c1 {c3 > c1}")    # True
print(f"c3 >= c1 {c3 >= c1}")  # True
print(f"c3 < c1 {c3 < c1}")    # False
print(f"c3 <= c1 {c3 <= c1}")  # False

# 2 скриншот

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # конвертация в секунды для простоты расчётов
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def _from_seconds(self, sec):
        # создание нового объекта из секунд
        c = Clock()
        c.total_seconds = int(sec)
        return c

    def __str__(self):
        # форматирование в HH:MM:SS
        h = self.total_seconds // 3600
        m = (self.total_seconds % 3600) // 60
        s = self.total_seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def __sub__(self, other):
        return self._from_seconds(self.total_seconds - other.total_seconds)

    def __mul__(self, other):
        # умножение на число (другой объект Clock интерпретируется как множитель секунд)
        if isinstance(other, Clock):
            return self._from_seconds(self.total_seconds * other.total_seconds)
        return self._from_seconds(self.total_seconds * other)

    def __floordiv__(self, other):
        if isinstance(other, Clock):
            return self._from_seconds(self.total_seconds // other.total_seconds)
        return self._from_seconds(self.total_seconds // other)

    def __mod__(self, other):
        if isinstance(other, Clock):
            return self._from_seconds(self.total_seconds % other.total_seconds)
        return self._from_seconds(self.total_seconds % other)

    def __isub__(self, other):
        self.total_seconds -= other.total_seconds
        return self

    def __imul__(self, other):
        if isinstance(other, Clock):
            self.total_seconds *= other.total_seconds
        else:
            self.total_seconds *= other
        return self

    def __ifloordiv__(self, other):
        if isinstance(other, Clock):
            self.total_seconds //= other.total_seconds
        else:
            self.total_seconds //= other
        return self

    def __imod__(self, other):
        if isinstance(other, Clock):
            self.total_seconds %= other.total_seconds
        else:
            self.total_seconds %= other
        return self

c1 = Clock(0, 10, 0)   # 00:10:00
c2 = Clock(0, 3, 20)   # 00:03:20

print(f"c1: {c1}")
print(f"c1 - c2: {c1 - c2}")
print(f"c1 * c2: {c1 * c2}")
print(f"c1 // c2: {c1 // c2}")
print(f"c1 % c2: {c1 % c2}")

c1 -= c2
print(f"c1 -= c2: {c1}")

c1 = Clock(0, 10, 0)
c1 *= c2
print(f"c1 *= c2: {c1}")

c1 = Clock(0, 10, 0)
c1 //= c2
print(f"c1 //= c2: {c1}")

c1 = Clock(0, 10, 0)
c1 %= c2
print(f"c1 % c2: {c1}")
