#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import os.path
from xml.etree.ElementTree import parse, Element
import argparse
from tqdm import tqdm

def modify_xml_path(
        xmls_path: str, # 所有xml文件的路径，"./path/to/Annotations"
        img_format: str, # 图像的格式，一般是".jpg"
        images_path: str  # 所有图像存放的路径，"./path/to/Images"
):
    # 得到文件夹下所有文件名称
    files = os.listdir(xmls_path)

    # 遍历文件夹
    for xmlFile in tqdm(files):
        # 判断是否是文件夹,不是文件夹才打开
        if not os.path.isdir(xmlFile):
            print(xmlFile)
            pass
        xmlfile_path = os.path.join(xmls_path, xmlFile)

        # 路径拼接,输入的是具体路径
        dom = parse(xmlfile_path)
        root = dom.getroot()
        # 获得xml文件后缀.前的文件名
        file_name = os.path.splitext(xmlFile)[0]
        # 文件名+后缀，前提是VOC格式下，图像和注释文件的名字一致
        img_name = file_name + img_format
        # 希望修改后<path>的属性值
        new_path_value = images_path + img_name
        # 修改<path>当前的属性值
        root.find('path').text = new_path_value

        print('path after change')
        # 写入原文件
        dom.write(xmlfile_path, xml_declaration=True)
        pass

def main():
    parser = argparse.ArgumentParser(
        description='This script is to modify <path> in voc format xmls')
    parser.add_argument('--xmls_path', type=str, default="./Annotations/",
                        help='path to xml files directory.')
    parser.add_argument('--images_path', type=str, default="./JPEGImages/",
                        help='path to image files directory.')
    parser.add_argument('--img_format', type=str, default=".jpg",
                        help='format of img file.')
    args = parser.parse_args()

    modify_xml_path(args.xmls_path, args.img_format, args.images_path)


if __name__ == '__main__':
    main()
