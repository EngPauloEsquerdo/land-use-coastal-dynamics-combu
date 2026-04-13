import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------
# 1. DADOS (RECRIADOS AQUI PARA NÃO DEPENDER DE CSV)
# ------------------------------------------------------------
data = {
    'ANO': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023] * 3,
    'NDVI': [0.764, 0.787, 0.795, 0.779, 0.760, 0.773, 0.748, 0.756,
             0.785, 0.808, 0.812, 0.798, 0.790, 0.803, 0.773, 0.790,
             0.752, 0.779, 0.782, 0.786, 0.755, 0.767, 0.739, 0.735],
    'NDWI': [-0.700, -0.718, -0.726, -0.712, -0.691, -0.704, -0.675, -0.682,
             -0.717, -0.735, -0.742, -0.726, -0.716, -0.728, -0.697, -0.713,
             -0.692, -0.712, -0.718, -0.719, -0.688, -0.698, -0.669, -0.667],
    'BSI': [-0.344, -0.352, -0.343, -0.338, -0.327, -0.336, -0.328, -0.339,
            -0.354, -0.362, -0.351, -0.351, -0.349, -0.350, -0.341, -0.359,
            -0.340, -0.353, -0.344, -0.352, -0.337, -0.336, -0.328, -0.320],
    'Local': ['IGARAPÉ COMBU']*8 + ['IGARAPÉ PIRIQUITAQUARA']*8 + ['ILHA COMBU']*8
}
df = pd.DataFrame(data)

# ------------------------------------------------------------
# 2. CONFIGURAÇÃO VISUAL (REVISTA)
# ------------------------------------------------------------
plt.style.use('default')
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'axes.facecolor': 'white',
    'figure.facecolor': 'white',
    'axes.edgecolor': 'black',
    'axes.linewidth': 0.8,
    'xtick.direction': 'in',
    'ytick.direction': 'in'
})

cores = {
    'IGARAPÉ COMBU': '#1b9e77',
    'IGARAPÉ PIRIQUITAQUARA': '#d95f02',
    'ILHA COMBU': '#7570b3'
}

# ------------------------------------------------------------
# 3. CRIAÇÃO DO GRÁFICO
# ------------------------------------------------------------
fig, axes = plt.subplots(3, 1, figsize=(7, 8.5))  # altura extra para legenda

indices = ['NDVI', 'NDWI', 'BSI']
titulos = ['(a) Índice de Vegetação (NDVI)', 
           '(b) Índice de Umidade (NDWI)', 
           '(c) Índice de Solo Exposto (BSI)']
ylabels = ['NDVI', 'NDWI', 'BSI']

handles_legenda = []
labels_legenda = []

for i, (idx, titulo, ylab) in enumerate(zip(indices, titulos, ylabels)):
    ax = axes[i]
    for local in df['Local'].unique():
        dados = df[df['Local'] == local]
        linha = ax.plot(dados['ANO'], dados[idx],
                        marker='o', linestyle='-', 
                        linewidth=1.2, markersize=4.5,
                        color=cores[local], 
                        label=local.title().replace('Igarape', 'Igarapé').replace('Ilha', 'Ilha'))
        if i == 0:
            handles_legenda.extend(linha)
            labels_legenda.append(local.title().replace('Igarape', 'Igarapé').replace('Ilha', 'Ilha'))
    
    # Linha vertical tracejada em 2022 (anomalia)
    ax.axvline(x=2022, color='red', linestyle='--', linewidth=1.0, alpha=0.7)
    
    ax.set_ylabel(ylab)
    ax.set_title(titulo, loc='left', fontweight='bold')
    ax.grid(True, axis='y', linestyle='-', linewidth=0.5, alpha=0.3, color='gray')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Adicionar elemento da anomalia à legenda
from matplotlib.lines import Line2D
elemento_anomalia = Line2D([0], [0], color='red', linestyle='--', linewidth=1.0, label='Anomalia (2022)')
handles_legenda.append(elemento_anomalia)
labels_legenda.append('Anomalia (2022)')

# Eixo X comum
axes[-1].set_xlabel('Ano')
axes[-1].set_xticks(sorted(df['ANO'].unique()))
axes[-1].set_xlim(2015.5, 2023.5)

# ------------------------------------------------------------
# 4. AJUSTE DE LAYOUT E LEGENDA PRÓXIMA
# ------------------------------------------------------------
plt.tight_layout(rect=[0, 0.05, 1, 1])  # reserva espaço inferior
plt.subplots_adjust(bottom=0.08)        # margem inferior controlada

# Legenda centralizada logo abaixo do eixo "Ano"
fig.legend(handles=handles_legenda, labels=labels_legenda,
           loc='upper center',          # âncora no centro superior da legenda
           bbox_to_anchor=(0.5, 0.0), # (x, y) -> y negativo = abaixo do eixo
           ncol=4, 
           frameon=False, 
           fontsize=10)

# ------------------------------------------------------------
# 5. SALVAR (SVG E PNG)
# ------------------------------------------------------------
plt.savefig('Figura_Combu_Final_Proxima.svg', bbox_inches='tight')
plt.savefig('Figura_Combu_Final_Proxima.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Gráfico salvo com legenda próxima ao eixo 'Ano'.")