import torch
import numpy as np

import random
from typing import Optional
import time
import os
import gc


root_filepath = "src/main/"
is_remote_execution = False
torch.set_printoptions(threshold=100000, edgeitems=10000, linewidth=100000)


SETimesByT5Vaswani2017Kocmi2018_0 = {
    'dataset_transformer_name': 'dataset_transformer_setimesbyt5',
    'model_name': 'transformer_vaswani2017',
    'trainer_name': 'model_trainer_kocmi2018',
    'latest_param_filename_tag': '1715672129',
    # corresponds to dictionary 'get' calls in the dataset_loader constructor
    'dataset_transformer_hyperparameters': {
        'sentence_length_min_percentile': 5,
        'sentence_length_max_percentile': 95,
        'parsed_dataset_filename': 'setimes_parsed-1715586293'
    },
    # corresponds to dictionary 'get' calls in the model constructor
    'model_hyperparameters': {
        'd_model': 256,
        'nhead': 8,
        # number of encoders is 3 times that of decoders, following Xue 2021 - ByT5 - Sec 3.1
        'num_encoder_layers': 9,
        'num_decoder_layers': 3,
        'dim_feedforward': 2048,
        'dropout': 0.1,
        'activation': torch.nn.functional.relu,
        'custom_encoder': None,
        'custom_decoder': None,
        'layer_norm_eps': 1e-5,
        'batch_first': True,
        'norm_first': False,
        'bias': True,
        'device': None,
        'dtype': None
    },
    # corresponds to dictionary 'get' calls in the trainer constructor
    'trainer_hyperparameters': {
        # optimization and lr schedule following Kocmi 2018 - Trivial TL - Sec 3
        'optimizer_name': 'Adam',
        'lr_scheduler_name': 'ExponentialLR',
        'initial_lr': 0.001,
        'exp_decay': 0.5,
        'epochs': 10,
        'epoch_starting_index': 0,
        'batch_size_limit': 175,
        'element_difference_limit': 19,
        'batch_starting_index': 765
    }
}

SETimesByT5Vaswani2017Kocmi2018_1 = {
    'dataset_transformer_name': 'dataset_transformer_setimesbyt5',
    'model_name': 'transformer_vaswani2017',
    'trainer_name': 'model_trainer_kocmi2018',
    'latest_param_filename_tag': '1715672186',
    # corresponds to dictionary 'get' calls in the dataset_loader constructor
    'dataset_transformer_hyperparameters': {
        'sentence_length_min_percentile': 5,
        'sentence_length_max_percentile': 95,
        'parsed_dataset_filename': 'setimes_parsed-1715586974'
    },
    # corresponds to dictionary 'get' calls in the model constructor
    'model_hyperparameters': {
        'd_model': 256,
        'nhead': 8,
        # number of encoders is 3 times that of decoders, following Xue 2021 - ByT5 - Sec 3.1
        'num_encoder_layers': 9,
        'num_decoder_layers': 3,
        'dim_feedforward': 1796,
        'dropout': 0.1,
        'activation': torch.nn.functional.relu,
        'custom_encoder': None,
        'custom_decoder': None,
        'layer_norm_eps': 1e-5,
        'batch_first': True,
        'norm_first': False,
        'bias': True,
        'device': None,
        'dtype': None
    },
    # corresponds to dictionary 'get' calls in the trainer constructor
    'trainer_hyperparameters': {
        # optimization and lr schedule following Kocmi 2018 - Trivial TL - Sec 3
        'optimizer_name': 'Adam',
        'lr_scheduler_name': 'ExponentialLR',
        'initial_lr': 0.001,
        'exp_decay': 0.5,
        'epochs': 10,
        'epoch_starting_index': 1,
        'batch_size_limit': 250,
        'element_difference_limit': 19,
        'batch_starting_index': 0
    }
}

SETimesByT5Vaswani2017Kocmi2018_2 = {
    'dataset_transformer_name': 'dataset_transformer_setimesbyt5',
    'model_name': 'transformer_vaswani2017',
    'trainer_name': 'model_trainer_kocmi2018',
    'latest_param_filename_tag': '1715672061',
    # corresponds to dictionary 'get' calls in the dataset_loader constructor
    'dataset_transformer_hyperparameters': {
        'sentence_length_min_percentile': 5,
        'sentence_length_max_percentile': 95,
        'parsed_dataset_filename': 'setimes_parsed-1715586361'
    },
    # corresponds to dictionary 'get' calls in the model constructor
    'model_hyperparameters': {
        'd_model': 128,
        'nhead': 8,
        # number of encoders is 3 times that of decoders, following Xue 2021 - ByT5 - Sec 3.1
        'num_encoder_layers': 9,
        'num_decoder_layers': 3,
        'dim_feedforward': 1024,
        'dropout': 0.1,
        'activation': torch.nn.functional.relu,
        'custom_encoder': None,
        'custom_decoder': None,
        'layer_norm_eps': 1e-5,
        'batch_first': True,
        'norm_first': False,
        'bias': True,
        'device': None,
        'dtype': None
    },
    # corresponds to dictionary 'get' calls in the trainer constructor
    'trainer_hyperparameters': {
        # optimization and lr schedule following Kocmi 2018 - Trivial TL - Sec 3
        'optimizer_name': 'Adam',
        'lr_scheduler_name': 'ExponentialLR',
        'initial_lr': 0.001,
        'exp_decay': 0.5,
        'epochs': 10,
        'epoch_starting_index': 1,
        'batch_size_limit': 400,
        'element_difference_limit': 19,
        'batch_starting_index': 0
    }
}

loss_weights_0 = torch.tensor([0, 0, 0.244293498, 0.354252208, 0.119055746, 0.129490827, 0.234447, 0.331966255, 0.062493498, 0.200436672, 0.128134531, 0.115730135, 0.114789455, 0.111928721, 0.120232896, 0.172708905, 0.091552235, 0.18382728, 0.167772254, 0.221570123, 0.26933557, 0.207267199, 0.161156936, 0.163208063, 0.206129376, 0.1923278, 0.246448966, 0.309805116, 0.312319847, 0.341492611, 0.287077958, 0.317765776, 0.282694925, 0.328107375, 0.305618951, 0.342956521, 0.33013427, 0.36810305, 0.29995848, 0.39787945, 0.36195021, 0.231575726, 0.238716465, 0.228047462, 0.589442629, 0.428540415, 0.349514641, 0.428583838, 0.372321337, 0.35910363, 0.314836573, 0.359830778, 0.329628544, 0.358553271, 0.38731315, 0.301171514, 0.414866271, 0.454463773, 0.410552656, 0.418645272, 0.489374491, 0.60674051, 0.415410876, 0.387694004, 0.469862412, 0.387466491, 0.404244134, 0.410692024, 0.3650963, 0.328332631, 0.362047807, 0.390990331, 0.407611852, 0.353090879, 0.519082435, 0.465516001, 0.382984849, 0.382904558, 0.417591599, 0.47406963, 0.513595183, 0.561900207, 0.600687916, 0.552947486, 0.672534847, 0.775971182, 0.728910416, 0.783069437, 0.726598021, 0.870987145, 0.761128877, 0.716818395, 0.708372474, 0.70507743, 0.731312344, 0.718124592, 0.931839821, 0.675783865, 0.863679642, 0.79786095, 0.870987145, 0.888835536, 0.845831251, 0.845831251, 0.870987145, 0.831986963, 0.817320914, 0.888835536, 0.82798286, 0.931839821, 0.900147142, 0.91399143, 0.91399143, 0.956995715, 0.931839821, 1, 0.900147142, 0.870987145, 0.870987145, 1, 0.900147142, 0.888835536, 0.956995715, 0.824221583, 1, 1, 0.956995715, 1, 0.931839821, 0.931839821, 0.956995715, 0.956995715, 0.956995715, 0.888835536, 0.931839821, 1, 0.900147142, 0.91399143, 0.956995715, 0.956995715, 0.956995715, 1, 1, 1, 0.900147142, 0.931839821, 0.900147142, 0.931839821, 0.956995715, 0.91399143, 1, 0.956995715, 1, 1, 1, 1, 1, 0.956995715, 1, 1, 1, 1, 1, 1, 1, 0.931839821, 1, 0.956995715, 1, 1, 0.956995715])
loss_weights_1 = torch.tensor([0, 0, 0.283786926, 0.387999164, 0.165094134, 0.174983875, 0.274455009, 0.366877881, 0.111487844, 0.242222071, 0.173698459, 0.16194232, 0.1610508, 0.158339569, 0.166209765, 0.215943364, 0.139027964, 0.226480689, 0.211264704, 0.262251081, 0.307520293, 0.248695632, 0.204995104, 0.206939038, 0.247617272, 0.23453697, 0.285829749, 0.345874889, 0.3482582, 0.375906387, 0.324335459, 0.353419523, 0.320181484, 0.363220667, 0.341907494, 0.377293793, 0.365141636, 0.401126157, 0.336542841, 0.429346435, 0.395294867, 0.271733788, 0.27850135, 0.268389913, 0.610898469, 0.458405049, 0.383509184, 0.458446203, 0.405123996, 0.39259705, 0.350643401, 0.393286196, 0.36466234, 0.392075452, 0.419332333, 0.337692481, 0.44544552, 0.482973645, 0.441357336, 0.449027029, 0.51605992, 0.627292358, 0.445961663, 0.419693282, 0.497567547, 0.419477659, 0.435378499, 0.44148942, 0.398276541, 0.363434152, 0.395387363, 0.422817343, 0.438570219, 0.386898527, 0.544215318, 0.493448281, 0.415230229, 0.415154135, 0.448028421, 0.501554895, 0.539014832, 0.584795422, 0.621556075, 0.576310573, 0.689648265, 0.78767899, 0.743077631, 0.794406288, 0.740886083, 0.877729392, 0.773612348, 0.731617543, 0.723613008, 0.720490164, 0.745354034, 0.732855478, 0.93540189, 0.692727489, 0.870803781, 0.808424792, 0.877729392, 0.894645021, 0.853888152, 0.853888152, 0.877729392, 0.84076737, 0.826867773, 0.894645021, 0.836972522, 0.93540189, 0.90536548, 0.918486261, 0.918486261, 0.959243131, 0.93540189, 1, 0.90536548, 0.877729392, 0.877729392, 1, 0.90536548, 0.894645021, 0.959243131, 0.833407811, 1, 1, 0.959243131, 1, 0.93540189, 0.93540189, 0.959243131, 0.959243131, 0.959243131, 0.894645021, 0.93540189, 1, 0.90536548, 0.918486261, 0.959243131, 0.959243131, 0.959243131, 1, 1, 1, 0.90536548, 0.93540189, 0.90536548, 0.93540189, 0.959243131, 0.918486261, 1, 0.959243131, 1, 1, 1, 1, 1, 0.959243131, 1, 1, 1, 1, 1, 1, 1, 0.93540189, 1, 0.959243131, 1, 1, 0.959243131])

english_char_mappings = {
    ord(" "): ord(" "),
    ord("e"): ord("e"),
    ord("t"): ord("t"),
    ord("a"): ord("a"),
    ord("i"): ord("i"),
    ord("o"): ord("o"),
    ord("n"): ord("n"),
    ord("r"): ord("r"),
    ord("s"): ord("s"),
    ord("h"): ord("h"),
    ord("l"): ord("l"),
    ord("d"): ord("d"),
    ord("c"): ord("c"),
    ord("u"): ord("u"),
    ord("m"): ord("m"),
    ord("p"): ord("p"),
    ord("f"): ord("f"),
    ord("g"): ord("g"),
    ord("y"): ord("y"),
    ord("b"): ord("b"),
    ord("w"): ord("w"),
    ord("v"): ord("v"),
    ord(","): ord(","),
    ord("."): ord("."),
    ord("k"): ord("k"),
    ord("T"): ord("T"),
    ord("S"): ord("S"),
    ord("0"): ord("0"),
    ord("A"): ord("A"),
    ord("-"): ord("-"),
    ord("B"): ord("B"),
    ord("M"): ord("M"),
    ord("\""): ord("\""),
    ord("E"): ord("E"),
    ord("P"): ord("P"),
    ord("C"): ord("C"),
    ord("I"): ord("I"),
    ord("1"): ord("1"),
    ord("'"): ord("'"),
    ord("j"): ord("j"),
    ord("2"): ord("2"),
    ord("R"): ord("R"),
    ord("U"): ord("U"),
    ord("K"): ord("K"),
    ord("D"): ord("D"),
    ord("x"): ord("x"),
    ord("H"): ord("H"),
    ord("F"): ord("F"),
    ord("N"): ord("N"),
    ord("G"): ord("G"),
    ord("/"): ord("/"),
    ord("O"): ord("O"),
    ord(")"): ord(")"),
    ord("("): ord("("),
    ord("9"): ord("9"),
    ord("W"): ord("W"),
    ord("z"): ord("z"),
    ord("5"): ord("5"),
    ord("3"): ord("3"),
    ord("J"): ord("J"),
    ord("4"): ord("4"),
    ord("q"): ord("q"),
    ord("L"): ord("L"),
    ord("6"): ord("6"),
    ord("7"): ord("7"),
    ord("8"): ord("8"),
    ord("V"): ord("V"),
    ord("["): ord("["),
    ord("]"): ord("]"),
    ord(":"): ord(":"),
    ord("Z"): ord("Z"),
    ord("%"): ord("%"),
    ord("Y"): ord("Y"),
    ord(";"): ord(";"),
    ord("–"): ord("-"),
    ord("?"): ord("?"),
    ord("X"): ord("X"),
    ord("$"): ord("$"),
    ord("’"): ord("'"),
    ord("Q"): ord("Q"),
    ord("…"): ord("\u0120"),
    ord("!"): ord("\u0120"),
    ord("&"): ord("\u0120"),
    ord("ć"): ord("\u0120"),
    ord("”"): ord("\""),
    ord("é"): ord("\u0120"),
    ord("“"): ord("\""),
    ord("ı"): ord("\u0120"),
    ord("ü"): ord("\u0120"),
    ord("+"): ord("\u0120"),
    ord("ç"): ord("\u0120"),
    ord("ˈ"): ord("'"),
    ord("ö"): ord("\u0120"),
    ord("ë"): ord("\u0120"),
    ord("Ç"): ord("\u0120"),
    ord("ğ"): ord("\u0120"),
    ord("č"): ord("\u0120"),
    ord("š"): ord("\u0120"),
    ord("‘"): ord("'"),
    ord("ž"): ord("\u0120"),
    ord("*"): ord("\u0120"),
    ord("ş"): ord("\u0120"),
    ord("б"): ord("\u0120"),
    ord("Š"): ord("\u0120"),
    ord("İ"): ord("\u0120"),
    ord("à"): ord("\u0120"),
    ord("г"): ord("\u0120"),
    ord("ï"): ord("\u0120"),
    ord("Ü"): ord("\u0120"),
    ord("—"): ord("-"),
    ord("€"): ord("\u0120"),
    ord("Ö"): ord("\u0120"),
    ord("đ"): ord("\u0120"),
    ord("\\"): ord("\u0120"),
    ord("Ι"): ord("\u0120"),
    ord("Α"): ord("A"),
    ord("`"): ord("'"),
    ord("_"): ord("\u0120"),
    ord("="): ord("\u0120"),
    ord("@"): ord("\u0120"),
    ord("А"): ord("A"),
    ord("ó"): ord("\u0120"),
    ord("í"): ord("\u0120"),
    ord("â"): ord("\u0120"),
    ord("\x80"): ord("\u0120"),
    ord("Ž"): ord("\u0120"),
    ord("Κ"): ord("K"),
    ord("Ο"): ord("O"),
    ord("р"): ord("p"),
    ord("Ş"): ord("\u0120"),
    ord("á"): ord("\u0120"),
    ord("у"): ord("y"),
    ord("\x93"): ord("\u0120"),
    ord("°"): ord("\u0120"),
    ord("<"): ord("\u0120"),
    ord("½"): ord("\u0120"),
    ord("Т"): ord("T"),
    ord("ø"): ord("\u0120"),
    ord("Ε"): ord("E"),
    ord("#"): ord("\u0120"),
    ord("ý"): ord("\u0120"),
    ord("л"): ord("\u0120"),
    ord("я"): ord("\u0120"),
    ord("�"): ord("\u0120"),
    ord("º"): ord("\u0120"),
    ord("ä"): ord("\u0120"),
    ord("е"): ord("e"),
    ord("о"): ord("o"),
    ord("Đ"): ord("\u0120"),
    ord("è"): ord("\u0120"),
    ord("¾"): ord("\u0120"),
    ord("\x96"): ord("\u0120"),
    ord("æ"): ord("\u0120"),
    ord(">"): ord("\u0120"),
    ord("¦"): ord("\u0120"),
    ord("μ"): ord("\u0120"),
    ord("Č"): ord("\u0120"),
    ord("ñ"): ord("\u0120"),
    ord("х"): ord("x"),
    ord("М"): ord("M"),
    ord("É"): ord("\u0120"),
    ord("±"): ord("\u0120"),
    ord("£"): ord("\u0120"),
    ord("{"): ord("\u0120"),
    ord("}"): ord("\u0120"),
    ord("ъ"): ord("\u0120"),
    ord("а"): ord("\u0120"),
    ord("и"): ord("\u0120")
}

turkish_char_mappings = {
    ord(" "): ord(" "),
    ord("a"): ord("a"),
    ord("e"): ord("e"),
    ord("i"): ord("i"),
    ord("n"): ord("n"),
    ord("r"): ord("r"),
    ord("l"): ord("l"),
    ord("ı"): ord("ı"),
    ord("k"): ord("k"),
    ord("d"): ord("d"),
    ord("t"): ord("t"),
    ord("s"): ord("s"),
    ord("u"): ord("u"),
    ord("m"): ord("m"),
    ord("y"): ord("y"),
    ord("o"): ord("o"),
    ord("ü"): ord("ü"),
    ord("b"): ord("b"),
    ord("ş"): ord("ş"),
    ord("v"): ord("v"),
    ord("g"): ord("g"),
    ord("z"): ord("z"),
    ord("ç"): ord("ç"),
    ord("ğ"): ord("ğ"),
    ord("."): ord("."),
    ord(","): ord(","),
    ord("c"): ord("c"),
    ord("h"): ord("h"),
    ord("p"): ord("p"),
    ord("ö"): ord("ö"),
    ord("'"): ord("'"),
    ord("B"): ord("B"),
    ord("A"): ord("A"),
    ord("f"): ord("f"),
    ord("S"): ord("S"),
    ord("K"): ord("K"),
    ord("0"): ord("0"),
    ord("\""): ord("\""),
    ord("T"): ord("T"),
    ord("M"): ord("M"),
    ord("1"): ord("1"),
    ord("P"): ord("P"),
    ord("D"): ord("D"),
    ord("H"): ord("H"),
    ord("2"): ord("2"),
    ord("E"): ord("E"),
    ord("R"): ord("R"),
    ord("-"): ord("-"),
    ord("G"): ord("G"),
    ord("j"): ord("j"),
    ord("Y"): ord("Y"),
    ord("C"): ord("C"),
    ord("İ"): ord("İ"),
    ord("O"): ord("O"),
    ord("/"): ord("/"),
    ord("F"): ord("F"),
    ord("N"): ord("N"),
    ord("9"): ord("9"),
    ord("5"): ord("5"),
    ord("3"): ord("3"),
    ord("I"): ord("I"),
    ord("4"): ord("4"),
    ord("L"): ord("L"),
    ord("6"): ord("6"),
    ord(")"): ord(")"),
    ord("("): ord("("),
    ord("7"): ord("7"),
    ord("8"): ord("8"),
    ord("U"): ord("U"),
    ord("V"): ord("V"),
    ord(":"): ord(":"),
    ord("["): ord("["),
    ord("]"): ord("]"),
    ord("’"): ord("'"),
    ord("Z"): ord("Z"),
    ord("Ç"): ord("Ç"),
    ord("J"): ord("J"),
    ord("Ü"): ord("Ü"),
    ord("Ş"): ord("Ş"),
    ord("Ö"): ord("Ö"),
    ord("%"): ord("%"),
    ord(";"): ord(";"),
    ord("w"): ord("w"),
    ord("W"): ord("W"),
    ord("â"): ord("â"),
    ord("–"): ord("-"),
    ord("?"): ord("?"),
    ord("x"): ord("x"),
    ord("“"): ord("\""),
    ord("”"): ord("\""),
    ord("X"): ord("X"),
    ord("q"): ord("q"),
    ord("î"): ord("\u0120"),
    ord("&"): ord("\u0120"),
    ord("!"): ord("\u0120"),
    ord("ð"): ord("\u0120"),
    ord("Q"): ord("\u0120"),
    ord("+"): ord("\u0120"),
    ord("þ"): ord("\u0120"),
    ord("‘"): ord("'"),
    ord("é"): ord("\u0120"),
    ord("º"): ord("\u0120"),
    ord("ë"): ord("\u0120"),
    ord("…"): ord("\u0120"),
    ord("б"): ord("\u0120"),
    ord("*"): ord("\u0120"),
    ord("="): ord("\u0120"),
    ord("`"): ord("'"),
    ord("ć"): ord("\u0120"),
    ord("û"): ord("\u0120"),
    ord("Ý"): ord("\u0120"),
    ord("г"): ord("\u0120"),
    ord("—"): ord("\u0120"),
    ord("\\"): ord("\u0120"),
    ord("°"): ord("\u0120"),
    ord("@"): ord("\u0120"),
    ord("č"): ord("\u0120"),
    ord("ó"): ord("\u0120"),
    ord("š"): ord("\u0120"),
    ord("р"): ord("\u0120"),
    ord("_"): ord("\u0120"),
    ord("{"): ord("\u0120"),
    ord("#"): ord("\u0120"),
    ord("^"): ord("\u0120"),
    ord(">"): ord("\u0120"),
    ord("$"): ord("\u0120"),
    ord("đ"): ord("\u0120"),
    ord("í"): ord("\u0120"),
    ord("ø"): ord("\u0120"),
    ord("Š"): ord("\u0120"),
    ord("ž"): ord("\u0120"),
    ord("Þ"): ord("\u0120"),
    ord("л"): ord("\u0120"),
    ord("я"): ord("\u0120"),
    ord("}"): ord("\u0120"),
    ord("±"): ord("\u0120"),
    ord("½"): ord("\u0120"),
    ord("¾"): ord("\u0120"),
    ord("ª"): ord("\u0120"),
    ord("á"): ord("\u0120"),
    ord("É"): ord("\u0120"),
    ord("è"): ord("\u0120"),
    ord("Ğ"): ord("\u0120"),
    ord("ï"): ord("\u0120"),
    ord("ñ"): ord("\u0120"),
    ord("ý"): ord("\u0120"),
    ord("Ž"): ord("\u0120"),
    ord("μ"): ord("\u0120"),
    ord("а"): ord("\u0120"),
    ord("и"): ord("\u0120"),
    ord("у"): ord("\u0120"),
    ord("х"): ord("\u0120"),
    ord("ъ"): ord("\u0120"),
}

class DatasetHolder:

    def __init__(self):
        self.unknown_vocabulary_type = None
        self.padding_vocabulary_type = None
        self.end_of_sequence_type = None
        self.target_vocab = None
        self.target_vocab_array = None
        self.target_vocab_counts = None
        self.source_vocab = None
        self.source_vocab_array = None
        self.source_vocab_counts = None
        self.target_encodings = None
        self.target_encodings_train = None
        self.target_encodings_test = None
        self.source_encodings = None
        self.source_encodings_train = None
        self.source_encodings_test = None
        self.max_src_seq_obs = 0
        self.max_tgt_seq_obs = 0

    def get_unknown_vocabulary_type(self):
        return self.unknown_vocabulary_type

    def set_unknown_vocabulary_type(self, unknown_vocabulary_type):
        self.unknown_vocabulary_type = unknown_vocabulary_type

    def get_padding_vocabulary_type(self):
        return self.padding_vocabulary_type

    def set_padding_vocabulary_type(self, padding_vocabulary_type):
        self.padding_vocabulary_type = padding_vocabulary_type

    def get_end_of_sequence_vocabulary_type(self):
        return self.end_of_sequence_type

    def set_end_of_sequence_vocabulary_type(self, end_of_sequence_type):
        self.end_of_sequence_type = end_of_sequence_type

    def get_target_vocab(self):
        return self.target_vocab

    def set_target_vocab(self, target_vocab):
        self.target_vocab = target_vocab

    def get_target_vocab_numpy(self):
        if self.target_vocab_array is None:
            self.target_vocab_array = np.array(self.target_vocab)
        return self.target_vocab_array

    def get_target_vocab_counts(self):
        return self.target_vocab_counts

    def set_target_vocab_counts(self, target_vocab_counts):
        self.target_vocab_counts = target_vocab_counts

    def get_source_vocab(self):
        return self.source_vocab

    def set_source_vocab(self, source_vocab):
        self.source_vocab = source_vocab

    def get_source_vocab_numpy(self):
        if self.source_vocab_array is None:
            self.source_vocab_array = np.array(self.source_vocab)
        return self.source_vocab_array

    def get_source_vocab_counts(self):
        return self.source_vocab_counts

    def set_source_vocab_counts(self, source_vocab_counts):
        self.source_vocab_counts = source_vocab_counts

    def get_target_encodings(self):
        return self.target_encodings

    def set_target_encodings(self, target_encodings):
        del self.target_encodings
        self.target_encodings = target_encodings
        if is_remote_execution:
            torch.cuda.empty_cache()

    def get_source_encodings(self):
        return self.source_encodings

    def set_source_encodings(self, source_encodings):
        del self.source_encodings
        self.source_encodings = source_encodings
        if is_remote_execution:
            torch.cuda.empty_cache()

    def get_target_encodings_train(self):
        return self.target_encodings_train

    def set_target_encodings_train(self, target_encodings_train):
        del self.target_encodings_train
        self.target_encodings_train = target_encodings_train
        if is_remote_execution:
            torch.cuda.empty_cache()

    def get_source_encodings_train(self):
        return self.source_encodings_train

    def set_source_encodings_train(self, source_encodings_train):
        del self.source_encodings_train
        self.source_encodings_train = source_encodings_train
        if is_remote_execution:
            torch.cuda.empty_cache()

    def get_target_encodings_test(self):
        return self.target_encodings_test

    def set_target_encodings_test(self, target_encodings_test):
        del self.target_encodings_test
        self.target_encodings_test = target_encodings_test
        if is_remote_execution:
            torch.cuda.empty_cache()

    def get_source_encodings_test(self):
        return self.source_encodings_test

    def set_source_encodings_test(self, source_encodings_test):
        del self.source_encodings_test
        self.source_encodings_test = source_encodings_test
        if is_remote_execution:
            torch.cuda.empty_cache()

    def get_max_src_seq_obs(self):
        return self.max_src_seq_obs

    def set_max_src_seq_obs(self, max_src_seq_obs):
        self.max_src_seq_obs = max_src_seq_obs

    def get_max_tgt_seq_obs(self):
        return self.max_tgt_seq_obs

    def set_max_tgt_seq_obs(self, max_tgt_seq_obs):
        self.max_tgt_seq_obs = max_tgt_seq_obs


# class name matches file name
class dataset_transformer_setimesbyt5():

    def __init__(self,
                 datasets_directory=root_filepath+"resources",
                 raw_dataset_directory="raw_datasets/setimes",
                 parsed_dataset_directory="parsed_datasets/setimes",
                 ids_filename='SETIMES.en-tr.ids',
                 en_filename='SETIMES.en-tr.en',
                 tr_filename='SETIMES.en-tr.tr',
                 dataset_hyperparameters=None):
        self.datasets_directory = datasets_directory
        self.raw_dataset_directory = raw_dataset_directory
        self.parsed_dataset_directory = parsed_dataset_directory
        self.ids_filename = ids_filename
        self.en_filename = en_filename
        self.tr_filename = tr_filename
        self.parsed_dataset_filename = None
        if 'parsed_dataset_filename' in dataset_hyperparameters:
            self.parsed_dataset_filename = dataset_hyperparameters['parsed_dataset_filename']
        self.sentence_length_min_percentile = None
        if 'sentence_length_min_percentile' in dataset_hyperparameters:
            self.sentence_length_min_percentile = dataset_hyperparameters['sentence_length_min_percentile']
        self.sentence_length_max_percentile = None
        if 'sentence_length_max_percentile' in dataset_hyperparameters:
            self.sentence_length_max_percentile = dataset_hyperparameters['sentence_length_max_percentile']


    def read_dataset(self):
        dataset_holder = None
        if self.parsed_dataset_filename is not None:
            dataset_holder = torch.load(self.datasets_directory + "/"
                                        + self.parsed_dataset_directory + "/"
                                        + self.parsed_dataset_filename)
        else:
            target_sentences = list()
            source_sentences = list()
            index_file = open(self.datasets_directory + "/" + self.raw_dataset_directory + "/" + self.ids_filename)
            en_file = open(self.datasets_directory + "/" + self.raw_dataset_directory + "/" + self.en_filename)
            tr_file = open(self.datasets_directory + "/" + self.raw_dataset_directory + "/" + self.tr_filename)
            indices = list()
            en_sentences = list()
            tr_sentences = list()
            line_number = 1
            for line in index_file:
                line_segments = line.strip().split()
                if len(line_segments) != 4:
                    print("Line segmentation error on line " + str(line_number))
                    print("Content: " + line)
                    continue
                if line_segments[0].startswith("en") and line_segments[1].startswith("tr"):
                    indices.append((int(line_segments[2]), int(line_segments[3])))
                elif line_segments[0].startswith("tr") and line_segments[1].startswith("en"):
                    indices.append((int(line_segments[3]), int(line_segments[2])))
                else:
                    print("Index parsing error on line " + str(line_number))
                    print("Content: " + line)
                    continue
                line_number = line_number + 1
            for line in en_file:
                en_sentences.append(line.strip())
            for line in tr_file:
                tr_sentences.append(line.strip())
            for index in indices:
                target_sentences.append(en_sentences[index[0] - 1])
                source_sentences.append(tr_sentences[index[1] - 1])
            target_sentence_lengths = list()
            for sentence in target_sentences:
                target_sentence_lengths.append(len(sentence))
            source_sentence_lengths = list()
            for sentence in source_sentences:
                source_sentence_lengths.append(len(sentence))
            target_sentences_length_limited = list()
            source_sentences_length_limited = list()
            target_min_len = int(np.percentile(sorted(target_sentence_lengths), self.sentence_length_min_percentile))
            target_max_len = int(np.percentile(sorted(target_sentence_lengths), self.sentence_length_max_percentile))
            source_min_len = int(np.percentile(sorted(source_sentence_lengths), self.sentence_length_min_percentile))
            source_max_len = int(np.percentile(sorted(source_sentence_lengths), self.sentence_length_max_percentile))
            max_src_seq_obs = 0
            max_tgt_seq_obs = 0
            for i in range(0, len(target_sentences)):
                if (len(target_sentences[i]) > target_min_len and len(target_sentences[i]) <= target_max_len
                        and len(source_sentences[i]) > source_min_len and len(source_sentences[i]) <= source_max_len):
                    if len(source_sentences[i]) > max_src_seq_obs:
                        max_src_seq_obs = len(source_sentences[i])
                    if len(target_sentences[i]) > max_tgt_seq_obs:
                        max_tgt_seq_obs = len(target_sentences[i])
                    target_sentences_length_limited.append(target_sentences[i].translate(english_char_mappings))
                    source_sentences_length_limited.append(source_sentences[i].translate(turkish_char_mappings))
            dataset_holder = DatasetHolder()
            dataset_holder.set_max_src_seq_obs(max_src_seq_obs)
            dataset_holder.set_max_tgt_seq_obs(max_tgt_seq_obs)
            # encode to Pytorch tensors as raw UTF-8 character vocabulary
            # method replicated from Xue 2021 - ByT5 - Introduction, sec 3.1
            unknown_vocabulary_type = "\u0120".encode('utf-8').decode('utf-8')
            padding_vocabulary_type = "\u0121".encode('utf-8').decode('utf-8')
            end_of_sequence_vocabulary_type = "\u0122".encode('utf-8').decode('utf-8')
            dataset_holder.set_unknown_vocabulary_type(unknown_vocabulary_type)
            dataset_holder.set_padding_vocabulary_type(padding_vocabulary_type)
            dataset_holder.set_end_of_sequence_vocabulary_type(end_of_sequence_vocabulary_type)
            target_vocab = list([unknown_vocabulary_type, padding_vocabulary_type, end_of_sequence_vocabulary_type])
            source_vocab = list([unknown_vocabulary_type, padding_vocabulary_type, end_of_sequence_vocabulary_type])
            target_encodings = list()
            source_encodings = list()
            for entry in target_sentences_length_limited:
                encoding = list()
                for character in entry:
                    if character not in target_vocab:
                        target_vocab.append(character)
                    encoding.append(target_vocab.index(character))
                encoding.append(target_vocab.index(end_of_sequence_vocabulary_type))
                target_encodings.append(torch.tensor(encoding))
            for entry in source_sentences_length_limited:
                encoding = list()
                for character in entry:
                    if character not in source_vocab:
                        source_vocab.append(character)
                    encoding.append(source_vocab.index(character))
                encoding.append(target_vocab.index(end_of_sequence_vocabulary_type))
                source_encodings.append(torch.tensor(encoding))
            # fix vocabulary indices using tuple type
            dataset_holder.set_target_vocab(tuple(target_vocab))
            dataset_holder.set_target_encodings(target_encodings)
            dataset_holder.set_source_vocab(tuple(source_vocab))
            dataset_holder.set_source_encodings(source_encodings)
            dataset_holder = DatasetUtils.create_dataset_segments(dataset_holder)
            torch.save(dataset_holder,
                       self.datasets_directory + "/" +
                       self.parsed_dataset_directory + "/" +
                       "setimes_parsed-" + str(int(time.time())))
        return dataset_holder


class Utils:

    def __init__(self):
        pass

    @staticmethod
    def load_python_object(object_path: str, object_attribute: str):
        path_segments = object_path.split('.')
        module = __import__(object_path)
        for segment in path_segments[1:]:
            module = getattr(module, segment)
        return getattr(module, object_attribute)


class DatasetUtils:

    @staticmethod
    def shuffle_dataset(dataset_holder: DatasetHolder):
        new_source_encodings, new_target_encodings = (
            DatasetUtils.shuffle_lists(
                dataset_holder.get_source_encodings(),
                dataset_holder.get_target_encodings()
            )
        )
        dataset_holder.set_source_encodings(new_source_encodings)
        dataset_holder.set_target_encodings(new_target_encodings)
        return dataset_holder

    @staticmethod
    def shuffle_training_dataset(dataset_holder: DatasetHolder):
        new_source_encodings, new_target_encodings = (
            DatasetUtils.shuffle_lists(
                dataset_holder.get_source_encodings_train(),
                dataset_holder.get_target_encodings_train()
            )
        )
        dataset_holder.set_source_encodings(new_source_encodings)
        dataset_holder.set_target_encodings(new_target_encodings)
        return dataset_holder

    @staticmethod
    def shuffle_test_dataset(dataset_holder: DatasetHolder):
        new_source_encodings, new_target_encodings = (
            DatasetUtils.shuffle_lists(
                dataset_holder.get_source_encodings_test(),
                dataset_holder.get_target_encodings_test()
            )
        )
        dataset_holder.set_source_encodings(new_source_encodings)
        dataset_holder.set_target_encodings(new_target_encodings)
        return dataset_holder

    @staticmethod
    def shuffle_lists(source_list, target_list):
        assert len(source_list) == len(target_list)
        list_element_shuffle_indices = list(range(0, len(source_list)))
        random.shuffle(list_element_shuffle_indices)
        new_source_list = list()
        new_target_list = list()
        for i in list_element_shuffle_indices:
            new_source_list.append(source_list[i])
            new_target_list.append(target_list[i])
        assert (len(new_source_list) == len(new_target_list)
                == len(source_list) == len(target_list))
        return new_source_list, new_target_list

    @staticmethod
    def create_dataset_segments(dataset_holder: DatasetHolder):
        split_with_even_target_distribution = False
        iteration = 1
        best_split_target_encodings = None
        best_split_source_encodings = None
        best_split_deviation_from_desired = 1
        segments = 20
        split_size = len(dataset_holder.get_target_encodings()) // segments
        train_size = split_size * (segments - 1)
        while not split_with_even_target_distribution and iteration <= 100:
            segment_attempt_start = time.time()
            dataset_holder = DatasetUtils.shuffle_dataset(dataset_holder)
            target_encodings = dataset_holder.get_target_encodings()
            source_encodings = dataset_holder.get_source_encodings()
            train_set_target_enc = target_encodings[0:train_size]
            test_set_target_enc = target_encodings[train_size:]
            numpy_encodings = list()
            for encoding in train_set_target_enc:
                numpy_encodings.append(encoding.flatten().numpy())
            train_set_target_enc_cts = np.bincount(
                np.concatenate([
                    np.concatenate(numpy_encodings),
                    np.arange(0, 170)
                ])
            )
            numpy_encodings = list()
            for encoding in test_set_target_enc:
                numpy_encodings.append(encoding.flatten().numpy())
            test_set_target_enc_cts = np.bincount(
                np.concatenate([
                    np.concatenate(numpy_encodings),
                    np.arange(0, 170)
                ])
            )
            # terms with probability ~ 1%
            total_5 = train_set_target_enc_cts[5] + test_set_target_enc_cts[5]
            total_40 = train_set_target_enc_cts[40] + test_set_target_enc_cts[40]
            total_42 = train_set_target_enc_cts[42] + test_set_target_enc_cts[42]
            # top 3 terms
            total_7 = train_set_target_enc_cts[7] + test_set_target_enc_cts[7]
            total_15 = train_set_target_enc_cts[15] + test_set_target_enc_cts[15]
            total_12 = train_set_target_enc_cts[12] + test_set_target_enc_cts[12]
            train_dist_goal = (segments - 1)/segments
            test_dist_goal = (1 / segments)
            deviation_from_desired = (
                    np.abs(((segments - 2)/segments) - (train_set_target_enc_cts[5] / total_5)) +
                    np.abs(train_dist_goal - (train_set_target_enc_cts[40] / total_40)) +
                    np.abs(train_dist_goal - (train_set_target_enc_cts[42] / total_42)) +
                    np.abs(train_dist_goal - (train_set_target_enc_cts[7] / total_7)) +
                    np.abs(train_dist_goal - (train_set_target_enc_cts[15] / total_15)) +
                    np.abs(train_dist_goal - (train_set_target_enc_cts[12] / total_12)) +
                    np.abs(test_dist_goal - (test_set_target_enc_cts[5] / total_5)) +
                    np.abs(test_dist_goal - (test_set_target_enc_cts[40] / total_40)) +
                    np.abs(test_dist_goal - (test_set_target_enc_cts[42] / total_42)) +
                    np.abs(test_dist_goal - (test_set_target_enc_cts[7] / total_7)) +
                    np.abs(test_dist_goal - (test_set_target_enc_cts[15] / total_15)) +
                    np.abs(test_dist_goal - (test_set_target_enc_cts[12] / total_12))
            )
            if deviation_from_desired <= 12 * 0.0001:
                split_with_even_target_distribution = True
                best_split_target_encodings = target_encodings
                best_split_source_encodings = source_encodings
                print(f"Found dataset split within tolerance for deviation from uniform distribution over characters")
            if deviation_from_desired < best_split_deviation_from_desired:
                best_split_target_encodings = target_encodings
                best_split_source_encodings = source_encodings
                best_split_deviation_from_desired = deviation_from_desired
            segment_attempt_end = time.time()
            print(f"Completed data split attempt. "
                  f"iteration:{iteration} "
                  f"best_split_deviation_from_desired:{best_split_deviation_from_desired} "
                  f"time_to_complete_attempt:{segment_attempt_end-segment_attempt_start}")
            iteration = iteration + 1
        best_split_source_encodings_train = best_split_source_encodings[0:train_size]
        best_split_target_encodings_train = best_split_target_encodings[0:train_size]
        assert len(best_split_source_encodings_train) == len(best_split_target_encodings_train)
        train_split_encoding_length_sum_and_encoding_index_pairs = list()
        for i in range(0, len(best_split_source_encodings_train)):
            train_split_encoding_length_sum_and_encoding_index_pairs.append(
                list([
                    best_split_source_encodings_train[i].shape[0] + best_split_target_encodings_train[i].shape[0],
                    np.abs(best_split_source_encodings_train[i].shape[0] - best_split_target_encodings_train[i].shape[0]),
                    i
                ])
            )
        train_split_encoding_length_sum_and_encoding_index_pairs = sorted(
            train_split_encoding_length_sum_and_encoding_index_pairs,
            key=lambda pair: (pair[0], pair[1])
        )
        train_source_encs_length_sorted = list()
        train_target_encs_length_sorted = list()
        for encoding_length_sum_and_encoding_index_pair in train_split_encoding_length_sum_and_encoding_index_pairs:
            train_source_encs_length_sorted.append(best_split_source_encodings_train[encoding_length_sum_and_encoding_index_pair[2]])
            train_target_encs_length_sorted.append(best_split_target_encodings_train[encoding_length_sum_and_encoding_index_pair[2]])
        best_split_source_encodings_test = best_split_source_encodings[train_size:]
        best_split_target_encodings_test = best_split_target_encodings[train_size:]
        assert len(best_split_source_encodings_test) == len(best_split_target_encodings_test)
        test_split_encoding_length_sum_and_encoding_index_pairs = list()
        for i in range(0, len(best_split_source_encodings_test)):
            test_split_encoding_length_sum_and_encoding_index_pairs.append(
                list([
                    best_split_source_encodings_test[i].shape[0] + best_split_target_encodings_test[i].shape[0],
                    np.abs(best_split_source_encodings_test[i].shape[0] - best_split_target_encodings_test[i].shape[0]),
                    i
                ])
            )
        test_split_encoding_length_sum_and_encoding_index_pairs = sorted(
            test_split_encoding_length_sum_and_encoding_index_pairs,
            key=lambda pair: (pair[0], pair[1])
        )
        test_source_encs_length_sorted = list()
        test_target_encs_length_sorted = list()
        for encoding_length_sum_and_encoding_index_pair in test_split_encoding_length_sum_and_encoding_index_pairs:
            test_source_encs_length_sorted.append(best_split_source_encodings_test[encoding_length_sum_and_encoding_index_pair[2]])
            test_target_encs_length_sorted.append(best_split_target_encodings_test[encoding_length_sum_and_encoding_index_pair[2]])
        dataset_holder.set_source_encodings(best_split_source_encodings)
        dataset_holder.set_target_encodings(best_split_target_encodings)
        dataset_holder.set_source_encodings_train(train_source_encs_length_sorted)
        dataset_holder.set_target_encodings_train(train_target_encs_length_sorted)
        dataset_holder.set_source_encodings_test(test_source_encs_length_sorted)
        dataset_holder.set_target_encodings_test(test_target_encs_length_sorted)
        return dataset_holder

    # use a dedicated padding token to pad batches as in Xue 2021 - ByT5 - Sec 3.1
    @staticmethod
    def prepare_batches(
            source_encodings,
            target_encodings,
            source_vocab,
            target_vocab,
            batch_size_limit: int,
            element_difference_limit: int,
            padding_value):
        assert len(source_encodings) == len(target_encodings)
        total_elements = len(source_encodings)
        source_encodings_batches = list()
        target_encodings_batches = list()
        source_encodings_tensors = list()
        target_encodings_tensors = list()
        encodings_index = 0
        while encodings_index < total_elements - 1:
            batch_size = 0
            batch_end_reached = False
            min_source_enc_len = source_encodings[encodings_index+batch_size].shape[0]
            max_source_enc_len = source_encodings[encodings_index+batch_size].shape[0]
            min_target_enc_len = target_encodings[encodings_index+batch_size].shape[0]
            max_target_enc_len = target_encodings[encodings_index+batch_size].shape[0]
            while not batch_end_reached:
                if (max(abs(source_encodings[encodings_index+batch_size].shape[0] - min_source_enc_len),
                        abs(source_encodings[encodings_index+batch_size].shape[0] - max_source_enc_len)) > element_difference_limit
                        or max(abs(target_encodings[encodings_index+batch_size].shape[0] - min_target_enc_len),
                               abs(target_encodings[encodings_index+batch_size].shape[0] - max_target_enc_len)) > element_difference_limit):
                    batch_end_reached = True
                if batch_size == batch_size_limit - 1:
                    batch_end_reached = True
                if encodings_index + batch_size + 1 < total_elements:
                    batch_size = batch_size + 1
                else:
                    batch_end_reached = True
            max_src_len_for_batch = 0
            max_tgt_len_for_batch = 0
            for batch_index in range(0, batch_size):
                if len(source_encodings[encodings_index+batch_index]) > max_src_len_for_batch:
                    max_src_len_for_batch = len(source_encodings[encodings_index+batch_index])
                if len(target_encodings[encodings_index+batch_index]) > max_tgt_len_for_batch:
                    max_tgt_len_for_batch = len(target_encodings[encodings_index+batch_index])
            for batch_index in range(0, batch_size):
                source_encoding = source_encodings[encodings_index]
                target_encoding = target_encodings[encodings_index]
                source_encodings_tensors.append(
                    torch.nn.functional.pad(
                        source_encoding,
                        (0, max_src_len_for_batch - len(source_encoding)),
                        value=source_vocab.index(padding_value)
                    )
                )
                target_encodings_tensors.append(
                    torch.nn.functional.pad(
                        target_encoding,
                        (0, max_tgt_len_for_batch - len(target_encoding)),
                        value=target_vocab.index(padding_value)
                    )
                )
                encodings_index = encodings_index + 1
            if batch_size > 0:
                source_batch = torch.stack(source_encodings_tensors)
                target_batch = torch.stack(target_encodings_tensors)
                source_encodings_batches.append(source_batch)
                target_encodings_batches.append(target_batch)
            source_encodings_tensors = list()
            target_encodings_tensors = list()
        target_encodings_batches_with_index = list()
        for i in range(0, len(target_encodings_batches)):
            target_encodings_batches_with_index.append(list([target_encodings_batches[i], i]))
        assert len(target_encodings_batches_with_index) == len(target_encodings_batches)
        target_encodings_batches_with_index_sorted = sorted(
            target_encodings_batches_with_index,
            key=lambda batch_pair: (-batch_pair[0].shape[0], -batch_pair[0].shape[1])
        )
        source_encodings_batches_sorted = list()
        target_encodings_batches_sorted = list()
        for i in range(0, len(target_encodings_batches_with_index_sorted)):
            source_encodings_batches_sorted.append(
                source_encodings_batches[target_encodings_batches_with_index_sorted[i][1]]
            )
            target_encodings_batches_sorted.append(
                target_encodings_batches[target_encodings_batches_with_index_sorted[i][1]]
            )
        del source_encodings_tensors
        del target_encodings_tensors
        del source_encodings_batches
        del target_encodings_batches
        del target_encodings_batches_with_index_sorted
        return source_encodings_batches_sorted, target_encodings_batches_sorted

    @staticmethod
    def prepare_training_batches(
            dataset_holder: DatasetHolder,
            batch_size_limit: int,
            element_difference_limit: int):
        source_encodings_batches, target_encodings_batches = DatasetUtils.prepare_batches(
            dataset_holder.get_source_encodings_train(),
            dataset_holder.get_target_encodings_train(),
            dataset_holder.get_source_vocab(),
            dataset_holder.get_target_vocab(),
            batch_size_limit,
            element_difference_limit,
            dataset_holder.get_padding_vocabulary_type()
        )

        source_vocab_counts = {}
        for source_encoding_batch in source_encodings_batches:
            for source_encoding in source_encoding_batch:
                for character in source_encoding:
                    if character.item() not in source_vocab_counts:
                        source_vocab_counts[character.item()] = 0
                    source_vocab_counts[character.item()] = source_vocab_counts[character.item()] + 1
        target_vocab_counts = {}
        for target_vocab_batch in target_encodings_batches:
            for target_encoding in target_vocab_batch:
                for character in target_encoding:
                    if character.item() not in target_vocab_counts:
                        target_vocab_counts[character.item()] = 0
                    target_vocab_counts[character.item()] = target_vocab_counts[character.item()] + 1
        dataset_holder.set_source_vocab_counts(source_vocab_counts)
        dataset_holder.set_target_vocab_counts(target_vocab_counts)
        return source_encodings_batches, target_encodings_batches

    @staticmethod
    def decode_target_tensor(dataset_holder: DatasetHolder, tensor_to_decode):
        vocab = dataset_holder.get_target_vocab_numpy()
        decoded_tensor = np.take(vocab, tensor_to_decode.detach().to(device="cpu").flatten().numpy())
        return "".join(decoded_tensor.tolist())

    @staticmethod
    def decode_source_tensor(dataset_holder: DatasetHolder, tensor_to_decode):
        vocab = dataset_holder.get_source_vocab_numpy()
        decoded_tensor = np.take(vocab, tensor_to_decode.detach().to(device="cpu").flatten().numpy())
        return "".join(decoded_tensor.tolist())


# class name matches file name
class transformer_vaswani2017(torch.nn.Transformer):

    def __init__(self,
                 model_hyperparameters):
        super().__init__(
            d_model=model_hyperparameters['d_model'],
            nhead=model_hyperparameters['nhead'],
            num_encoder_layers=model_hyperparameters['num_encoder_layers'],
            num_decoder_layers=model_hyperparameters['num_decoder_layers'],
            dim_feedforward=model_hyperparameters['dim_feedforward'],
            dropout=model_hyperparameters['dropout'],
            activation=model_hyperparameters['activation'],
            custom_encoder=model_hyperparameters['custom_encoder'],
            custom_decoder=model_hyperparameters['custom_decoder'],
            layer_norm_eps=model_hyperparameters['layer_norm_eps'],
            batch_first=model_hyperparameters['batch_first'],
            norm_first=model_hyperparameters['norm_first'],
            bias=model_hyperparameters['bias'],
            device=model_hyperparameters['device'],
            dtype=model_hyperparameters['dtype']
        )
        # add one for the end of sequence token
        self.max_src_seq_len = model_hyperparameters['max_src_seq_len'] + 1
        self.max_tgt_seq_len = model_hyperparameters['max_tgt_seq_len'] + 1
        self.src_embeddings = torch.nn.Embedding(
            model_hyperparameters['src_vocab_size'],
            model_hyperparameters['d_model']
        )
        self.tgt_embeddings = torch.nn.Embedding(
            model_hyperparameters['tgt_vocab_size'],
            model_hyperparameters['d_model']
        )
        self.src_pos_enc = torch.nn.Embedding(
            self.max_src_seq_len,
            model_hyperparameters['d_model']
        ).requires_grad_(False)
        self.tgt_pos_enc = torch.nn.Embedding(
            self.max_tgt_seq_len,
            model_hyperparameters['d_model']
        ).requires_grad_(False)
        self.linear_output_projection_1 = torch.nn.Linear(
            self.max_tgt_seq_len,
            1,
            bias=False
        )
        self.linear_output_projection_2 = torch.nn.Linear(
            model_hyperparameters['d_model'],
            model_hyperparameters['tgt_vocab_size'],
            bias=False
        )
        self.logsoftmax_output = torch.nn.LogSoftmax(dim=1)
        self.model_hyperparameters = model_hyperparameters
        self.tgt_mask_cache = {}
        for i in range(1, self.max_tgt_seq_len + 1):
            tgt_mask = self.generate_square_subsequent_mask(i)
            if is_remote_execution:
                self.tgt_mask_cache[i] = tgt_mask.to(device="cuda")
            self.tgt_mask_cache[i] = tgt_mask
        self.indices_cache = {}
        for i in range(1, max([self.max_src_seq_len, self.max_tgt_seq_len]) + 1):
            indices = torch.tensor(np.arange(0, i), dtype=torch.long)
            if is_remote_execution:
                indices = indices.to(device="cuda")
            self.indices_cache[i] = indices

    def forward(self,
                src: torch.Tensor,
                tgt: torch.Tensor,
                src_mask: Optional[torch.Tensor] = None,
                tgt_mask: Optional[torch.Tensor] = None,
                memory_mask: Optional[torch.Tensor] = None,
                src_key_padding_mask: Optional[torch.Tensor] = None,
                tgt_key_padding_mask: Optional[torch.Tensor] = None,
                memory_key_padding_mask: Optional[torch.Tensor] = None,
                src_is_causal: Optional[bool] = None,
                tgt_is_causal: Optional[bool] = True,
                memory_is_causal: bool = False) -> torch.Tensor:
        src_embedding_pos_enc = self.src_embeddings(src) + self.src_pos_enc(self.indices_cache[src.shape[1]])
        tgt_embedding_pos_enc = self.tgt_embeddings(tgt) + self.tgt_pos_enc(self.indices_cache[tgt.shape[1]])
        tgt_mask = self.tgt_mask_cache[tgt.shape[1]]
        transformer_output = super().forward(src_embedding_pos_enc, tgt_embedding_pos_enc, src_mask,
                                             tgt_mask, memory_mask, src_key_padding_mask,
                                             tgt_key_padding_mask, memory_key_padding_mask,
                                             src_is_causal, tgt_is_causal, memory_is_causal)
        transformer_output = torch.swapaxes(transformer_output, -1, -2)
        transformer_output = torch.nn.functional.pad(
            transformer_output,
            (0, self.max_tgt_seq_len - transformer_output.shape[2]),
            value=0
        )
        output = self.logsoftmax_output(
            self.linear_output_projection_2(
                torch.squeeze(
                    self.linear_output_projection_1(
                        transformer_output
                    ),
                    dim=2
                )
            )
        )
        del src_embedding_pos_enc
        del tgt_embedding_pos_enc
        del transformer_output
        return output


class model_trainer_kocmi2018():

    def __init__(self,
                 trainer_hyperparameters=None,
                 model_parameter_directory=None,
                 trainer_parameter_directory=None,
                 runner_hyperparameters_name=None,
                 latest_param_filename_tag=None):
        self.trainer_hyperparameters = trainer_hyperparameters
        self.optimizer_name = self.trainer_hyperparameters['optimizer_name']
        self.initial_lr = self.trainer_hyperparameters['initial_lr']
        self.exp_decay = self.trainer_hyperparameters['exp_decay']
        self.lr_scheduler_name = self.trainer_hyperparameters['lr_scheduler_name']
        self.epochs = self.trainer_hyperparameters['epochs']
        self.epoch_starting_index = self.trainer_hyperparameters['epoch_starting_index']
        self.batch_size_limit = self.trainer_hyperparameters['batch_size_limit']
        self.element_difference_limit = self.trainer_hyperparameters['element_difference_limit']
        self.batch_starting_index = self.trainer_hyperparameters['batch_starting_index']
        self.model_parameter_directory = model_parameter_directory
        self.trainer_parameter_directory = trainer_parameter_directory
        self.runner_hyperparameters_name = runner_hyperparameters_name
        self.latest_param_filename_tag = latest_param_filename_tag
        self.dataset_holder = None
        self.model = None
        self.source_encoding_batches = None
        self.target_encoding_batches = None
        self.optimizer = None
        self.lr_scheduler = None
        self.loss_fcn = None

    def init_trainer(self):
        self.source_encoding_batches, self.target_encoding_batches = (
            DatasetUtils.prepare_training_batches(
                self.dataset_holder,
                self.batch_size_limit,
                self.element_difference_limit
            )
        )
        # get_target_vocab_counts requires that training batches have been prepared
        # this ensures that vocab counts include padding and eos tokens
        loss_weights = list()
        for vocab_term in self.dataset_holder.get_target_vocab():
            loss_weights.append(
                1 / self.dataset_holder.get_target_vocab_counts()[
                    self.dataset_holder.get_target_vocab().index(vocab_term)
                ]
            )
        # set padding to have 0 weight
        loss_weights[
            self.dataset_holder.get_target_vocab().index(self.dataset_holder.get_padding_vocabulary_type())] = 0
        loss_weights = torch.tensor(loss_weights, dtype=torch.float)
        if is_remote_execution:
            torch.cuda.empty_cache()
            self.model.cuda()
            loss_weights = loss_weights.to(device="cuda")
        self.loss_fcn = torch.nn.NLLLoss(weight=loss_weights)
        _optimizer_class_ = Utils.load_python_object('torch.optim', self.optimizer_name)
        self.optimizer = _optimizer_class_(self.model.parameters(), lr=self.initial_lr)
        _lr_scheduler_class_ = Utils.load_python_object('torch.optim.lr_scheduler', self.lr_scheduler_name)
        # constructor call assumes that the scheduler is the ExponentialLR scheduler
        self.lr_scheduler = _lr_scheduler_class_(self.optimizer, self.exp_decay)
        scheduler_parameter_filepath = self.trainer_parameter_directory + "/" + self.runner_hyperparameters_name + "-" + self.latest_param_filename_tag + "-scheduler.params"
        if os.path.exists(scheduler_parameter_filepath):
            scheduler_parameters = torch.load(scheduler_parameter_filepath)
            self.lr_scheduler.load_state_dict(scheduler_parameters)
        parameter_count = 0
        bytes_consumed = 0
        for parameter in self.model.parameters():
            if parameter.requires_grad:
                parameter_count = parameter_count + np.prod(parameter.data.shape)
                bytes_consumed = bytes_consumed + parameter.data.nbytes
        gb_consumed = bytes_consumed / 1024 / 1024 / 1024
        print(f"Model trainer initialization complete."
              f"Trainer will run on model with parameter count {parameter_count} "
              f"and parameter memory use {gb_consumed} GB")

    # pretraining is not used for monolingual english as described in Xue 2021 - ByT5 - Sec 3.1
    def run_trainer(self):
        assert self.epoch_starting_index < self.epochs
        for i in range(self.epoch_starting_index, self.epochs):
            while self.lr_scheduler.state_dict()['last_epoch'] > i:
                print(f"Updating lr_scheduler: {self.lr_scheduler.state_dict()}")
                self.lr_scheduler.step()
            epoch_start = time.time()
            print(f"Beginning epoch {i+1} of {self.epochs} with scheduler {self.lr_scheduler.state_dict()}")
            # if i > 0:
            #     self.source_encoding_batches, self.target_encoding_batches = DatasetUtils.shuffle_lists(
            #         self.source_encoding_batches, self.target_encoding_batches
            #     )
            source_batches = None
            target_batches = None
            if is_remote_execution:
                source_batches = list()
                target_batches = list()
                for batch in self.source_encoding_batches:
                    source_batches.append(batch.to(device="cuda"))
                    del batch
                for batch in self.target_encoding_batches:
                    target_batches.append(batch.to(device="cuda"))
                    del batch
                torch.cuda.empty_cache()
            else:
                source_batches = self.source_encoding_batches
                target_batches = self.target_encoding_batches
            assert len(source_batches) == len(target_batches)
            batch_ct = len(source_batches)
            batch_size = source_batches[0].shape[0]
            samples_passed = 0
            last_log = 0
            last_loss = 0
            note_step_prediction = False
            step_prediction_at_percentage_of_sample = 0
            total_batch_time = 0
            assert self.batch_starting_index < batch_ct
            for j in range(self.batch_starting_index, batch_ct):
                batch_start = time.time()
                batch_sequence_length = target_batches[j].shape[1]
                step_prediction_step_number = int(batch_sequence_length * step_prediction_at_percentage_of_sample)
                print(f"Starting batch.")
                print(f"epoch:{i+1}/{self.epochs} batch:{j+1}/{batch_ct} batch_size:{target_batches[j].shape[0]}")
                for k in range(1, batch_sequence_length-1):
                    target_batch_slices = torch.tensor_split(target_batches[j], [k], dim=1)
                    self.model.zero_grad()
                    output_logits = self.model.forward(
                        source_batches[j],
                        target_batch_slices[0]
                    )
                    next_word_indices = target_batch_slices[1][:, 0]
                    last_loss = self.loss_fcn(output_logits, next_word_indices)
                    last_loss.backward()
                    self.optimizer.step()
                    if note_step_prediction and k == step_prediction_step_number:
                        note_step_prediction = False
                        full_sequence = DatasetUtils.decode_target_tensor(self.dataset_holder, target_batches[j][0])
                        prefix_sequence = DatasetUtils.decode_target_tensor(
                            self.dataset_holder,
                            target_batch_slices[0][0]
                        )
                        next_token = DatasetUtils.decode_target_tensor(
                            self.dataset_holder,
                            next_word_indices[0]
                        )
                        predicted_token = DatasetUtils.decode_target_tensor(
                            self.dataset_holder,
                            torch.argmax(output_logits[0])
                        )
                        print(f"Next token prediction. step:{k}/{batch_sequence_length} "
                              f"batch:{j+1}/{batch_ct} epoch:{i+1}/{self.epochs}")
                        print(f"full seq: {full_sequence}")
                        print(f"pref seq: {prefix_sequence}")
                        print(f"next tok: {next_token.rjust(k, ' ')}")
                        print(f"pred tok: {predicted_token.rjust(k, ' ')}")
                        del full_sequence
                        del prefix_sequence
                        del next_token
                        del predicted_token
                    del target_batch_slices
                    del output_logits
                    del next_word_indices
                    last_loss = last_loss.detach()
                    gc.collect()
                    if is_remote_execution:
                        torch.cuda.empty_cache()
                batch_end = time.time()
                batch_time = batch_end - batch_start
                total_batch_time = total_batch_time + batch_time
                print(f"Completed batch.")
                print(f"epoch:{i+1}/{self.epochs} batch:{j+1}/{batch_ct} batch_size:{target_batches[j].shape[0]} loss:{last_loss} "
                      f"time_for_batch_instance:{batch_time} total_batch_time:{total_batch_time} running_batch_average:{total_batch_time/(j+1)}")
                samples_passed = samples_passed + batch_size
                if samples_passed - last_log > 100:
                    last_log = samples_passed
                    note_step_prediction = True
                    step_prediction_at_percentage_of_sample = random.random()
                    if is_remote_execution:
                        print(f"Memory usage summary:")
                        print(f"{torch.cuda.memory_summary()}")
                        torch.cuda.reset_max_memory_allocated()
                        torch.cuda.reset_max_memory_cached()
                        torch.cuda.reset_peak_memory_stats()
                    param_filename_tag = str(int(time.time()))
                    torch.save(
                        self.model.state_dict(),
                        self.model_parameter_directory + "/" + self.runner_hyperparameters_name + "-" + param_filename_tag + "-model.params"
                    )
                    torch.save(
                        self.lr_scheduler.state_dict(),
                        self.trainer_parameter_directory + "/" + self.runner_hyperparameters_name + "-" + param_filename_tag + "-scheduler.params"
                    )
                    torch.save(
                        f"epoch:{i+1}/{self.epochs} batch:{j+1}/{batch_ct}",
                        self.trainer_parameter_directory + "/" + self.runner_hyperparameters_name + "-" + param_filename_tag + "-trainer.params"
                    )
            del source_batches
            del target_batches
            gc.collect()
            if is_remote_execution:
                torch.cuda.empty_cache()
            self.lr_scheduler.step()
            epoch_end = time.time()
            print(f"Completed epoch {i+1}/{self.epochs} in {(epoch_end - epoch_start) / 60 }m")
            print(f"epoch:{i+1}, batch:{j+1}/{batch_ct}, loss:{last_loss}")

    def get_dataset_holder(self):
        return self.dataset_holder

    def set_dataset_holder(self, dataset_holder):
        self.dataset_holder = dataset_holder

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model


class Runner:

    def __init__(self,
                 model_parameter_directory=root_filepath+"resources/model_parameters",
                 trainer_parameter_directory=root_filepath+"resources/trainer_parameters",
                 runner_hyperparameters_name="SETimesByT5Vaswani2017Kocmi2018_0"):
        self.model_parameter_directory = model_parameter_directory
        self.trainer_parameter_directory = trainer_parameter_directory
        self.runner_hyperparameters_name = runner_hyperparameters_name
        self.runner_hyperparameters = SETimesByT5Vaswani2017Kocmi2018_0
        self.dataset_holder: DatasetHolder = None
        self.model = None
        self.trainer = None
        self.latest_param_filename_tag = None
        if 'latest_param_filename_tag' in self.runner_hyperparameters:
            self.latest_param_filename_tag = self.runner_hyperparameters['latest_param_filename_tag']
        print(f"Initialized runner {runner_hyperparameters_name} with parameters {self.runner_hyperparameters}")

    def load_dataset(self):
        dataset_transformer_name = self.runner_hyperparameters.get('dataset_transformer_name')
        dataset_hyperparameters = self.runner_hyperparameters.get('dataset_transformer_hyperparameters')
        dataset_transformer = dataset_transformer_setimesbyt5(dataset_hyperparameters=dataset_hyperparameters)
        self.dataset_holder = dataset_transformer.read_dataset()

    def load_model(self):
        model_hyperparameters = self.runner_hyperparameters.get('model_hyperparameters')
        model_hyperparameters['src_vocab_size'] = len(self.dataset_holder.get_source_vocab())
        model_hyperparameters['tgt_vocab_size'] = len(self.dataset_holder.get_target_vocab())
        model_hyperparameters['max_src_seq_len'] = self.dataset_holder.get_max_src_seq_obs()
        model_hyperparameters['max_tgt_seq_len'] = self.dataset_holder.get_max_tgt_seq_obs()
        model_parameter_filepath = self.model_parameter_directory + "/" + self.runner_hyperparameters_name + "-" + self.latest_param_filename_tag + "-model.params"
        self.model = transformer_vaswani2017(model_hyperparameters=model_hyperparameters)
        if os.path.exists(model_parameter_filepath):
            model_parameters = torch.load(model_parameter_filepath)
            self.model.load_state_dict(model_parameters)

    def load_trainer(self):
        trainer_hyperparameters = self.runner_hyperparameters.get('trainer_hyperparameters')
        self.trainer = model_trainer_kocmi2018(
            trainer_hyperparameters=trainer_hyperparameters,
            model_parameter_directory=self.model_parameter_directory,
            trainer_parameter_directory=self.trainer_parameter_directory,
            runner_hyperparameters_name=self.runner_hyperparameters_name,
            latest_param_filename_tag=self.latest_param_filename_tag
        )

    def run_trainer(self):
        self.trainer.set_dataset_holder(self.dataset_holder)
        self.trainer.set_model(self.model)
        self.trainer.init_trainer()
        self.trainer.run_trainer()


runner = Runner(runner_hyperparameters_name="SETimesByT5Vaswani2017Kocmi2018_2")

runner.load_dataset()
runner.load_model()
runner.load_trainer()
runner.run_trainer()
