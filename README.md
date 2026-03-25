# BC3412 — Business Analytics Consulting
 
**Analysing the Impact of Microplastics on North Atlantic Shellfish**
 
A group project investigating whether microplastic concentrations affect lobster shell hardness, oyster histopathology, and overall water quality across the North Atlantic region (1995–2015).
 
---

### Option A — Jupyter Notebook (Local)

Save `.ipynb` files in the `notebooks/` folder.
 
### Option B — Google Colab (Cloud)

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click **File → Open notebook → GitHub**
3. Paste the repo URL: `https://github.com/dhairya-p/bc3412-code`
4. Select the notebook you want to open
 
**Loading data in Colab** — clone datasets into your Colab runtime:
 
```python
!git clone https://github.com/dhairya-p/bc3412-code.git
import pandas as pd
 
lobster = pd.read_csv("bc3412-code/data/Lobster Shell Hardness/Lobster_Data (2004-2015).csv")
microplastics = pd.read_csv("bc3412-code/data/Microplastics Concentration/Marine_Microplastics (1995-2002).csv")
oyster = pd.read_csv("bc3412-code/data/Oyster DTA/Oyster_Histopath (1995-2010).csv")
...
```
 
