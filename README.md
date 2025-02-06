# modify-xmls-path
modify &lt;path> values of XML annotation files in batches


## Why do you need to modify the value of &lt;path>
The current image path of the dataset is different from the path stored when the image was marked.

## Pre-set premise
Pascal VOC format, annotated by LabelImg, the image and its corresponding .xml annotation file have the same name.

## Usage
```bash
python modify_xml_path.py \
--xmls_path ./path/to/Annotations \
--images_path ./path/to/Images \
--img_format .jpg
```
