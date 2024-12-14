import matplotlib.pyplot as plt

# Функція для зчитування датасету з файлу та відображення точок
def plot_points_from_dataset(file_path, output_file):
    # Зчитування датасету
    try:
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                x, y = map(int, line.split())
                data.append((x, y))
        x_coords, y_coords = zip(*data)
    except Exception as e:
        print(f"Error reading dataset: {e}")
        return

    # Встановлення розмірів полотна (960x540 пікселів)
    plt.figure(figsize=(960 / 100, 540 / 100), dpi=100)

    # Налаштування осей: (0, 0) у нижньому правому куті
    ax = plt.gca()
    ax.set_xlim(0, max(x_coords)+10)  # Налаштування меж по X (+10 щоб графік не доторкався да границь)
    ax.set_ylim(0, max(y_coords)+10)  # Налаштування меж по Y
    ax.invert_xaxis()  # Інвертувати вісь X для перенесення (0, 0) у нижній правий кут

    # Інвертування осі Y, щоб напрямок був знизу вверх (з нижнього правого до верхнього правого кута)
    ax.yaxis.set_ticks_position('right')
    ax.yaxis.set_label_position('right')

    # Відображення точок
    plt.scatter(x_coords, y_coords, c='blue', label='Точки')

    # Налаштування осей
    plt.xlabel('X-вісь')
    plt.ylabel('Y-вісь')
    plt.title('Графік')
    plt.legend()

    # Збереження результату у графічний формат
    try:
        plt.savefig(output_file, format='png')
        print(f"Plot saved as {output_file}")
    except Exception as e:
        print(f"Error saving plot: {e}")

#Назва вихідного зображення
output_file = 'result_plot.png'

# Виклик функції
plot_points_from_dataset("DS8.txt", output_file)