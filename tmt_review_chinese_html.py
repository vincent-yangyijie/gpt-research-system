#!/usr/bin/env python3
"""
Generate TMT Literature Review in Chinese HTML format
"""

import os
from collections import defaultdict

def categorize_tmt_papers():
    """Categorize TMT papers by research focus"""

    tmt_dir = "../TMT"
    if not os.path.exists(tmt_dir):
        print(f"❌ TMT directory not found: {tmt_dir}")
        return {}

    papers = {}
    categories = defaultdict(list)

    # Define category keywords
    category_keywords = {
        "Thermal Management": ["thermal", "temperature", "heat", "stability"],
        "Optical Design": ["optical", "telescope", "lens", "imaging", "aberration"],
        "Structural Analysis": ["dynamic", "jitter", "vibration", "structural"],
        "Environmental Effects": ["environment", "atmospheric", "thermal environment"],
        "Simulation Tools": ["simulation", "modeling", "code v", "analysis tool"],
        "System Integration": ["design", "test", "performance", "integration"],
        "Space Applications": ["space", "satellite", "remote sensing", "mars"],
        "Machine Learning": ["machine learning", "prediction", "framework"]
    }

    for filename in os.listdir(tmt_dir):
        if filename.endswith('.pdf'):
            filepath = os.path.join(tmt_dir, filename)
            papers[filename] = filepath

            # Categorize paper
            title_lower = filename.lower()
            for category, keywords in category_keywords.items():
                if any(keyword in title_lower for keyword in keywords):
                    categories[category].append(filename)

    return papers, dict(categories)

def generate_chinese_html_review():
    """Generate comprehensive literature review in Chinese HTML format"""

    print("🔬 生成TMT文献综述 - 中文HTML格式")
    print("=" * 60)

    papers, categories = categorize_tmt_papers()

    if not papers:
        print("❌ 未找到论文")
        return

    print(f"📚 分析TMT论文总数: {len(papers)}")
    print(f"📂 分类研究领域: {len(categories)}")
    print()

    # Start HTML content
    html_parts = []

    html_parts.append("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>三十米望远镜(TMT)研究文献综述</title>
    <style>
        body {
            font-family: 'Microsoft YaHei', 'SimSun', Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            color: #34495e;
            border-left: 4px solid #3498db;
            padding-left: 15px;
            margin-top: 30px;
        }
        h3 {
            color: #7f8c8d;
            margin-top: 25px;
        }
        .summary {
            background: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .paper-list {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .paper-item {
            margin: 5px 0;
            padding: 5px;
            background: white;
            border-radius: 3px;
        }
        .stats {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
        }
        .stat-box {
            background: #3498db;
            color: white;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
            flex: 1;
            margin: 0 10px;
        }
        .references {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 5px;
            margin-top: 30px;
        }
        .category-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .category-card {
            background: #e8f4f8;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }
        .category-title {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>三十米望远镜(TMT)研究文献综述</h1>

        <div class="stats">
            <div class="stat-box">
                <h3>论文总数</h3>
                <div style="font-size: 2em; font-weight: bold;">""")

    html_parts.append(str(len(papers)))

    html_parts.append("""</div>
            </div>
            <div class="stat-box">
                <h3>研究领域</h3>
                <div style="font-size: 2em; font-weight: bold;">""")

    html_parts.append(str(len(categories)))

    html_parts.append("""</div>
            </div>
            <div class="stat-box">
                <h3>核心主题</h3>
                <div style="font-size: 2em; font-weight: bold;">6</div>
            </div>
        </div>

        <div class="summary">
            <h2>执行摘要</h2>
            <p>本文献综述分析了与三十米望远镜(TMT)项目相关的18篇研究论文，涵盖从设计概念化到先进模拟和测试方法的全过程。综述识别了大规模光学望远镜系统中的关键研究主题、技术挑战和未来发展方向。</p>
            <p>TMT代表了现代望远镜技术的巅峰之作，其30米的巨大尺寸带来了前所未有的工程挑战。本综述系统地梳理了TMT相关研究，特别关注热管理、光学设计、结构分析和系统集成等关键领域。</p>
        </div>

        <h2>研究概况</h2>

        <h3>论文分类统计</h3>
        <div class="category-grid">
""")

    # Add category statistics
    category_names_zh = {
        "Thermal Management": "热管理",
        "Optical Design": "光学设计",
        "Structural Analysis": "结构分析",
        "Environmental Effects": "环境影响",
        "Simulation Tools": "模拟工具",
        "System Integration": "系统集成",
        "Space Applications": "空间应用",
        "Machine Learning": "机器学习"
    }

    for category, paper_list in categories.items():
        zh_name = category_names_zh.get(category, category)
        html_parts.append(f"""
            <div class="category-card">
                <div class="category-title">{zh_name} ({len(paper_list)}篇)</div>
                <div class="paper-list">
""")
        for paper in paper_list[:3]:  # Show first 3 papers
            html_parts.append(f"""                    <div class="paper-item">• {paper}</div>
""")
        if len(paper_list) > 3:
            html_parts.append(f"""                    <div class="paper-item"><em>... 还有{len(paper_list)-3}篇论文</em></div>
""")
        html_parts.append("""                </div>
            </div>
""")

    # Add the rest of the HTML content
    html_parts.append("""
        </div>

        <h2>详细分析</h2>

        <h3>1. 热管理和稳定性</h3>
        <p>热管理研究是TMT发展的关键焦点领域，多项研究解决了在不同环境条件下维持光学稳定的挑战。</p>
        <div class="paper-list">
            <div class="paper-item">• Thermal modeling environment for TMT.pdf</div>
            <div class="paper-item">• Thermal modeling of the TMT Telescope.pdf</div>
            <div class="paper-item">• Thermal performance prediction of the TMT optics.pdf</div>
            <div class="paper-item">• TMT光学系统在复杂热环境下的稳定性.pdf</div>
            <div class="paper-item">• TMT光学系统在复杂热环境下稳定性研究中，如何通过理论推导、工程仿真和实验验证提出优化方案？.pdf</div>
        </div>

        <h3>2. 光学设计与性能</h3>
        <p>光学设计研究涵盖了为超大望远镜创建高性能光学系统的核心工程挑战。</p>
        <div class="paper-list">
            <div class="paper-item">• Design and test of a high performance off-axis TMA telescope.pdf</div>
            <div class="paper-item">• High-resolution optical modeling of the Thirty Meter Telescope.pdf</div>
            <div class="paper-item">• 用于火星沙尘暴探测的广角多光谱成像光学系统设计.pdf</div>
            <div class="paper-item">• 温度环境下空间遥感光学系统成像质量的检测.pdf</div>
        </div>

        <h3>3. 结构与动力学分析</h3>
        <p>结构分析解决了支持和维持30米级望远镜对准的机械挑战。</p>
        <div class="paper-list">
            <div class="paper-item">• Dynamic analysis of TMT.pdf</div>
            <div class="paper-item">• Development of Integrated Simulation Tool for Jitter Analysis.pdf</div>
        </div>

        <h3>4. 环境与操作挑战</h3>
        <p>研究解决望远镜部署的环境因素和操作考虑。</p>
        <div class="paper-list">
            <div class="paper-item">• Environmental Modeling and Athermalization in CODE V.pdf</div>
            <div class="paper-item">• Ultra-Stable Observatory Roman Space Telescope Stability.pdf</div>
            <div class="paper-item">• Thermal Stability Optimization of the Luojia 1-01.pdf</div>
        </div>

        <h3>5. 模拟与分析方法</h3>
        <p>先进的计算工具和望远镜分析方法。</p>
        <div class="paper-list">
            <div class="paper-item">• Environmental Modeling and Athermalization in CODE V.pdf</div>
            <div class="paper-item">• Development of Integrated Simulation Tool for Jitter Analysis.pdf</div>
            <div class="paper-item">• High-resolution optical modeling of the Thirty Meter Telescope.pdf</div>
        </div>

        <h3>6. 新兴技术和应用</h3>
        <p>探索新技术的前瞻性研究。</p>
        <div class="paper-list">
            <div class="paper-item">• machine-learning-based-framework-for-quick-prediction-of-tg-and-td-of-oled-materials.pdf</div>
            <div class="paper-item">• 用于火星沙尘暴探测的广角多光谱成像光学系统设计.pdf</div>
        </div>

        <h2>关键发现与主题</h2>

        <h3>技术挑战</h3>
        <ul>
            <li><strong>热稳定性：</strong>维持光学对准跨越极端温度变化</li>
            <li><strong>规模管理：</strong>30米级光学系统的工程解决方案</li>
            <li><strong>环境适应：</strong>减轻大气和操作环境影响</li>
            <li><strong>系统集成：</strong>协调多个复杂子系统</li>
            <li><strong>性能优化：</strong>平衡成本、复杂性和光学性能</li>
        </ul>

        <h3>研究模式</h3>
        <ul>
            <li><strong>多学科方法：</strong>光学、机械、热和控制系统工程的集成</li>
            <li><strong>模拟驱动设计：</strong>大量依赖计算建模和分析工具</li>
            <li><strong>迭代优化：</strong>通过模拟和测试逐步完善设计</li>
            <li><strong>跨平台验证：</strong>使用多种分析工具(CODE V、自定义模拟等)</li>
        </ul>

        <h3>技术创新</h3>
        <ul>
            <li>先进的热管理策略</li>
            <li>集成模拟框架</li>
            <li>机器学习在设计优化中的应用</li>
            <li>针对极端环境的专用光学设计</li>
            <li>多物理建模方法</li>
        </ul>

        <h2>未来研究方向</h2>

        <h3>近期优先事项</h3>
        <ul>
            <li><strong>集成系统测试：</strong>全尺寸原型验证</li>
            <li><strong>先进控制系统：</strong>主动光学和振动控制</li>
            <li><strong>成本优化：</strong>平衡性能与建设预算</li>
            <li><strong>操作可靠性：</strong>长期维护和校准策略</li>
        </ul>

        <h3>长期机遇</h3>
        <ul>
            <li><strong>AI驱动设计：</strong>机器学习自动化优化</li>
            <li><strong>自适应光学：</strong>实时大气补偿</li>
            <li><strong>模块化架构：</strong>可扩展设计方法</li>
            <li><strong>多信使集成：</strong>结合光学和其他天文观测</li>
        </ul>

        <h2>结论</h2>
        <p>TMT研究文献展示了解决30米级望远镜开发前所未有挑战的全面方法。这些研究涵盖从基础光学设计到操作考虑的全谱，特别强调热管理和系统集成。</p>
        <p>研究突显了现代望远镜开发的跨学科性质，需要光学、机械、热工程和软件系统的专业知识。模拟工具的广泛使用和专门分析框架的开发强调了这些系统的复杂性和对先进计算方法的需求。</p>
        <p>随着TMT向建设和运营迈进，这些研究建立的研究基础为成功实施和未来大规模望远镜项目提供了关键见解。</p>

        <div class="references">
            <h2>参考文献</h2>
""")

    # Add all papers as references
    for i, (filename, filepath) in enumerate(papers.items(), 1):
        clean_title = filename.replace('.pdf', '').replace('_', ' ')
        html_parts.append(f"""            <p>{i}. {clean_title}</p>
""")

    html_parts.append("""
        </div>
    </div>
</body>
</html>
""")

    # Join all HTML parts
    html_content = ''.join(html_parts)

    # Save the HTML file
    output_file = "tmt_literature_review_chinese.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ 中文HTML文献综述已生成并保存至: {output_file}")
    print("\n" + "="*80)
    print("TMT文献综述 - 中文HTML版本")
    print("="*80)
    print("📄 文件包含完整的中文分析和格式化的HTML布局")
    print("🌐 可在浏览器中直接打开查看")
    print("="*80)

if __name__ == "__main__":
    generate_chinese_html_review()
