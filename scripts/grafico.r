library(ggplot2)
library(tidyr)

# 1. Leitura e transformação (igual ao anterior)
dados <- read.csv("dados_limpos.csv", sep = ";", dec = ".")
dados_long <- pivot_longer(dados, cols = c(NDVI, NDWI, BSI), 
                           names_to = "Indice", values_to = "Valor")

# 2. Criação do Gráfico em Painéis (Facets)
grafico_paineis <- ggplot(dados_long, aes(x = Ano, y = Valor, group = Indice)) +
  geom_line(linewidth = 0.8, color = "black") +  
  geom_point(size = 3, color = "black") +              
  scale_x_continuous(breaks = min(dados$Ano):max(dados$Ano)) +
  
  # AQUI ESTÁ O SEGREDO: Separa os gráficos e deixa o eixo Y livre para cada um
  facet_wrap(~ Indice, scales = "free_y", ncol = 1) + 
  
  labs(x = "Ano", y = "Valor do Índice") +
  theme_bw() + # Tema com bordas, excelente para painéis em artigos
  theme(
    text = element_text(family = "serif", size = 12, color = "black"),
    axis.text = element_text(color = "black"),
    strip.background = element_rect(fill = "white", color = "black"), # Fundo do título do painel
    strip.text = element_text(face = "bold", size = 12) # Texto do título do painel
  )

# Exibe
print(grafico_paineis)

# Salva em alta resolução
ggsave("grafico_indices_paineis.tiff", plot = grafico_paineis, 
       width = 16, height = 18, units = "cm", dpi = 300, compression = "lzw")