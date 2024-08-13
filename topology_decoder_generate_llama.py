import pandas as pd

context_length = [128,256,512,1024,2048,4096]
llama_model_configs = {
    "1-llama-7b": {"emb_dim": 4096, "n_layers": 32, "n_heads": 32, "ffn_dim": 11008},
    "2-llama-13b": {"emb_dim": 5120, "n_layers": 40, "n_heads": 40, "ffn_dim": 13824},
}

for key, value in llama_model_configs.items():
    for j in context_length:
        data = [
            ['Q', 1, value['emb_dim'], value['emb_dim']],
            ['K', 1, value['emb_dim'], value['emb_dim']],
            ['V', 1, value['emb_dim'], value['emb_dim']],
            ['Attention_score', 1, j, value['emb_dim'] // value['n_heads']],
            ['Attention_output', 1, value['emb_dim'] // value['n_heads'], j],
            ['Add_norm', 1, value['emb_dim'], value['emb_dim']],
            ['FFN_in', 1, value['emb_dim'], value['ffn_dim']],
            ['FFN_out', 1, value['ffn_dim'], value['emb_dim']]
        ]
        
        pd.DataFrame(data, columns=['Layer Name', 'M', 'N', 'K']).astype({
            'Layer Name': 'object',
            'M': 'int32',
            'N': 'int32',
            'K': 'int32'
        }).to_csv(f"{key}_{value['emb_dim']}_{value['n_heads']}_{j}.csv", index=False)
