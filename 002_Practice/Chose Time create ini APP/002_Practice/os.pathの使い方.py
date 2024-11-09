import os

#os.path.join()⇒将多个路径合并成一个路径
path = os.path.join("home", "user", "documents", "file.txt")
print(path)  # 输出: home/user/documents/file.txt (在 Windows 上可能会输出 home\user\documents\file.txt)

#os.path.basename()⇒返回路径中的最后一个部分，即文件名或目录名
path = "/home/user/documents/file.txt"
basename = os.path.basename(path)
print(basename)  # 输出: file.txt

#os.path.dirname()⇒返回路径中的目录部分，不包括文件名
path = "/home/user/documents/file.txt"
dirname = os.path.dirname(path)
print(dirname)  # 输出: /home/user/documents

#os.path.split()⇒将路径拆分为目录和文件名两部分，返回一个元组
path = "/home/user/documents/file.txt"
dir_part, file_part = os.path.split(path)
print(dir_part)  # 输出: /home/user/documents
print(file_part)  # 输出: file.txt

#os.path.exists()⇒判断路径（文件或目录）是否存在
path = "/home/user/documents/file.txt"
exists = os.path.exists(path)
print(exists)  # 输出: 如果文件存在则为 True，否则为 False

#os.path.isfile()⇒判断路径是否为一个文件
path = "/home/user/documents/file.txt"
is_file = os.path.isfile(path)
print(is_file)  # 输出: 如果是文件则为 True，否则为 False

#os.path.isdir()⇒判断路径是否为一个目录
path = "/home/user/documents"
is_dir = os.path.isdir(path)
print(is_dir)  # 输出: 如果是目录则为 True，否则为 False

#os.path.abspath()⇒返回路径的绝对路径
path = "documents/file.txt"
abs_path = os.path.abspath(path)
print(abs_path)  # 输出: 绝对路径，如 /home/user/documents/file.txt

#os.path.getsize()⇒返回文件的大小（字节数）
path = "/home/user/documents/file.txt"
size = os.path.getsize(path)
print(size)  # 输出: 文件的字节大小，如 1024

#os.path.splitext()⇒将路径拆分为文件名和扩展名两部分，返回一个元组
path = "/home/user/documents/file.txt"
filename, file_extension = os.path.splitext(path)
print(filename)  # 输出: /home/user/documents/file
print(file_extension)  # 输出: .txt