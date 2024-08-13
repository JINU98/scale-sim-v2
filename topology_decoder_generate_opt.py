import pandas as pd

context_length = [128, 256, 512, 1024, 2048, 4096]
opt_model_configs = {
    "1-opt-125m": {"emb_dim": 768, "n_layers": 12, "n_heads": 12},
    "2-opt-350m": {"emb_dim": 1024, "n_layers": 24, "n_heads": 16},
    "3-opt-1b3m": {"emb_dim": 2048, "n_layers": 24, "n_heads": 32},
    "4-opt-2b7m": {"emb_dim": 2560, "n_layers": 32, "n_heads": 32},
    "5-opt-6b7m": {"emb_dim": 4096, "n_layers": 32, "n_heads": 32},
    "6-opt-13b": {"emb_dim": 5120, "n_layers": 40, "n_heads": 40},
    "7-opt-30b": {"emb_dim": 7168, "n_layers": 48, "n_heads": 56},
    "8-opt-66b": {"emb_dim": 9216, "n_layers": 64, "n_heads": 72},
    "9-opt-175b": {"emb_dim": 12288, "n_layers": 96, "n_heads": 96},

}

for key, value in opt_model_configs.items():
    for j in context_length:
        data = [
            ['Q', 1, value['emb_dim'], value['emb_dim']],
            ['K', 1, value['emb_dim'], value['emb_dim']],
            ['V', 1, value['emb_dim'], value['emb_dim']],
            ['Attention_score', 1, j, value['emb_dim'] // value['n_heads']],
            ['Attention_output', 1, value['emb_dim'] // value['n_heads'], j],
            ['Add_norm', 1, value['emb_dim'], value['emb_dim']],
            ['FFN_in', 1, value['emb_dim'], value['emb_dim'] * 4],  # OPT uses 4x embedding dim for FFN
            ['FFN_out', 1, value['emb_dim'] * 4, value['emb_dim']]
        ]
        
        pd.DataFrame(data, columns=['Layer Name', 'M', 'N', 'K']).astype({
            'Layer Name': 'object',
            'M': 'int32',
            'N': 'int32',
            'K': 'int32'
        }).to_csv(f"{key}_{value['emb_dim']}_{value['n_heads']}_{j}.csv", index=False)
