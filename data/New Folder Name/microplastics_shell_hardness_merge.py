import pandas as pd

# --- Load data ---
mp = pd.read_csv("Marine_Microplastics__1995-2021_.csv")
lb = pd.read_csv("Lobster_Data__2004-2015_.csv")

# --- Microplastics: parse date, extract year, filter ocean water only ---
mp['Sample Date'] = pd.to_datetime(mp['Sample Date'], errors='coerce')
mp['Year'] = mp['Sample Date'].dt.year
mp_ow = mp[mp['Marine Setting'] == 'Ocean water'].copy()

# --- Annual mean microplastic concentration ---
mp_annual = mp_ow.groupby('Year')['Microplastics Measurement'].mean().reset_index()
mp_annual.columns = ['Year', 'mean_microplastic_conc_pieces_m3']

# --- Annual mean shell hardness ---
lb_annual = lb.groupby('Year')['Shellhardness'].mean().reset_index()
lb_annual.columns = ['Year', 'mean_shell_hardness']

# --- Merge on overlapping years only (inner join) ---
merged = pd.merge(mp_annual, lb_annual, on='Year').round(4)

print(merged)
print(f"\nShape: {merged.shape}")
print(f"Overlapping years: {merged['Year'].tolist()}")

# --- Save ---
merged.to_csv("microplastics_shell_hardness_overlapping_years.csv", index=False)
print("\nSaved to microplastics_shell_hardness_overlapping_years.csv")
