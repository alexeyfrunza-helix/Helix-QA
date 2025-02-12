import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import os

# Функция для сборки версии
def get_version(v1, v2, v3, v4):
    return f"{v1.get()}.{v2.get()}.{v3.get()}.{v4.get()}"

# Функция для проверки, что все поля содержат только цифры
def is_valid_version(*entries):
    return all(entry.get().isdigit() for entry in entries)

# Функция для обработки данных и запуска скрипта
def submit():
    # Проверка заполненности всех полей
    if not all([oldversion_1_1.get(), oldversion_1_2.get(), oldversion_1_3.get(), oldversion_1_4.get(),
                newversion_1_1.get(), newversion_1_2.get(), newversion_1_3.get(), newversion_1_4.get(),
                platformversion_1_1.get(), platformversion_1_2.get(), platformversion_1_3.get(), platformversion_1_4.get(),
                slkversion_1_1.get(), slkversion_1_2.get(), slkversion_1_3.get(), slkversion_1_4.get()]):
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        return

    # Проверка корректности ввода версий
    if not (is_valid_version(oldversion_1_1, oldversion_1_2, oldversion_1_3, oldversion_1_4) and 
            is_valid_version(newversion_1_1, newversion_1_2, newversion_1_3, newversion_1_4) and 
            is_valid_version(platformversion_1_1, platformversion_1_2, platformversion_1_3, platformversion_1_4) and 
            is_valid_version(slkversion_1_1, slkversion_1_2, slkversion_1_3, slkversion_1_4)):
        messagebox.showerror("Ошибка", "Все версии должны содержать только числа.")
        return

    # Получение данных из полей
    product = product_var.get()
    oldversion_1 = get_version(oldversion_1_1, oldversion_1_2, oldversion_1_3, oldversion_1_4)
    newversion_1 = get_version(newversion_1_1, newversion_1_2, newversion_1_3, newversion_1_4)
    platformversion_1 = get_version(platformversion_1_1, platformversion_1_2, platformversion_1_3, platformversion_1_4)
    slkversion = get_version(slkversion_1_1, slkversion_1_2, slkversion_1_3, slkversion_1_4)

    # Определение source и target директории в зависимости от выбранного продукта
    directories = {
        "Fitness": ("C:/automation/sample/Fitness", "D:/SBORKA/Fitness"),
        "Fitness_PROF": ("C:/automation/sample/Fitness_PROF", "D:/SBORKA/Fitness_PROF"),
        "Salon": ("C:/automation/sample/Salon", "D:/SBORKA/Salon"),
        "SPA_Salon": ("C:/automation/sample/SPA_Salon", "D:/SBORKA/SPA_Salon"),
        "Stomatology": ("C:/automation/sample/Stomatology", "D:/SBORKA/Stomatology"),
    }
    sourceDirectory, target_path = directories.get(product, (None, None))

    # Проверка, что директории корректно определены
    if not sourceDirectory or not target_path:
        messagebox.showerror("Ошибка", "Не удалось определить директории для выбранного продукта.")
        return

    # Выводим собранные данные (для проверки)
    print("Product:", product)
    print("Source Directory:", sourceDirectory)
    print("Target Path:", target_path)
    print("Old Version:", oldversion_1)
    print("New Version:", newversion_1)
    print("Platform Version:", platformversion_1)
    print("SLK Version:", slkversion)

    # Определение пути к директории скрипта
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Определение путей к скриптам
    delete_folders_and_files_path = os.path.join(base_path, 'delete_folders_and_files.py')
    update_files_and_contents_path = os.path.join(base_path, 'update_files_and_contents.py')

    # Запуск внешних скриптов с обработкой ошибок
    try:
        subprocess.run(['python', delete_folders_and_files_path, target_path], check=True)
        subprocess.run(['python', update_files_and_contents_path, sourceDirectory, target_path, oldversion_1, newversion_1, platformversion_1, slkversion], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Ошибка", f"Ошибка при запуске скрипта: {e}")
        return

# Создаем основное окно приложения
root = tk.Tk()
root.title("Документация")

# Фрейм для выбора продукта
frame_product = ttk.Frame(root)
frame_product.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
ttk.Label(frame_product, text="Продукт:").grid(row=0, column=0, padx=5, pady=5)
product_var = tk.StringVar(value="Fitness")
product_menu = ttk.Combobox(frame_product, textvariable=product_var, values=["Fitness", "Fitness_PROF", "Salon", "SPA_Salon", "Stomatology"])
product_menu.grid(row=0, column=1, padx=5, pady=5)

# Функция для создания полей версий с предустановленными значениями
def create_version_fields(frame, label_text, row, default_values=None):
    ttk.Label(frame, text=label_text).grid(row=row, column=0, padx=5, pady=5)
    v1 = tk.Entry(frame, width=5)
    v2 = tk.Entry(frame, width=5)
    v3 = tk.Entry(frame, width=5)
    v4 = tk.Entry(frame, width=5)
    if default_values:
        v1.insert(0, default_values[0])
        v2.insert(0, default_values[1])
        v3.insert(0, default_values[2])
        v4.insert(0, default_values[3])
    v1.grid(row=row, column=1)
    v2.grid(row=row, column=2)
    v3.grid(row=row, column=3)
    v4.grid(row=row, column=4)
    return v1, v2, v3, v4

# Фрейм для ввода версий
frame_versions = ttk.Frame(root)
frame_versions.grid(row=1, column=0, padx=10, pady=10)

# Поля для ввода версий с предустановленными значениями для платформы и СЛК
oldversion_1_1, oldversion_1_2, oldversion_1_3, oldversion_1_4 = create_version_fields(frame_versions, "Old Version:", 1)
newversion_1_1, newversion_1_2, newversion_1_3, newversion_1_4 = create_version_fields(frame_versions, "New Version:", 2)
platformversion_1_1, platformversion_1_2, platformversion_1_3, platformversion_1_4 = create_version_fields(frame_versions, "Platform Version:", 3, default_values=('8', '3', '24', '1368'))
slkversion_1_1, slkversion_1_2, slkversion_1_3, slkversion_1_4 = create_version_fields(frame_versions, "SLK Version:", 4, default_values=('3', '0', '35', '11554'))

# Кнопка для отправки данных
submit_button = ttk.Button(root, text="Запуск", command=submit)
submit_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Запуск основного цикла приложения
root.mainloop()