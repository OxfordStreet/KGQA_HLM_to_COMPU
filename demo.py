# from pyltp import SentenceSplitter
# from pyltp import Segmentor
# import os

# LTP_DATA_DIR = 'C:/Users/73949/Downloads/ltp_data_v3.4.0/ltp_data_v3.4.0'  # ltp模型目录的路径


# sents = SentenceSplitter.split('元芳你怎么看？我就趴在窗口上看呗！元芳你怎么这样子了？我哪样子了？')
# print(sents)
# print('\n'.join(sents))
# sents = '|'.join(sents)
# print(sents)

# def cut_words(words):
#     segmentor = Segmentor()
#     seg_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
#     segmentor.load(seg_model_path)
#     words = segmentor.segment(words)
#     array_str="|".join(words)
#     array=array_str.split("|")
#     segmentor.release()
#     return array


# from py2neo.database.work import Record


# for i in range(3):
#     print(i)

# dict = [Record({1: 1, 2: 'aa', 'D': 'ae', 'Ty': 45})]
# print(dict[0]['D'])