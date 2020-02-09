#!/usr/bin/python
# coding=utf-8

import os
import sys
import shutil
import re

file_name = os.path.basename(__file__)
file_path = os.path.abspath(__file__)
root_path = file_path.replace("/script/" + file_name, "")
template_path = root_path + "/script/template"

category_map = {
    "arithmetic": "算法",
    "database": "数据库",
    "shell": "Shell",
    "multithreading": "多线程"
}


# 判断是哪种类型的题目
def get_title_category():
    print("题目类型：")
    print("1. 算法")
    print("2. 数据库")
    print("3. Shell")
    print("4. 多线程")
    sys.stdout.write("请输入题目类型的序号（默认 1）>")
    title_category_index = sys.stdin.readline().replace("\n", "")
    if title_category_index == "1":
        title_category = "arithmetic"
    elif title_category_index == "2":
        title_category = "database"
    elif title_category_index == "3":
        title_category = "shell"
    elif title_category_index == "4":
        title_category = "multithreading"
    elif title_category_index == "":
        title_category = "arithmetic"
    else:
        print(title_category_index)
        sys.stdout.write("您输入的题目类型有误，请重新输入:")
        title_category = get_title_category()
    return title_category


title_category = get_title_category()


# 需要知道题目的标题以及编号
def get_title_index():
    sys.stdout.write("请输入题目的编号 >")
    title_index = sys.stdin.readline().replace("\n", "")
    if title_index == "":
        print("请不要输入空的内容，下面请重新输入：")
        title_index = get_title_index()
    return title_index


title_index = get_title_index()


def get_title_name():
    sys.stdout.write("请输入题目的标题 >")
    title_name = sys.stdin.readline().replace("\n", "")
    if title_name == "":
        print("请不要输入空的内容，下面请重新输入：")
        title_name = get_title_name()
    return title_name


title_name = get_title_name()


# 生成文本文件，文件名为 <序号.md>，文件内容使用固定模板
def generate_new_title_file(root_path, template_path, title_category, title_index):
    new_title_file_path = root_path + "/" + title_category + "/" + title_index + ".md"
    if os.path.exists(new_title_file_path):
        print("您需要生成的 [" + title_index + ".md] 文件已存在")
        print("退出脚本")
        exit(0)
    shutil.copy2(template_path + "/template.md", new_title_file_path)


generate_new_title_file(root_path, template_path, title_category, title_index)

# 修改 SUMMARY.md 文件，为该文件加上目录
summary_file_path = root_path + "/SUMMARY.md"
summary_fd = open(summary_file_path, "r+")


def insert_specify_file_line(summary_file_path, line_num, content):
    lines = []
    f = open(summary_file_path, 'r')
    for line in f:
        lines.append(line)
    f.close()
    lines.insert(line_num, content + "\n")
    s = ''.join(lines)
    f = open(summary_file_path, 'w+')  # 重新写入文件
    f.write(s)
    f.close()
    del lines[:]  # 清空列表


# 标识目前处于哪一个目录
mark_category = ""
# 将数据初始化到
for (line_num, line) in enumerate(summary_fd):
    # mark_category == "" 表示未进入目录的情况
    # 然后查找正则表示找到需要进入的目录
    if mark_category == "":
        if re.search("\\* \\[" + category_map[title_category] + "\\]\\(.*\\)", line, flags=0) is not None:
            # 随便给一个空格，表示已经进入了目录
            mark_category = " "
    elif mark_category == " ":
        current_index = re.search("\\(.*\\)", line, flags=0) \
            .group(0) \
            .replace("(" + title_category + "/", "") \
            .replace(".md)", "")
        if str(line).startswith("*"):
            # 如果进入下一个目录则说明这是最大的一条记录
            insert_specify_file_line(
                summary_file_path, line_num,
                "  * [" + title_index + ". " + title_name + "](" + title_category + "/" + title_index + ".md)")
            break
        elif int(current_index) > int(title_index):
            insert_specify_file_line(
                summary_file_path, line_num,
                "  * [" + title_index + ". " + title_name + "](" + title_category + "/" + title_index + ".md)")
            break
