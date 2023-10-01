import computational_geometry_nesting_check as nch
import re

"""
Выполняет обработку файлов с исходными данными и вывод результата.
Файл "files.txt" в первой строке содержит путь к файлу, в который будут выводиться результаты.
Остальные стороки содержат пути к файлам, каждый из которых задает пару многоугольников,
вложенность которых задается. При задании многоугольника указывается его "имя", направление обхода точек
(> - по часовой, < - против) и последовательность точек в виде пар целочисленных координат
(одна пара - одна строка). Повторять первую точку в конце НЕ нужно.
Результат выводится в виде строки -
"<название исходного файла> - (false|<имя многоугольника вложенного в другой>)"
Примеры представлены в файлах "results.txt", "test1.txt", "test2.txt"...
"""
def process_files():
    with open("files.txt") as files:
        output_file = files.readline().strip()
        with open(output_file, "w") as output:
            for path in files:
                next = False
                path = path.strip()
                if path != "":
                    with open(path) as file:
                        polygons = []
                        for line in file:
                            line = line.strip()
                            if re.fullmatch(r"\w+\s+(\<|\>)", line) != None:
                                if len(polygons) >= 2:
                                    output.write(path + " - Incorrect input: too much polygons\n")
                                    next = True
                                    break
                                polygons.append(nch.Polygon())
                                polygons[-1].name = line[:-1].strip()
                                polygons[-1].direction = line[-1]
                            else:
                                if line == "":
                                    continue
                                if len(polygons) == 0:
                                    output.write(path + " - Incorrect input: incorrect polygon description\n")
                                    next = True
                                    break
                                match = re.fullmatch(r"(-?\d+)\s+(-?\d+)", line)
                                if match == None:
                                    output.write(path + " - Incorrect input: incorrect point description\n")
                                    next = True
                                    break
                                polygons[-1].points.append((int(match.group(1)), int(match.group(2))))
                        if len(polygons) < 2 and not next:
                            output.write(path + " - Incorrect input: too few polygons\n")
                            next = True
                    if next:
                        continue
                    else:
                        output.write(path + " - " + nch.nesting_check(polygons[0], polygons[1]) + "\n")


if __name__ == "__main__":
    process_files()