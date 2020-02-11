#!/usr/bin/python
# coding=utf-8

import os
import sys
import datetime
import shutil

numToMonth = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

file_name = os.path.basename(__file__)
file_path = os.path.abspath(__file__)
root_path = file_path.replace("/script/" + file_name, "") + "/src"


def split_file_suffix(path):
    split_arr = str(path).split("/")
    file_name_arr = split_arr[split_arr.__len__() - 1].split(".")
    suffix = file_name_arr[file_name_arr.__len__() - 1]
    return "." + suffix


def split_file_prefix(path):
    split_arr = str(path).split("/")
    file_name_arr = split_arr[split_arr.__len__() - 1].split(".")
    prefix = file_name_arr[0]
    return prefix


def main(path):
    print("请输入图片的路径:")
    sys.stdout.write("> ")
    picture_file = sys.stdin.readline().replace("\n", "")
    if not os.path.exists(picture_file):
        print("文件不存在 [" + picture_file + "]")
        exit(0)
    file_time_path = "/" + str(datetime.datetime.now().year) + "/" + numToMonth[datetime.datetime.now().month]
    # 检查文件夹是否存在
    dirs = path + file_time_path + "/"
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    # 新的文件路径
    file_name_list = []
    for rootPath, dirs, files in os.walk(dirs):
        for file_name in files:
            file_name_list.append(int(split_file_prefix(file_name)))
    try:
        # 找出原路径下最大的文件，然后在其上加一为新序号
        num = max(file_name_list)
        new_file_index = str(num + 1)
    except ValueError:
        # 如果没找到则说明这是第一个文件
        new_file_index = "1"
    web_picture_url = file_time_path + "/" + new_file_index + split_file_suffix(picture_file)
    # 拼接文件名
    dest_file_path = path + web_picture_url
    print("传送文件到 [" + dest_file_path + "]")
    # 传送文件
    shutil.copy(picture_file, dest_file_path)
    # 打印 markdown 使用的路径
    print("markdown 请使用这个路径: ![](/static" + web_picture_url + ")")


path = root_path + "/static"
main(path)
