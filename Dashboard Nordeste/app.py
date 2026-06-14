import streamlit as st
import pandas as pd
import os
from PIL import Image

# Configuração da página
st.set_page_config(
    page_title="Dashboard Região Nordeste",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS customizado para aparência premium
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Cores de fundo e cartões */
    .metric-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
        border-color: #d97706;
    }
    
    .metric-title {
        font-size: 0.875rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 2.25rem;
        color: #1e293b;
        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 8px;
    }
    .metric-desc {
        font-size: 0.875rem;
        color: #475569;
    }
    
    /* Header do Dashboard */
    .dashboard-header {
        background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
        padding: 40px;
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 10px 15px -3px rgba(217, 119, 6, 0.2);
    }
    .dashboard-header h1 {
        color: white !important;
        margin: 0;
        font-weight: 700;
        font-size: 2.5rem;
    }
    .dashboard-header p {
        margin-top: 10px;
        margin-bottom: 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Seções de Texto */
    .section-title {
        color: #1e293b;
        font-weight: 700;
        font-size: 1.5rem;
        margin-top: 25px;
        margin-bottom: 15px;
        border-bottom: 2px solid #f1f5f9;
        padding-bottom: 8px;
    }
    
    .info-box {
        background-color: #fffbeb;
        border-left: 4px solid #d97706;
        border-radius: 8px;
        padding: 16px;
        margin: 15px 0;
        color: #451a03;
    }
    
    .highlight-card {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border: 1px solid #fcd34d;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        color: #78350f;
    }
</style>
""", unsafe_allow_html=True)

# Função para carregar imagem com fallback seguro
def load_image(filename):
    path = os.path.join("assets", filename)
    if os.path.exists(path):
        return Image.open(path)
    else:
        st.warning(f"Imagem {filename} não encontrada em assets/.")
        return None

# Header principal
st.markdown("""
<div class="dashboard-header">
    <h1>Análise Multidimensional da Região Nordeste</h1>
    <p>Estrutura territorial, demografia, economia regional e aplicação do modelo de Von Thünen</p>
</div>
""", unsafe_allow_html=True)

# Definição das Tabs
tab_visao, tab_demo, tab_economia, tab_thunen = st.tabs([
    "📍 Visão Geral", 
    "👥 Demografia", 
    "🌾 Economia e Biomas", 
    "⭕ Modelo de Von Thünen"
])

# ==========================================
# TAB 1: VISÃO GERAL
# ==========================================
with tab_visao:
    st.markdown('<div class="section-title">Estrutura Territorial e Capitais Produtivas</div>', unsafe_allow_html=True)
    
    col_intro, col_map = st.columns([1, 1])
    
    with col_intro:
        st.write("""
        A Região Nordeste do Brasil é composta por **9 estados (unidades federativas)** que cobrem uma vasta área territorial com características ecológicas, econômicas e sociais bastante diversas. 
        Ao todo, a região conta com **1.794 municípios**, representando cerca de **32,2% do total nacional** (IBGE, 2000), o que a torna a região brasileira com a maior quantidade de municípios.
        """)
        
        st.write("""
        Historicamente, a maior parte dos estados surgiu através das Capitanias Hereditárias em 1534, evoluindo para unidades da federação com a Proclamação da República em 1889. Abaixo, são apresentadas as datas de fundação oficial de cada estado ordenadas cronologicamente:
        """)
        
        # DataFrame com dados estruturados da Tabela 1
        df_estados = pd.DataFrame({
            "Estado": ["Rio Grande do Norte (RN)", "Pernambuco (PE)", "Bahia (BA)", "Paraíba (PB)", "Maranhão (MA)", "Ceará (CE)", "Alagoas (AL)", "Sergipe (SE)", "Piauí (PI)"],
            "Fundação Oficial": ["07/08/1501", "10/03/1534", "01/01/1549", "05/08/1585", "13/06/1621", "17/01/1799", "16/09/1817", "08/07/1820", "24/01/1823"]
        })
        st.dataframe(df_estados, hide_index=True, use_container_width=True)

    with col_map:
        st.markdown("**Mapa Político: Unidades Federativas e Municípios do Nordeste**")
        img_mun = load_image("mapa_municipios.png")
        if img_mun:
            st.image(img_mun, use_column_width=True)
            
    st.markdown('<div class="section-title">Três Maiores Capitais na Production Corrente</div>', unsafe_allow_html=True)
    col_cap1, col_cap2, col_cap3 = st.columns(3)
    
    with col_cap1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Fortaleza • CE</div>
            <div class="metric-value">Fortaleza</div>
            <div class="metric-desc">
                Um dos principais polos comerciais do Nordeste. Destaca-se pelo dinamismo no setor de serviços, turismo, construção civil e indústrias de bens de consumo (têxtil, vestuário e calçados).
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_cap2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Salvador • BA</div>
            <div class="metric-value">Salvador</div>
            <div class="metric-desc">
                Historicamente um dos maiores polos econômicos da região. Centro administrativo, turístico e cultural de grande relevância, com conexões industriais fortes no recôncavo baiano.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_cap3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Recife • PE</div>
            <div class="metric-value">Recife</div>
            <div class="metric-desc">
                Grande força econômica focada em serviços especializados, abrigando o maior polo médico do Norte-Nordeste, além de um robusto ecossistema de TI (Porto Digital) e o Porto de Suape.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Contraste Socioeconômico do Nordeste</div>', unsafe_allow_html=True)
    
    col_text_pib, col_map_pib = st.columns([1, 1])
    
    with col_text_pib:
        st.markdown("""
        <div class="highlight-card">
            <h4>Pobreza vs Riqueza Municipal</h4>
            <p style="font-size: 1.1rem; margin-top: 10px;">
                <b>94% dos municípios</b> do Nordeste acumulam um Produto Interno Bruto (PIB) anual de <b>menos de 2 bilhões de reais</b>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.write("""
        Esse dado evidencia a enorme desigualdade e a concentração da riqueza em torno das regiões metropolitanas e polos industriais específicos. O mapa ao lado ilustra esse contraste de forma direta:
        
        * **Municípios em Roxo**: Municípios considerados mais pobres, com PIB anual **inferior a 2 bilhões de reais**. Eles constituem a quase totalidade da região no interior.
        * **Municípios em Branco**: Municípios com PIB **entre 2 bilhões e 30 bilhões de reais**, destacando as capitais estaduais e polos específicos do agronegócio ou indústria (como Petrolina, Juazeiro e Luís Eduardo Magalhães).
        """)
        
        st.markdown("""
        <div class="info-box">
            <strong>Diferencial Censitário (2010 vs 2022):</strong><br>
            O censo demográfico de 2022 trouxe um avanço metodológico fundamental: o mapeamento completo e específico das comunidades quilombolas e indígenas em todo o Nordeste, permitindo identificar vulnerabilidades dessas populações tradicionais.
        </div>
        """, unsafe_allow_html=True)

    with col_map_pib:
        st.markdown("**Mapa de Contraste: Municípios Ricos versus Pobres**")
        img_pib = load_image("mapa_contraste_pib.png")
        if img_pib:
            st.image(img_pib, use_column_width=True)

# ==========================================
# TAB 2: DEMOGRAFIA
# ==========================================
with tab_demo:
    st.markdown('<div class="section-title">Aspectos Demográficos e Dinâmica Populacional</div>', unsafe_allow_html=True)
    
    col_demo_metric, col_demo_text = st.columns([1, 2])
    
    with col_demo_metric:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: white; border: none;">
            <div class="metric-title" style="color: #cbd5e1;">Presença Rural no Brasil</div>
            <div class="metric-value" style="color: #fbbf24; font-size: 3.5rem;">48%</div>
            <div class="metric-desc" style="color: #94a3b8; font-size: 1rem;">
                De toda a população rural do território brasileiro reside na região Nordeste (IBGE, 2022).
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_demo_text:
        st.write("""
        Embora a população total do Nordeste apresente uma concentração urbana superior à rural, a região ainda mantém um perfil marcadamente interiorizado se comparada ao Sudeste. 
        Este contingente rural expressivo está exposto a dinâmicas migratórias e etárias peculiares:
        
        * **Ciclo Migratório de Jovens**: Ocorre um fluxo contínuo de jovens em direção aos grandes centros urbanos em busca de melhores oportunidades de estudo e trabalho. O estado do **Maranhão** é um exemplo clássico, concentrando a maior proporção de jovens entre 10 e 14 anos (cerca de 12,2% de sua população total).
        * **Assentamento da População Idosa**: Em contraste, as regiões mais áridas do interior (o Sertão e o Agreste) mostram um assentamento concentrado da população mais idosa (faixa de 65 a 69 anos). Os estados da Paraíba, Rio Grande do Norte, Ceará, além do centro-sul do Piauí e a região central da Bahia, apresentam maiores proporções de idosos residindo em áreas rurais ou pequenos municípios.
        * **Desafios Estruturais**: Este contraste etário cria pressões significativas para as finanças públicas locais devido à redução da População Economicamente Ativa (PEA) no interior, gerando menor arrecadação tributária local e demandando políticas específicas de suporte social e desenvolvimento.
        """)

    st.markdown('<div class="section-title">Análise Espacial: Etnias e Faixas Etárias</div>', unsafe_allow_html=True)
    
    map_type = st.radio("Selecione a categoria de análise populacional:", ["Distribuição Étnica", "Distribuição por Faixas Etárias"], horizontal=True)
    
    if map_type == "Distribuição Étnica":
        col_etnia_txt, col_etnia_map = st.columns([1, 1])
        
        with col_etnia_txt:
            etnia = st.selectbox("Escolha a Etnia para visualizar no mapa:", ["Parda (Majoritária)", "Branca", "Preta"])
            
            if etnia == "Branca":
                st.markdown("### Proporção da População Branca")
                st.write("""
                A maior concentração de população de etnia branca (tons de verde mais escuros) é registrada principalmente na **Paraíba, em partes de Pernambuco, na faixa litorânea e interior do Rio Grande do Norte, leste do Ceará** e em regiões específicas de **Alagoas**.
                """)
                img_white = load_image("mapa_etnia_branca.png")
                if img_white:
                    st.session_state["etnia_img"] = img_white
            
            elif etnia == "Parda (Majoritária)":
                st.markdown("### Proporção da População Parda")
                st.write("""
                A população parda representa a **maior parte étnica presente no Nordeste**. O mapa revela a raridade de se encontrar municípios onde os pardos representem menos de 30% da população total. Em quase toda a extensão territorial, a etnia parda é amplamente predominante (destacada em tons de azul escuro).
                """)
                img_brown = load_image("mapa_etnia_parda.png")
                if img_brown:
                    st.session_state["etnia_img"] = img_brown
                    
            elif etnia == "Preta":
                st.markdown("### Proporção da População Preta")
                st.write("""
                A maioria dos municípios apresenta uma proporção de população preta na faixa de **17% a 25%**. 
                Os estados da **Bahia** e do **Maranhão** despontam com a maior concentração de pessoas que se autodeclaram pretas no Nordeste (representados pelas cores cinza mais escuras no mapa).
                """)
                img_black = load_image("mapa_etnia_preta.png")
                if img_black:
                    st.session_state["etnia_img"] = img_black
                    
        with col_etnia_map:
            st.markdown(f"**Mapa de Distribuição Étnica: {etnia}**")
            if "etnia_img" in st.session_state and st.session_state["etnia_img"]:
                st.image(st.session_state["etnia_img"], use_column_width=True)
            else:
                img_default = load_image("mapa_etnia_parda.png")
                if img_default:
                    st.image(img_default, use_column_width=True)
                    
    else:  # Distribuição por Faixas Etárias
        col_idade_txt, col_idade_map = st.columns([1, 1])
        
        with col_idade_txt:
            idade_faixa = st.selectbox("Escolha a Faixa Etária:", ["10 a 14 anos (Jovens)", "35 a 39 anos (Adultos)", "65 a 69 anos (Idosos)"])
            
            if idade_faixa == "10 a 14 anos (Jovens)":
                st.markdown("### Concentração de Jovens (10 a 14 anos)")
                st.write("""
                Os jovens nesta faixa etária estão distribuídos de maneira mais expressiva na **região oeste e norte do Nordeste**. 
                O **Maranhão** se destaca como o estado com a maior concentração de jovens nessa idade no país, representando cerca de **12,2%** de toda a população do estado.
                """)
                img_age_young = load_image("mapa_idade_10_14.png")
                if img_age_young:
                    st.session_state["age_img"] = img_age_young
                    
            elif idade_faixa == "35 a 39 anos (Adultos)":
                st.markdown("### População em Plena Idade Produtiva (35 a 39 anos)")
                st.write("""
                Esta população apresenta maior densidade (tons de vermelho) ao longo de toda a **faixa leste da região** (Rio Grande do Norte, Paraíba, Pernambuco, Alagoas, Sergipe) e também no **leste/sul da Bahia**. 
                No extremo oeste da Bahia, destaca-se o município de **Luís Eduardo Magalhães**, que atrai muitos trabalhadores nesta faixa etária devido à forte geração de empregos pelo agronegócio de grãos.
                """)
                img_age_mid = load_image("mapa_idade_35_39.png")
                if img_age_mid:
                    st.session_state["age_img"] = img_age_mid
                    
            elif idade_faixa == "65 a 69 anos (Idosos)":
                st.markdown("### População no Início da Terceira Idade (65 a 69 anos)")
                st.write("""
                Os idosos estão mais concentrados (tons amarelados) no interior semiárido, abrangendo o **Sertão e o Agreste** da **Paraíba, Rio Grande do Norte, Ceará, centro-sul do Piauí e região central da Bahia**. 
                Em contraste, o estado do Maranhão apresenta baixos índices de envelhecimento populacional nesta área. Isto evidencia o efeito do ciclo de migração de jovens que esvazia economicamente o interior do Nordeste.
                """)
                img_age_old = load_image("mapa_idade_65_69.png")
                if img_age_old:
                    st.session_state["age_img"] = img_age_old
                    
        with col_idade_map:
            st.markdown(f"**Mapa de Distribuição Etária: {idade_faixa}**")
            if "age_img" in st.session_state and st.session_state["age_img"]:
                st.image(st.session_state["age_img"], use_column_width=True)
            else:
                img_default_age = load_image("mapa_idade_10_14.png")
                if img_default_age:
                    st.image(img_default_age, use_column_width=True)

# ==========================================
# TAB 3: ECONOMIA E BIOMAS
# ==========================================
with tab_economia:
    st.markdown('<div class="section-title">Economia por Biomas do Nordeste</div>', unsafe_allow_html=True)
    
    col_bio_text, col_bio_map = st.columns([1, 1])
    
    with col_bio_text:
        st.write("""
        A distribuição ecológica do Nordeste conta com quatro biomas principais: **Caatinga, Cerrado, Mata Atlântica e Amazônia**. A atividade econômica local desenvolve-se de acordo com o potencial natural de cada bioma:
        
        * **Cerrado e MATOPIBA**: Situado no oeste e sul da região (fronteiras da Bahia, Piauí e Maranhão). É a área onde o agronegócio moderno de commodities agrícolas (**soja, milho e algodão**) ganhou imensa força nas últimas décadas. Caracteriza-se por grandes propriedades altamente automatizadas.
        * **Caatinga e Fruticultura Irrigada**: Ocupa mais da metade da região e convive com secas recorrentes. A pecuária de bovídeos é comum nas terras secas. No entanto, contornando a aridez hídrica com tecnologias de irrigação a partir do Rio São Francisco, o polo de **Petrolina (PE)** e **Juazeiro (BA)** tornou-se referência internacional na exportação de uvas, mangas e outras frutas.
        * **Mata Atlântica**: Ocupa a faixa litorânea leste. Tradicionalmente explorada pela extração de pau-brasil e plantações de cana-de-açúcar desde o período colonial. Hoje, concentra a maior densidade populacional e de serviços, além de abrigar polos industriais petroquímicos (Camaçari - BA) e unidades de conservação (ex. Chapada Diamantina - BA).
        * **Amazônia**: Presente no extremo oeste do estado do Maranhão devido à proximidade física com a região Norte do Brasil.
        """)
        
        st.markdown("""
        <div class="info-box" style="background-color: #f1f5f9; border-left-color: #475569; color: #1e293b;">
            <strong>Desigualdade Fundiária (Fernandes, 2004):</strong><br>
            A estrutura agrária do Nordeste é marcada por uma profunda divisão social. A imensa maioria dos proprietários de terras é formada por <b>pequenos produtores rurais</b> no Sertão e Agreste que produzem a maior parte dos alimentos que abastecem os mercados internos brasileiros. No lado oposto, estão os <b>grandes latifundiários</b> do Cerrado, com alta automatização voltada à exportação, que geram poucos empregos locais e acentuam a desigualdade de renda e de terras.
        </div>
        """, unsafe_allow_html=True)

    with col_bio_map:
        st.markdown("**Mapa da Biodiversidade e Biomas do Nordeste**")
        img_bioma = load_image("mapa_biomas.png")
        if img_bioma:
            st.image(img_bioma, use_column_width=True)

    st.markdown('<div class="section-title">Infraestrutura Logística e Potencial das Terras</div>', unsafe_allow_html=True)
    
    col_infra_txt, col_infra_map = st.columns([1, 1])
    
    with col_infra_txt:
        map_select = st.selectbox(
            "Selecione o mapa logístico ou de potencial agrícola:",
            ["Infraestrutura de Transportes (Rodovias, ferrovias e portos)", "Classes de Potencialidade Agrícola Natural das Terras"]
        )
        
        if "Transportes" in map_select:
            st.markdown("### Infraestrutura de Transportes e Escoamento de Safra")
            st.write("""
            O Nordeste possui um sistema rodoviário e portuário bem desenvolvido, atendendo principalmente à exportação de commodities. A malha ferroviária, contudo, ainda é restrita às áreas periféricas.
            
            Principais projetos e eixos estruturantes:
            * **Ferrovia Transnordestina**: Projetada para ligar a fronteira agrícola do Piauí aos portos de Pecém (Ceará) e Suape (Pernambuco), reduzindo custos de frete do interior.
            * **Ferrovia Norte-Sul e Estrada de Ferro Carajás**: Cruciais para o transporte de grãos e minérios do Maranhão e estados vizinhos até o Porto do Itaqui (São Luís - MA).
            """)
            selected_map_img = load_image("mapa_transportes.png")
            
        else:
            st.markdown("### Classes de Potencialidade Agrícola Natural (IBGE, 2022)")
            st.write("""
            Este mapeamento do IBGE qualifica as terras de acordo com sua aptidão natural para a agricultura:
            * **Classes A (Muito Boa/Boa)**: Áreas planas com solos férteis e boa pluviosidade, onde a mecanização agrícola é facilitada (destacada em verde/amarelo).
            * **Classes C e D (Restrita/Muito Restrita)**: Áreas com relevo acidentado, solos pedregosos, propensas à erosão ou com forte deficit hídrico (como grandes extensões do Semiárido). Exigem manejo sofisticado ou irrigação induzida.
            """)
            selected_map_img = load_image("mapa_potencialidade.png")
            
    with col_infra_map:
        st.markdown(f"**Visualização: {map_select}**")
        if selected_map_img:
            st.image(selected_map_img, use_column_width=True)

# ==========================================
# TAB 4: MODELO DE VON THÜNEN
# ==========================================
with tab_thunen:
    st.markdown('<div class="section-title">Teoria do Estado Isolado Aplicada ao Nordeste</div>', unsafe_allow_html=True)
    
    col_thunen_txt, col_thunen_map = st.columns([1, 1])
    
    with col_thunen_txt:
        st.write("""
        O modelo clássico de **Johann Heinrich von Thünen (1826)** explica a ocupação e uso do solo agrícola ao redor de um mercado consumidor central baseado na renda da terra e nos custos de transporte. 
        
        Na adaptação para o Nordeste, **Recife (PE)** é considerado como o mercado central consumidor e o principal porto de exportação. A organização das atividades ocorre em anéis concêntricos a partir de Recife:
        """)
        
        # Lista dos anéis
        st.markdown("""
        1. 🌟 **Mercado Central (Recife)**: Centro urbano consumidor e porto de exportação.
        2. 🥬🥛 **Anel 1: Horticultura e Laticínios**: Produtos altamente perecíveis e de transporte rápido, situados na proximidade imediata devido ao alto valor da terra e necessidade de consumo rápido.
        3. 🪵🌲 **Anel 2: Floresta (Combustíveis e Silvicultura)**: Extração de madeira e carvão vegetal. São produtos volumosos e pesados, exigindo proximidade para evitar fretes proibitivos.
        4. 🌾🚜 **Anel 3: Agricultura Extensiva (Grãos)**: Cultivos de grãos que possuem alta durabilidade e fácil estocagem, suportando custos de transporte por distâncias intermediárias.
        5. 🐂🏜️ **Anel 4: Pecuária Extensiva**: Localizada nas terras mais baratas do interior (Sertão e Agreste), onde o gado se desloca a pé ou é transportado de regiões distantes.
        """)
        
        st.write("""
        A regra básica de Von Thünen estabelece que **quanto mais próximo do mercado central, maior o custo da terra**. Por isso, a produção agrícola deve organizar-se para maximizar os lucros subtraindo os custos de frete do preço de mercado.
        """)
        
    with col_thunen_map:
        st.markdown("**Modelo de Von Thünen Aplicado ao Nordeste**")
        img_thunen = load_image("mapa_thunen.png")
        if img_thunen:
            st.image(img_thunen, use_column_width=True)

    st.markdown('<div class="section-title">Recomendações de Políticas Públicas</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-card" style="background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); border-color: #a7f3d0; color: #065f46;">
        <h4>Integração Produtiva e Irrigação no Sertão</h4>
        <p style="margin-top: 10px;">
            A adaptação do modelo de Von Thünen à realidade contemporânea sugere que, para descentralizar a riqueza e expandir a fronteira agrícola produtiva, os governos do <b>Ceará</b> e de <b>Pernambuco</b> devem buscar viabilizar e ampliar projetos voltados à <b>irrigação das terras do Sertão</b>.
        </p>
        <p>
            Essa ação estratégica possibilitará o cultivo viável de grãos e fruticultura no semiárido, expandindo a pauta de exportações regional, gerando empregos agrícolas no interior e descentralizando o desenvolvimento econômico do Nordeste.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 0.85rem; padding: 20px; border-top: 1px solid #e2e8f0; margin-top: 40px;">
    Análise da Região Nordeste • Bruno de Azevedo Gameiro • Disciplina de Economia Regional e Urbana • 2026
</div>
""", unsafe_allow_html=True)
