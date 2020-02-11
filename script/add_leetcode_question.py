#!/usr/bin/python
# coding=utf-8

import os
import sys
import shutil
import re

file_name = os.path.basename(__file__)
file_path = os.path.abspath(__file__)
root_path = file_path.replace("/script/" + file_name, "") + "/src"
summary_path = root_path + "/SUMMARY.md"
template_path = file_path.replace(file_name, "template")


# 需要知道题目的标题以及编号
def get_title_index():
    sys.stdout.write("请输入题目的编号 >")
    title_index = sys.stdin.readline().replace("\n", "")
    if title_index == "":
        print("请不要输入空的内容，下面请重新输入：")
        title_index = get_title_index()
    if int(title_index) <= 0:
        print("请不要输入小于等于 0 的编号")
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
def calculate_file_path(index):
    factor = int(index) // 100
    start_index = factor * 100 + 1
    end_index = factor * 100 + 99
    return "content/" + str(start_index) + "-" + str(end_index)


def generate_new_title_file(root_path, template_path, title_index):
    new_title_directory_path = root_path + "/" + calculate_file_path(title_index)
    if not os.path.exists(new_title_directory_path):
        os.makedirs(new_title_directory_path)
    new_title_file_path = new_title_directory_path + "/" + title_index + ".md"
    if os.path.exists(new_title_file_path):
        print("您需要生成的 [" + title_index + ".md] 文件已存在")
        print("退出脚本")
        exit(0)
    shutil.copy2(template_path + "/template.md", new_title_file_path)


generate_new_title_file(root_path, template_path, title_index)

# 修改 SUMMARY.md 文件，将该文件加入目录
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
    f = open(summary_file_path, 'w')
    f.write(s)
    f.close()


is_write = 0
last_line_num = 0
for (line_num, line) in enumerate(summary_fd):
    # 跳过空行
    if str(line).strip(" ") == "" or line == "\n" \
            or str(line).__contains__("* [项目介绍](README.md)") \
            or str(line).startswith("#"):
        continue
    last_line_num = line_num
    current_index = str(line).split("/")[2].replace(".md)", "")
    if int(current_index) > int(title_index):
        insert_specify_file_line(
            summary_path, line_num,
            "* [" + title_index + ". " + title_name + "]("
            + calculate_file_path(title_index) + "/" + title_index + ".md)"
        )
        is_write = 1
        break

if is_write == 0:
    insert_specify_file_line(
        summary_path, last_line_num + 1,
        "* [" + title_index + ". " + title_name + "]("
        + calculate_file_path(title_index) + "/" + title_index + ".md)"
    )
