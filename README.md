# 🔮 算命能力合集 (Divination Skills)

> **8 大体系 · 3 脚本排盘 · 排盘靠计算不靠猜**

中华传统术数 + 西方命理与性格分析 AI 技能包 - 让你的 AI 助手掌握东西方命理智慧，并具备更透明、可校验的推演能力。

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://github.com/openclaw/openclaw)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 简介

本技能包整合中华传统术数和西方命理与性格分析体系，让 OpenClaw、Claude、GPT 等 AI 助手能够进行专业的算命起卦、塔罗解读和性格分析服务。

### 中华传统术数

| 术数 | 适用场景 | 排盘方式 |
|------|----------|----------|
| **六爻问卦** | 一事一断、近期决策、吉凶判断 | ⚙️ 脚本排盘 |
| **奇门遁甲** | 择时决策、方位选择、趋吉避凶 | ⚙️ 脚本排盘 |
| **紫微斗数** | 命盘分析、人生规划、长期运势 | ⚙️ 脚本排盘 |
| **子平八字** | 命局结构、十神格局、喜用神、大运流年 | LLM 解读 |

### 西方命理与性格分析

| 方法 | 适用场景 | 排盘方式 |
|------|----------|----------|
| **塔罗牌** 🆕 | 一事一断、直觉指引、心理探索 | LLM 解读 |
| **占星学** | 性格分析、情感模式、事业规划 | LLM 解读 |
| **九型人格** | 动机分析、个人成长、关系模式 | LLM 解读 |
| **MBTI** | 认知功能、职业匹配、团队建设 | LLM 解读 |

## ✨ 特点

- 🧮 **脚本排盘**：紫微斗数、奇门遁甲、六爻问卦均有 Python 排盘脚本，零依赖 LLM 心算
- 🃏 **塔罗解读**：基于 Rider-Waite-Smith 体系，支持 78 张牌正逆位解读，多种牌阵
- 🔄 **智能路由**：根据问题类型自动推荐最合适的方法
- 📚 **多源整合**：每个体系整合了多个优质来源的排盘规则和解读框架
- 🤖 **AI Agent 友好**：设计为 AI Agent 的技能插件，可被 OpenClaw 等 Agent 框架直接调用

## 快速开始

### 安装到 OpenClaw

```bash
# 方法1: 直接克隆到技能目录
cd ~/.openclaw/workspace/skills
git clone https://github.com/mingkunyuan/divination-skills.git divination

# 方法2: 下载压缩包
curl -L https://github.com/mingkunyuan/divination-skills/archive/main.tar.gz | tar xz
mv divination-skills-main ~/.openclaw/workspace/skills/divination
```

### 排盘脚本依赖

```bash
pip install -r requirements.txt
```

或者什么都不做——**wrapper 脚本首次运行时会自动创建 venv 并安装依赖**。

### 使用方式

重启 OpenClaw 或刷新技能后，直接对话：

```
用户：帮我起个卦看看这件事能不能成
用户：用奇门看看今天适合去哪个方向
用户：帮我排个紫微命盘，我是1990年5月15日早上8点出生的男生
用户：帮我看八字，想看事业和这两年的财运
用户：帮我抽个塔罗看看最近的方向
用户：最近心里很乱，想抽张牌看看
```

## 排盘脚本使用

### 紫微斗数
```bash
python3 scripts/run_ziwei.py --date 1983-04-29 --time 11:05 --gender male --format markdown
```

### 奇门遁甲
```bash
echo '{"question_type":"事业","time_input":"2026-06-09 10:00","calendar_type":"solar","location":{"country":"China","timezone":"Asia/Shanghai"},"ruleset":"mainline-cn-v1"}' > /tmp/qi_in.json
python3 scripts/run_qimen.py --input /tmp/qi_in.json --output /tmp/qi_out.json
cat /tmp/qi_out.json
```

### 六爻问卦
```bash
# 时间起卦
python3 scripts/run_liuyao.py --date "2026-06-09 10:00" --question "事业"

# 铜钱起卦（6次摇出的背面数，0-3）
python3 scripts/run_liuyao.py --coins "1,2,3,1,2,3" --question "财运"

# 数字起卦
python3 scripts/run_liuyao.py --numbers "3,5,7,2,8,9"
```

## 技能结构

```
divination/
├── SKILL.md                    # 主入口 - 自动选择方法
├── scripts/                    # 排盘 wrapper 脚本
│
├── liuyao/                     # 六爻问卦
│   ├── SKILL.md                # 起卦、解卦流程
│   ├── time-casting.md         # 时间起卦+六爻断卦
│   ├── scripts/                # 排盘脚本
│   └── references/             # 解读参考
│
├── qimen-dunjia/               # 奇门遁甲
│   ├── SKILL.md                # 排盘、解盘流程
│   ├── scripts/                # 排盘脚本
│   └── references/             # 解读参考
│
├── ziwei-doushu/               # 紫微斗数
│   ├── SKILL.md                # 排盘、解盘流程
│   ├── scripts/                # 排盘脚本
│   └── references/             # 解读参考
│
├── bazi/                       # 子平八字
│   └── SKILL.md                # 十神、格局、喜用神、大运流年
│
├── tarot/                      # 塔罗牌 🆕
│   ├── SKILL.md                # 抽牌、解读流程
│   └── references/             # 牌义、牌阵、解读规则
│
├── astrology/                  # 西方占星学
│   └── SKILL.md                # 星盘分析、相位解读
│
├── enneagram/                  # 九型人格
│   └── SKILL.md                # 九型测试、成长方向
│
└── mbti/                       # MBTI 性格类型
    └── SKILL.md                # 认知功能、类型分析
```

## 功能特性

### 六爻问卦
- ✅ 三枚硬币起卦法（传统）
- ✅ **时间起卦法**（梅花易数起卦 + 六爻纳甲断卦）
- ✅ **脚本排盘** — liuyao_pan.py
- ✅ 六亲取用神、世应关系分析、吉凶判断、应期推断

### 奇门遁甲
- ✅ 时家转盘奇门、阴遁/阳遁定局
- ✅ **脚本排盘** — qimen_cli.py
- ✅ 用神取用、方位选择、择时决策
- ✅ 结构化访谈流程

### 紫微斗数
- ✅ 十四主星排盘、十二宫位解读
- ✅ **脚本排盘** — ziwei_chart.py（双引擎 py/js 校验）
- ✅ 四化分析、大限流年推演、格局判断

### 子平八字
- ✅ 四柱命局分析、十神结构分析
- ✅ 格局与调候判断、喜用神/忌神分析
- ✅ 大运流年推演、出生信息不确定时的双方案校盘

### 塔罗牌 🆕
- ✅ 基于 Rider-Waite-Smith 体系，78 张牌正逆位
- ✅ 多种牌阵：单牌、三牌、凯尔特十字、关系牌阵
- ✅ 随机抽牌 + LLM 深度解读
- ✅ 中英双语支持
- ✅ 象征叙事型语气，尊重自由意志

### 占星学
- ✅ 太阳/月亮/上升星座分析
- ✅ 十大行星落点解读、十二宫位分析
- ✅ 相位解读、合盘比较、运势推演

### 九型人格
- ✅ 九种核心类型识别、三种副型分析
- ✅ 健康层级评估、整合与解离方向

### MBTI
- ✅ 四个维度测试、16 种性格类型识别
- ✅ 8 种认知功能分析、职业匹配建议

## 天府式增强能力（吸收版）

参考公开可见的 Tianfu Agent 产品思路，本技能额外增强：

- ✅ **透明依据**：结论尽量附关键盘面依据
- ✅ **不确定性分层**：高置信 / 中置信 / 待校验
- ✅ **迭代校正**：用户反馈不符时，优先回查时辰、口径、问题定义
- ✅ **主题化输出**：事业 / 关系 / 财富 / 阶段运势分模块表达
- ✅ **非模板化解读**：根据用户当前问题生成，不说空泛套话

## 使用原则

### 必须做
- ✅ 先问清再分析
- ✅ 有脚本的方法必须用脚本，不要 LLM 心算排盘
- ✅ 用人话解释术语
- ✅ 结论明确不模糊
- ✅ 高风险主题附现实建议
- ✅ 重要结论尽量附依据
- ✅ 信息不足时明确标注不确定性

### 禁止做
- ❌ 恐吓式语言
- ❌ 宿命论表述
- ❌ 跳过信息收集
- ❌ 替代专业意见
- ❌ 在有脚本可用时手算排盘

## 示例对话

### 六爻问卦
```
用户：帮我看看下周面试能不能过
助手：好的，这是一个近期决策问题，适合用六爻来预测。
     请确认一下：面试是下周几？你想要"直接结论"还是"详细分析"？
```

### 塔罗牌 🆕
```
用户：帮我抽个塔罗看看最近的方向
助手：好的！你想看哪一方面？感情、事业、还是整体方向？
     也可以直接说"帮我抽三张牌"——我会用过去·现在·未来的牌阵来读。
```

### 八字分析
```
用户：帮我看八字，这几年事业怎么样
助手：可以。我先确认几项关键信息：
     1. 出生日期是公历还是农历？
     2. 具体出生时间尽量精确到几点。
     3. 性别和出生城市补一下。
     4. 你这次更想看整体事业路径，还是重点看近两三年的变化？
```

### 奇门遁甲
```
用户：用奇门帮我看看今天去哪个方向谈合作比较好
助手：好的，奇门可以帮你选择方位。
     请告诉我：1）你在哪个城市？2）大概几点出发？
```

### 紫微斗数
```
用户：帮我排个紫微命盘
助手：好的，排紫微命盘需要一些信息：
     1. 出生日期是公历还是农历？
     2. 具体年月日是？
     3. 出生时间尽量精确到时辰
     4. 性别
```

## 致谢

本技能整合了多位作者的心血：

| 子技能 | 排盘脚本来源 | 解读参考来源 |
|--------|------------|------------|
| 紫微斗数 | [spyfree](https://clawhub.com) | spyfree + [mingkunyuan](https://github.com/mingkunyuan/divination-skills) |
| 奇门遁甲 | [FANzR-arch](https://github.com/FANzR-arch/Numerologist_skills) | FANzR-arch + [eamanc-lab](https://clawhub.com) + mingkunyuan |
| 六爻问卦 | [天工长老](https://clawhub.com) | eamanc-lab + mingkunyuan |
| 八字四柱 | — | eamanc-lab |
| 塔罗牌 🆕 | — | eamanc-lab |
| 占星/九型/MBTI | — | [clider0915](https://github.com/clider0915/divination-skills) |

## 免责声明

> 本技能包仅供学习和娱乐使用。传统术数属于中华文化遗产，塔罗占星属于西方文化传统，解读结果用于辅助观察与思考，不代替医疗、法律、财务等专业意见。涉及重大决策时，请结合现实信息理性判断。

## License

MIT License - 自由使用、修改和分发

---

*算命能力合集 v3.0 — 8 体系 · 3 脚本排盘 · 排盘靠计算不靠猜 🔮*
