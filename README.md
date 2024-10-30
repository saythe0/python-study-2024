# LaboratoryApp

## Описание

**LaboratoryApp** - это учебное приложение, состоящее из восьми лабораторных работ, реализованных с использованием языка программирования Python и библиотеки Tkinter для создания графического интерфейса.

## Функциональность

Программа предоставляет следующие функции:

1. **Математические функции**:
   - Сумма, разность, произведение двух чисел
   - Среднее арифметическое и геометрическое
   - Максимальное и минимальное значение
   - Деление с обработкой деления на ноль

2. **Генерация случайных чисел**:
   - Создание массива из 10 случайных чисел (от 0 до 10)
   - Сортировка массива и вывод максимального и минимального значений

3. **Работа с классами**:
   - Создание классов для животных с методами приветствия

4. **Работа с файлами**:
   - Запись и чтение массива случайных чисел из текстового файла
   - Вычисление среднего арифметического из чисел, записанных в файле

## Установка

1. Убедитесь, что у вас установлен Python 3.13. Если он не установлен, загрузите и установите его [с официального сайта Python](https://www.python.org/downloads/).

2. Убедитесь, что у вас установлен Git. Если он не установлен, загрузите и установите его [с официального сайта Git](https://git-scm.com/downloads).

3. Склонируйте репозиторий на свой компьютер:
   ```bash
   git clone https://github.com/saythe0/python-study-2024
   ```

4. Перейдите в каталог проекта:

   ```bash
   cd LaboratoryApp
   ```

## Запуск приложения

Чтобы запустить приложение, выполните следующую команду в терминале:

```bash
python main.py
```

## Использование

После запуска приложения откроется графический интерфейс, в котором вы сможете вводить данные и выполнять различные функции, доступные в лабораторных работах.

## Использование PyInstaller

1. Для более гибкой настройки упаковки приложения вы можете использовать файл спецификации main.spec.

2. Соберите приложение в один EXE файл используя PyInstaller:

	```bash
	pyinstaller main.spec
	```
	Это создаст исполняемый файл в папке `dist`.
