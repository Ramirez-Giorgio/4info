from datetime import date,time,datetime #dalla libreria datetime posso scegliere cosa importare al posto della libreria intera

oggi = date.today()
print(f"oggi è {oggi}")
d1 = date(2025, 10, 9)
print(d1) 
print(d1.year) 
print(d1.month) 
print(d1.day)
t = time(14, 30, 15)
print(t)
print(t.hour) 
print(t.minute)
dt = datetime(2025, 10, 9, 14, 30, 0)
print(dt) # 2025-10-09 14:30:00
print(dt.date()) # 2025-10-09 (solo data)
print(dt.time()) # 14:30:00 (solo ora)
adesso = datetime.now()
print("Adesso:", adesso)