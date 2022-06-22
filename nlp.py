from fastai.text.all import *
import pandas as pd
import pickle
from pathlib import Path

import torch

defaults.device = torch.device('cpu')

ROOT_PATH = Path('./')


def predict(text, n_words, temperature=0.5, only_last_word=True, no_unk=True,
            min_p=None, no_bar=False):
    awd_lstm_lm_config_old = dict(emb_sz=400, n_hid=1150, n_layers=3, pad_token=1, bidir=False, output_p=0.1,
                                  hidden_p=0.15, input_p=0.25, embed_p=0.02, weight_p=0.2, tie_weights=True,
                                  out_bias=True)

    test_df = pd.DataFrame({'text': ['у меня встал вопрос'] * 100})
    with open(ROOT_PATH / 'models' / 'max_bot_lm_vocab.pkl', 'rb') as f:
        vocab = pickle.load(f)
    test_data = TextDataLoaders.from_df(test_df, text_vocab=vocab, is_lm=True, seed=42, valid_pcd=0.25)
    learn = language_model_learner(test_data, arch=AWD_LSTM,
                                   config=awd_lstm_lm_config_old,
                                   pretrained=False,
                                   pretrained_fnames=('max_bot_tuned', 'max_bot_lm_vocab'),
                                   path=ROOT_PATH)

    return learn.predict(text, n_words, temperature=temperature, only_last_word=only_last_word, no_unk=no_unk,
                         min_p=min_p, no_bar=no_bar)
