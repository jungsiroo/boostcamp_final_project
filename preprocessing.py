from util.image_processing import *
from serialization import *
import pprint
import json
from typing import DefaultDict, Tuple

"""
model에 들어 가기 전 email, phone 추출 및 preprocessing Module
"""


def preprocessing_image(img: bytes, ocr_output: Dict) -> bytes:
    img_degree, mid_point_x, mid_point_y = find_degree_and_point(ocr_output)

    # 2. rotate_image : 파악한 정보를 통해 이미지를 알맞게 회전시킨다.
    rotate_img = rotate_image(img, img_degree, mid_point_x, mid_point_y)

    # 3. crop_image : 이미지에서 명함만 인식하여 crop한다.
    preprocessed_img = crop_image(rotate_img)

    # 4. type to binary : bytes 형태로 변환
    bin_img = img_to_binary(preprocessed_img)

    return bin_img


def preprocess_for_tagging(ocr_output: json):
    info_dict = get_serialization_string(ocr_output)

    email = info_dict["email"]
    phone = info_dict["phone"]

    del info_dict["email"]
    del info_dict["phone"]
    info_dict = " ".join(info_dict.values())

    return email, phone, info_dict

