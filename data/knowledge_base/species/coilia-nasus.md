# ═══════════════════════════════════════════════════════════════
# 刀鲚 (Coilia nasus) 物种知识库
# ═══════════════════════════════════════════════════════════════
# 课题组: 淡水渔业研究中心 刘凯研究员
# 相关物种: 短颌鲚 (C. brachygnathus)、凤鲚 (C. mystus)
# 分类地位: 鲱形目 > 鳀科 > 鲚属

species:
  id: "Coilia_nasus"
  chinese: "刀鲚"
  common_names: ["长江刀鱼", "刀鱼", "长颌鲚", "tapertail anchovy"]
  scientific: "Coilia nasus"
  family: "鳀科 (Engraulidae)"
  order: "鲱形目 (Clupeiformes)"
  genus: "Coilia"

  # IUCN 与保护 status
  conservation:
    iucn: "濒危(EN)"
    china_red_list: "濒危"
    protection_level: "未列入国家重点保护名录"
    yangtze_fishing_ban: "2021年起全面禁捕"
    special_permit: "2019年起停止发放专项捕捞许可证"

  # 生物学特征
  biology:
    max_length: "41 cm"
    common_length: "18-35 cm"
    max_weight: "~200 g"
    lifespan: "4-5 年"
    habitat: "溯河洄游性 — 海洋生长，淡水繁殖"
    spawning_season: "4-6月"
    spawning_grounds: "长江中下游及附属湖泊"
    feeding: "浮游动物、小型甲壳类、仔鱼"
    migration_type: "溯河洄游 (anadromous)"

  # 洄游特征
  migration:
    upstream_period: "2-4月 (溯江而上)"
    downstream_period: "秋冬季 (幼鱼降海)"
    historical_range: "长江口至洞庭湖 (最远可达宜昌)"
    current_range: "大幅萎缩，主要集中于长江口-安徽段"
    key_barriers: ["三峡大坝", "葛洲坝", "沿江多个闸坝"]

  # 经济与文化价值
  cultural:
    nickname: "长江三鲜之首 (刀鱼、鲥鱼、河豚)"
    peak_price: "清明前刀鱼曾达 8000-10000 元/斤"
    fishing_gear: "刀鱼网 (流刺网)、滚钩"
    culinary: "清蒸刀鱼为江南名菜"

  # 近缘种与分类混淆
  related_species:
    - name: "短颌鲚"
      scientific: "Coilia brachygnathus"
      difference: "淡水定居型，上颌骨较短，终生不入海。历史上曾被视为C. nasus同物异名或亚种(C. nasus taihuensis)。mtDNA控制区序列支持独立物种地位(Tang 2007)。与刀鲚存在自然杂交(Sun et al. 2026, Mar Biotechnol)。长江中下游泛滥平原湖泊优势种。"
      conservation: "无保护status"
      key_papers: ["Tang WQ 2007 Biodiversity Science", "Sun Z et al. 2026 Mar Biotechnol (hybridization discovery)"]
    - name: "凤鲚"
      scientific: "Coilia mystus"
      difference: "沿海-河口分布为主，偶入长江下游。体型较小，体色较浅。曾被记为C. ectenes的一部分。Yang et al.(2006)通过耳石Sr/Ca验证其与C. ectenes(刀鲚)的栖息地利用差异。"
      conservation: "IUCN EN"
      key_papers: ["Yang J et al. 2006 J Fish Biol (otolith Sr/Ca)", "He WP et al. 2011 (molecular ID of larvae)"]
    - name: "太湖湖鲚"
      scientific: "Coilia nasus taihuensis (生态型)"
      difference: "刀鲚的淡水定居生态型(ecomorphotype)，终生生活在太湖等湖泊中，不进行江海洄游。比较蛋白质组学显示洄游型与定居型嗅觉上皮蛋白表达差异(Zheng et al. 2019)。Liu et al.(2025)在长江大湾洲段识别出不同生态形态型。"
      conservation: "资源量相对稳定"
      key_papers: ["Zheng L et al. 2019 J Oceanol Limnol", "Liu JH et al. 2025 Fishes (ecomorphotypes)"]

  # 三鲚区分简明表
  species_comparison_table:
    - species: "刀鲚 Coilia nasus"
      migration: "溯河洄游(anadromous)"
      max_length: "41 cm"
      upper_jaw: "长，超过鳃盖后缘"
      sr_ca_pattern: "低→高→低 (淡水→海水→淡水)"
      habitat: "长江干流+海洋"
    - species: "短颌鲚 C. brachygnathus"
      migration: "淡水定居(resident)"
      max_length: "25 cm"
      upper_jaw: "短，不超过鳃盖"
      sr_ca_pattern: "持续低Sr/Ca (终生淡水)"
      habitat: "长江中下游湖泊+干流"
    - species: "凤鲚 C. mystus"
      migration: "河口-近海(estuarine)"
      max_length: "20 cm"
      upper_jaw: "中等长度"
      sr_ca_pattern: "中高Sr/Ca波动(河口-海水)"
      habitat: "长江口+近海"

  # 分类历史(理解学名变体至关重要)
  taxonomic_note: >
    Coilia nasus的分类历史复杂，涉及多次学名变更：
    - C. ectenes (Jordan & Seale 1905) → 曾长期作为刀鲚学名使用
    - C. nasus (Temminck & Schlegel 1846) → 当前公认学名
    - C. brachygnathus → 曾为C. nasus同物异名，现恢复为独立种
    - C. nasus taihuensis → 太湖定居生态型，分类地位存争议
    文献检索时必须同时使用以上所有学名变体，否则会遗漏大量早期文献。

  # 资源变迁
  population_trend:
    historical_peak: "1973年长江刀鱼产量 3750t"
    recent_low: "2010年后年产量不足 100t，部分年份 < 50t"
    fishing_ban_effect: >
      2021年禁捕后恢复显著:
      - Wang et al.(2024): 长江口相对生物量B/B0从0.22(2020)→0.90(2023), 体长+40%, 体重+134%, F/M从2.65→0.06
      - Chen et al.(2026): 刀鲚禁渔后早期恢复呈时空异质性, 环境因子(SST/盐度/径流)是关键驱动
      - Luo et al.(2025): 鄱阳湖水道LBB评估显示资源正在恢复
      - 但分子层面: 遗传多样性总体不高(Zhang et al. 2025/2026微卫星), ΔNe恢复待观察
    note: "刀鲚为FFART框架中r-对策洄游种的'最快响应'验证物种——生物量恢复极快，但结构不对称(ΔS)和遗传不对称(ΔNe)仍存疑"

# ══════════════════════════════════════════════════════════════
# 关键研究主题
# ══════════════════════════════════════════════════════════════
research_themes:
  - theme: "耳石微化学与洄游履历"
    methods: ["LA-ICP-MS", "Sr/Ca 比分析", "电子探针"]
    key_questions:
      - "刀鲚个体洄游履历如何重建？"
      - "不同群体间洄游模式差异？"
      - "水利工程对洄游通道的阻断程度？"

  - theme: "群体遗传学与种群结构"
    methods: ["微卫星(SSR)", "线粒体DNA", "SNP", "RAD-seq"]
    key_questions:
      - "长江刀鲚是否有多群体结构？"
      - "刀鲚与短颌鲚的遗传分化程度？"
      - "禁捕后遗传多样性是否恢复？"

  - theme: "资源评估与管理"
    methods: ["CPUE标准化", "体长频率法", "Beverton-Holt模型"]
    key_questions:
      - "禁捕后刀鲚资源恢复速率？"
      - "最大可持续产量(MSY)是多少？"
      - "何时可以考虑重新开放捕捞？"

  - theme: "早期资源与补充群体"
    methods: ["仔鱼网调查", "耳石日轮分析", "产卵场调查"]
    key_questions:
      - "刀鲚产卵场现状与分布？"
      - "补充群体数量年际变化？"

  - theme: "食性与营养生态"
    methods: ["胃含物分析", "稳定同位素(δ13C/δ15N)", "DNA宏条形码"]
    key_questions:
      - "刀鲚在不同生活史阶段的食性转换？"
      - "禁捕后食物网结构变化？"

# ══════════════════════════════════════════════════════════════
# 关键研究团队与文献 (国内)
# ══════════════════════════════════════════════════════════════
key_research_groups:
  - institution: "淡水渔业研究中心·南京农业大学无锡渔业学院"
    researchers: ["刘凯", "徐东坡", "施炜纲", "方弟安", "段金荣", "马凤娇", "应聪萍", "杨彦平", "郭弘艺", "唐文乔"]
    focus: "刀鲚资源评估、洄游生态、分子生物学(基因组/转录组/蛋白组/肠道微生物)、产卵迁移生理"
    key_papers:
      - "Ma F et al. 2025 Ecol Evol — Two Ecotypes Population Genomics (刘凯通讯)"
      - "Guo H et al. 2025 Biology — Spatial & Sex-Specific Growth Variations (刘凯通讯)"
      - "Wei SW et al. 2024 Fishes — Ovarian Development during Breeding Migration (刘凯参与)"
      - "Yang C et al. 2025 Microorganisms — Multi-Omics Gut Microbiota (刘凯参与)"
      - "Ma F et al. 2022 Comp Biochem Physiol — Proteomics digestive response (刘凯通讯)"
      - "Ying C et al. 2022 J Fish Biol — Anisakidae parasitism & liver fibrosis (刘凯通讯)"
      - "Yin D et al. 2020 Genomics — Metabolic mechanisms during migration (刘凯通讯)"
      - "Ying CP et al. 2020 Curr Microbiol — Gut microbiome spawning migration (刘凯通讯)"
      - "Ma F et al. 2019 J Fish Biol — Digestive enzyme activity migration (刘凯通讯)"
      - "Fang DA et al. 2017 Genes — HSP60/HSP10 testis development (刘凯参与)"
      - "Duan JR et al. 2016 BMC Dev Biol — GnRH receptor spawning migration (刘凯参与)"
      - "Wang M et al. 2016 Gene — LPL molecular cloning (刘凯参与)"
      - "Fang DA et al. 2016 Genes — HSP90AA1 anadromous fish (刘凯参与)"
      - "Duan JR et al. 2015 Mar Genomics — Ovary transcriptome spawning (刘凯参与)"
      - "刘凯等 2009 动物学杂志 — 凤鲚刀鲚湖鲚肌肉生化成分"

  - institution: "中国水产科学研究院淡水渔业研究中心·渔业微化学实验室"
    researchers: ["杨健", "姜涛", "刘洪波", "陈修报"]
    focus: "刀鲚/短颌鲚耳石微化学、Sr/Ca与87Sr/86Sr生活史重建、洄游模式多样性"
    key_papers:
      - "Song C et al. 2024 Fishes — Otolith Microchemistry Diversity of Migration Patterns (长江口)"
      - "Hu YH et al. 2022 Fishes — Dayang River life history otolith microchemistry"
      - "Xuan ZY et al. 2022 Reg Stud Mar Sci — Poyang Lake vs Estuary divergence (耳石+微卫星)"
      - "Sokta L et al. 2020 Heliyon — Loss of habitats in freshwater lakes"
      - "Jiang T et al. 2014 — Life History Variations Among Different Populations"
      - "Jiang T et al. 2012 Environ Biol Fish — Yellow Sea life history Sr:Ca"
      - "Jiang T et al. 2013 水产学报 — Two microchemistry patterns Poyang Lake"
      - "Chen TT et al. 2016 湖泊科学 — Jingjiang section C. nasus vs C. brachygnathus otolith"
      - "Li MM et al. 2017 生态学报 — Anqing section migration ecology"
      - "Sun Z et al. 2026 Mar Biotechnol — Natural Hybridization C. nasus × C. brachygnathus"

  - institution: "中国水产科学研究院东海水产研究所"
    researchers: ["庄平", "赵峰", "宋超"]
    focus: "刀鲚耳石微化学、长江口洄游、产卵场分布"
    key_papers:
      - "Song C et al. 2024 Fishes — Spawning Ground Distribution (长江口)"
      - "Wang SY et al. 2024 Front Mar Sci — Recovery after fishing ban (长江口)"

  - institution: "上海海洋大学"
    researchers: ["唐文乔", "刘其根"]
    focus: "刀鲚遗传学、群体结构、生态形态型识别"
    key_papers:
      - "Liu JH et al. 2025 Fishes — Different Ecomorphotypes Dawanzhou Section"
      - "Zheng L et al. 2019 J Oceanol Limnol — Olfactory rosette proteomics anadromous vs resident"

  - institution: "中国科学院水生生物研究所"
    researchers: ["刘焕章", "陈毅峰"]
    focus: "长江鱼类多样性、刀鲚保护生物学"
    key_papers:
      - "Liu HZ 2026 Chin Sci Bull — Ten-year fishing ban and river ecosystem restoration"

  - institution: "江西省水生生物保护救助中心"
    researchers: ["王生", "罗玉兰"]
    focus: "鄱阳湖刀鲚资源评估"
    key_papers:
      - "Luo YL et al. 2025 Front Mar Sci — LBB stock recovery Poyang Lake"

  - institution: "上海海洋大学/东海所"
    researchers: ["陈桂琴", "冯广朋"]
    focus: "刀鲚禁渔后早期恢复·时空格局"
    key_papers:
      - "Chen GQ et al. 2026 Fishes — Early Recovery Responses Spatiotemporal Patterns"
