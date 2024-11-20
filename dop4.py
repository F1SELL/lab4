import time
import importlib
import main
import dop1
import dop2
import dop3

start_time = time.perf_counter()
for i in range(100):
    importlib.reload(main)
end_time = time.perf_counter()

print(f"Основной- {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    importlib.reload(dop1)
end_time = time.perf_counter()

print(f"Доп 1  - {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    importlib.reload(dop2)
end_time = time.perf_counter()

print(f"Доп 2  - {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    importlib.reload(dop3)
end_time = time.perf_counter()

print(f"Доп 3  - {end_time - start_time}")
