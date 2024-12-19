# Try to look for packages data.time
# vacation calendar
from datetime import datetime

date = datetime(2024, 12, 18)
print(date)
# date_str = "2024-12-18"
# date = datetime.datetime(2024,12,18)
# date.time.strptime(date_str,"%y-%m-%d")
x = datetime.date()
datetime.strptime
# ferien_winter_start = datetime.date(2024, 12, 24)
# Wichtigste Funktionen und Klassen von datetime:
# datetime.date: Diese Klasse repräsentiert ein Datum (Jahr, Monat, Tag).
# datetime.time: Diese Klasse repräsentiert eine Uhrzeit (Stunden, Minuten, Sekunden).
# datetime.datetime: Diese Klasse kombiniert Datum und Uhrzeit.
# datetime.timedelta: Diese Klasse stellt die Differenz zwischen zwei datetime-Objekten dar.
# datetime.now(): Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.
# datetime.strptime(): Wandelt ein Datum in ein datetime-Objekt um, bas

d = input("enter day of the year")

if d >= "2024.12.24" and d <= "2025.01.02":
    print(f"This day belongs to Christmas vacation '25 : {d:}")
    exit()

if d >= "2025.04.18" and d <= "2025.04.21":

    exit()
if d > "2025.08.08" and d <= "2025.08.19":
    print(f"This day belongs to summer vacation : {d}")
    exit()
if d >= "2025.12.24" and d <= "2026.01.02":
    print(f"This day belongs to Christmas vacation '26 : {d}")
    exit()
print("It is a working day :-( ")
