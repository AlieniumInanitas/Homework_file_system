class FileInfo:
    """Хранит данные о файле"""
    def __init__(self, file_name, line_count):
        self.file_name = file_name
        self.line_count = line_count

class FileMerge:
    """Сливает список файлов в новый файл в порядке возрастания кол-ва строк"""
    def __init__(self):
        self.files_info = []

    def __line_count (self, files_names:list):
        for file_name in files_names:
            with open(file_name, encoding='utf-8') as f:
                line_count = len(f.readlines())
                file_info = FileInfo(file_name, line_count)
                self.files_info.append(file_info)

    def file_merge (self, file_name:list):
        self.__line_count(file_name)
        sorted_files = sorted(self.files_info, key=lambda x: x.line_count)
        with open('merged.txt', 'w', encoding='utf-8') as f:
            for file in sorted_files:
                with open(file.file_name, encoding='utf-8') as d:
                    f.write(file.file_name + '\n')
                    f.write(str(file.line_count) + '\n')
                    f.write(d.read() + '\n')
            
            
f = ['1.txt', '2.txt', '3.txt']
file_list = FileMerge()
file_list.file_merge(f)


