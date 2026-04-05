# 🔮 算命能力合集 (Divination Skills)

> 中华传统术数 AI 技能包 - 让你的 AI 助手学会算命起卦

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://github.com/openclaw/openclaw)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 简介

本技能包整合三大中华传统术数体系，让 OpenClaw、Claude、GPT 等 AI 助手能够进行专业的算命起卦服务。

| 术数 | 适用场景 | 优势 |
|------|----------|------|
| **六爻问卦** | 一事一断、简单预测、近期决策 | 快速直观、门槛低 |
| **奇门遁甲** | 择时决策、方位选择、趋吉避凶 | 时空结合、行动指南 |
| **紫微斗数** | 命盘分析、人生规划、长期运势 | 全面系统、结构清晰 |

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

### 使用方式

重启 OpenClaw 或刷新技能后，直接对话：

```
用户：帮我起个卦看看这件事能不能成
用户：用奇门看看今天适合去哪个方向
用户：帮我排个紫微命盘，我是1990年5月15日早上8点出生的男生
```

## 技能结构

```
divination/
├── SKILL.md                    # 主入口 - 自动选择方法
├── liuyao/                     # 六爻问卦
│   └── SKILL.md                # 起卦、解卦流程
├── qimen-dunjia/               # 奇门遁甲
│   ├── SKILL.md                # 排盘、解盘流程
│   └── references/
│       ├── yongshen.md         # 用神取用
│       ├── interview.md        # 访谈问题库
│       ├── ruleset-mainline.md # 默认规则
│       ├── geju.md             # 格局解读
│       └── examples.md         # 示例输出
└── ziwei-doushu/               # 紫微斗数
    ├── SKILL.md                # 排盘、解盘流程
    └── references/
        ├── calculation.md      # 排盘计算
        ├── stars.md            # 星曜详解
        ├── sihua.md            # 四化详解
        └── patterns.md         # 格局参考
```

## 功能特性

### 六爻问卦
- ✅ 三枚硬币起卦法
- ✅ 六亲取用神
- ✅ 世应关系分析
- ✅ 吉凶判断
- ✅ 应期推断

### 奇门遁甲
- ✅ 时家转盘奇门
- ✅ 阴遁/阳遁定局
- ✅ 用神取用
- ✅ 方位选择
- ✅ 择时决策

### 紫微斗数
- ✅ 十四主星排盘
- ✅ 十二宫位解读
- ✅ 四化分析
- ✅ 大限流年推演
- ✅ 格局判断

## 使用原则

### 必须做
- ✅ 先问清再分析
- ✅ 用人话解释术语
- ✅ 结论明确不模糊
- ✅ 高风险主题附现实建议

### 禁止做
- ❌ 恐吓式语言
- ❌ 宿命论表述
- ❌ 跳过信息收集
- ❌ 替代专业意见

## 示例对话

### 六爻问卦
```
用户：帮我看看下周面试能不能过
助手：好的，这是一个近期决策问题，适合用六爻来预测。
     请确认一下：面试是下周几？你想要"直接结论"还是"详细分析"？
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

- 奇门遁甲和紫微斗数技能基于 [FANzR-arch/Numerologist_skills](https://github.com/FANzR-arch/Numerologist_skills)
- 感谢所有传统术数研究者的贡献

## 免责声明

> 本技能包仅供学习和娱乐使用。传统术数属于中华文化遗产，解读结果用于辅助观察与思考，不代替医疗、法律、财务等专业意见。涉及重大决策时，请结合现实信息理性判断。

## License

MIT License - 自由使用、修改和分发

---

*让 AI 学会传统智慧 🔮*
