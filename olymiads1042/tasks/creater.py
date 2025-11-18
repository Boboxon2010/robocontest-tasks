import string
import os

def generate_excel_like_column_names(start_name='A', end_name='AD'):
    """
    Excel ustun nomlari (A, B, ..., Z, AA, AB, ...) kabi fayl nomlarini 
    boshlang'ich ('A') va tugatish ('AD') nomlari orasida generatsiya qiladi.
    
    Args:
        start_name (str): Boshlang'ich fayl nomi.
        end_name (str): Tugatish fayl nomi.
        
    Returns:
        list: Fayl nomlari ro'yxati (masalan, ['A', 'B', ..., 'AD']).
    """
    
    def name_to_number(name):
        """Excel nomini 1 asosli raqamga o'tkazadi (A=1, B=2, AA=27)."""
        number = 0
        for char in name:
            number = number * 26 + (string.ascii_uppercase.index(char) + 1)
        return number

    def number_to_name(number):
        """1 asosli raqamni Excel nomiga o'tkazadi."""
        name = ''
        while number > 0:
            # 0 asosli indeksni topish
            number, remainder = divmod(number - 1, 26)
            name = string.ascii_uppercase[remainder] + name
        return name

    start_num = name_to_number(start_name.upper())
    end_num = name_to_number(end_name.upper())
    
    if start_num > end_num:
        return []

    names = []
    for i in range(start_num, end_num + 1):
        names.append(number_to_name(i))
        
    return names

def create_python_files(start_name='A', end_name='AD', file_extension='.py'):
    """
    Belgilangan diapazondagi nomlar bilan Python fayllarini yaratadi.
    """
    file_names = generate_excel_like_column_names(start_name, end_name)
    
    print(f"Boshlanmoqda: {len(file_names)} ta fayl yaratiladi.")
    print("--------------------------------------------------")
    
    # Har bir faylga yoziladigan standart kontent
    default_content = """# Bu fayl avtomatik tarzda yaratildi.
# Fayl nomi: {file_name}

def main():
    print(f"Salom, men {file_name} fayliman.")
    # Faylga xos mantig'ingizni shu yerga qo'shing.

if __name__ == "__main__":
    main()
"""
    
    created_count = 0
    
    for name in file_names:
        full_file_name = f"{name}{file_extension}"
        
        # Fayl kontentini yaratish
        content = default_content.format(file_name=full_file_name)
        
        try:
            with open(full_file_name, 'w') as f:
                f.write(content)
            print(f"✅ Yaratildi: {full_file_name}")
            created_count += 1
        except IOError as e:
            print(f"❌ Xatolik yuz berdi: {full_file_name} faylini yaratib bo'lmadi. {e}")
            
    print("--------------------------------------------------")
    print(f"Bajarildi! {created_count} ta fayl muvaffaqiyatli yaratildi.")


# --- Kodni ishga tushirish ---
if __name__ == "__main__":
    # Siz xohlagan diapazonni shu yerda o'zgartirishingiz mumkin.
    create_python_files(start_name='A', end_name='AD')