import pandas as pd
context_length = [128,256,512,1024,2048,4096]
model_configs = {
    "gpt2-small_(124M)": {"emb_dim": 768, "n_layers": 12, "n_heads": 12},
    "gpt2-medium_(355M)": {"emb_dim": 1024, "n_layers": 24, "n_heads": 16},
    "gpt2-large_(774M)": {"emb_dim": 1280, "n_layers": 36, "n_heads": 20},
    "gpt2-xl_(1558M)": {"emb_dim": 1600, "n_layers": 48, "n_heads": 25},
}

for key,value in model_configs.items():
  for j in context_length:
    
    data = [['Q', 1, value['emb_dim'],value['emb_dim']],
            ['K', 1, value['emb_dim'],value['emb_dim']],
            ['V', 1, value['emb_dim'],value['emb_dim']],
            ['Attention_score',1,j,value['emb_dim']/value['n_heads']],
            ['Attention_output',1,value['emb_dim']/value['n_heads'],j],
            ['Add_norm',1,value['emb_dim'],value['emb_dim']],
            ['Dense_in',1,value['emb_dim'],value['emb_dim']],
            ['Dense_out',1,value['emb_dim'],value['emb_dim']]]
    
    pd.DataFrame(data, columns=['Layer Name','M','N','K']).astype({
            'Layer Name': 'object',
            'M': 'int32',
            'N': 'int32',
            'K': 'int32'
        }).to_csv(key+'_'+str(j)+'.csv',index=False)
    