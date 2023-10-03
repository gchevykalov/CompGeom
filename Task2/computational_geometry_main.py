from computational_geometry_quick_hull import convex_hull
import re

"""
Выполняет обработку файлов с исходными данными и вывод результата.
Файл "files.txt" содержит пути к файлам, каждая строка задает пару файлов in/out.
Набор точек задается в виде пар целочисленных координат: одна строка - одна точка, координаты x y через пробел.
Пример представлен в файле "test.txt".
Строится тонкая оболочка - точки на одной прямой исключаются.
Вывод результата производится в таком же формате. Точки записываются начиная с самой левой-нижней против часовой.
Начальная точка в выводе не повторяется.
"""
def process_files():
    with open("files.txt") as files:
        for lineFiles in files:
            next = False
            pathes = lineFiles.split('/')
            if len(pathes) != 2:
                print("Incorrect in/out description: ", lineFiles)
                continue
            pathin = pathes[0].strip()
            pathout = pathes[1].strip()
            if pathin != "":
                pointList = []
                with open(pathin) as inFile:
                    for line in inFile:
                        line = line.strip()
                        if line == "":
                            continue
                        match = re.fullmatch(r"(-?\d+)\s+(-?\d+)", line)
                        if match == None:
                            print(pathin + " - Incorrect input: incorrect point description\n")
                            next = True
                            break
                        pointList.append([int(match.group(1)), int(match.group(2))])
                if next:
                    continue
                else:
                    hull = convex_hull(pointList)
                    with open(pathout, "w") as out:
                        for point in hull:
                            out.write(str(point[0]) + " " + str(point[1]) + "\n")


if __name__ == "__main__":
    process_files()