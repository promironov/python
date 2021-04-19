time = int(input('Введите время в секундах'))
hours = time // 3600
mins_secs = time % 3600
mins = mins_secs // 60
secs = mins_secs % 60
print(f"Время составляет {hours:02}:{mins:02}:{secs:02}")