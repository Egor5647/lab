# Объем дискеты в мегабайтах
disk_capacity_mb = 1.44

# Параметры книги
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Рассчитываем общее количество символов в книге
total_chars = pages * lines_per_page * chars_per_line

# Рассчитываем размер книги в байтах
book_size_bytes = total_chars * bytes_per_char

# Конвертируем объем дискеты в байты (1 МБ = 1024 КБ, 1 КБ = 1024 байт)
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024

# Рассчитываем максимальное количество книг, которые поместятся на дискету
max_books = disk_capacity_bytes // book_size_bytes

#print("Количество книг, которое можно поместить на дискету:", int(max_books))
# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", int(max_books))
