from preprocessing import *
from util.log_and_config import *
from util.ocr_api import *
from tagging import *
from model.inference import *


def main(img: str, model: str, tokenizer: str, device: str, finder) -> json:

    logger = get_logger()

    with timer("api", logger):
        pre_res = call_ocr_api(img)
        bin_img = preprocessing_image(img, pre_res)

        res = call_ocr_api(bin_img)  # 전처리된 img로 api 호출
        email, phone, info_dict = preprocess_for_tagging(res)  # tagging 전처리

        texts, tags = inference(info_dict, model, tokenizer, device, finder)
        output = extract_info(texts, tags, finder)

        output["email"] = email
        output["phone"] = phone

        # logger.info( # encoding issue
        #     f"email : {output['email']}, phone : {output['phone']}, LOC : {output['LOC']}, name : {output['PER']}, ORG : {output['ORG']}, JOB : {output['JOB']}"
        # )

        return output
