from cnocr import CnOcr

img_fp = 'image.png'
ocr = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
out = ocr.ocr(img_fp)

print(out)

for i in out:
    print(i['text'])