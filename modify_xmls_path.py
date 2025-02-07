#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import os.path
from xml.etree.ElementTree import parse, Element
import argparse
from tqdm import tqdm

def modify_xml_path(
        xmls_path: str, # 所有XML文档的路径，"./path/to/Annotations"
        img_format: str, # 图像的格式，一般是".jpg"
        images_path: str  # 所有图像存放的路径，"./path/to/Images"
):
    files = os.listdir(xmls_path) # 得到Annotations文件夹下所有文件名称
    for xmlFile in tqdm(files): # 遍历所有Annotation文件夹下的文件
        if not os.path.isdir(xmlFile):  # 跳过文件夹
            print(xmlFile)
            pass
        xmlfile_path = os.path.join(xmls_path, xmlFile)  # 路径拼接，得到.xml文件的具体路径"./path/to/Annotations/xxx.xml"
		file_name = os.path.splitext(xmlFile)[0]  # 获得.xml文件后缀.前的文件名
        img_name = file_name + img_format  # 获得对应图像的文件名（含后缀），前提是VOC格式下，图像和注释文件的名字一致
        new_path_value = images_path + img_name  # 希望修改后<path>的属性值，"./path/to/Images/xxx.jpg"
        
        dom = parse(xmlfile_path)  # 解析.xml文件，并返回一个表示整个XML文档的对象
        root = dom.getroot()  # 从DOM对象中获取XML文档的根元素
        root.find('path').text = new_path_value  # 修改<path>当前的属性值
        print('path after change')
        dom.write(xmlfile_path, xml_declaration=True)  # 写入原文件
        pass

def main():
    parser = argparse.ArgumentParser(
        description='This script is to modify <path> in voc format xmls')
    parser.add_argument('--xmls_path', type=str, default="./shrimp_fry/Annotations/",
                        help='path to xml files directory.')
    parser.add_argument('--images_path', type=str, default="./shrimp_fry/JPEGImages/",
                        help='path to image files directory.')
    parser.add_argument('--img_format', type=str, default=".jpg",
                        help='format of img file.')
    args = parser.parse_args()

    modify_xml_path(args.xmls_path, args.img_format, args.images_path) # 调用修改函数

if __name__ == '__main__':
    main()
