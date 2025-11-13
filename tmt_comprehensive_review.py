#!/usr/bin/env python3
"""
Comprehensive TMT Literature Review with Web Resources
Combines local TMT papers with web-retrieved resources
"""

import os
import asyncio
from dotenv import load_dotenv
from gpt_researcher import GPTResearcher

# Load environment variables
load_dotenv()

def get_tmt_paper_paths():
    """Get paths to all TMT papers"""
    tmt_dir = "../TMT"
    if not os.path.exists(tmt_dir):
        print(f"❌ TMT directory not found: {tmt_dir}")
        return []

    paper_paths = []
    for filename in os.listdir(tmt_dir):
        if filename.endswith('.pdf'):
            full_path = os.path.join(tmt_dir, filename)
            paper_paths.append(full_path)
            print(f"📄 Found local paper: {filename}")

    print(f"\n📚 Local TMT papers: {len(paper_paths)}")
    return paper_paths

async def conduct_web_research():
    """Conduct web research on TMT topics"""
    print("\n🔍 Conducting web research on TMT topics...")

    # Configure API keys
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
    os.environ["OPENAI_API_KEY"] = os.getenv("KIMI_API_KEY")  # Use KIMI key for OpenAI-compatible access
    os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

    # LLM Configuration
    os.environ["FAST_LLM"] = "google_genai:gemini-2.0-flash-exp"
    os.environ["SMART_LLM"] = "openai:kimi-k2"  # Use OpenAI provider with KIMI model
    os.environ["EMBEDDING"] = "openai:text-embedding-3-small"

    web_research_query = """
    Conduct comprehensive research on the Thirty Meter Telescope (TMT) project. Focus on:

    1. **Current Status and Timeline**: Latest updates on TMT construction, delays, and expected completion
    2. **Technical Specifications**: Detailed technical parameters, mirror design, and performance metrics
    3. **Location and Site**: Mauna Kea site details, environmental considerations, and community relations
    4. **Scientific Objectives**: Primary science goals, observing capabilities, and research programs
    5. **International Collaboration**: Partner institutions, funding, and governance structure
    6. **Technological Innovations**: Advanced technologies developed for TMT
    7. **Comparison with Other Telescopes**: How TMT compares to existing and planned large telescopes
    8. **Challenges and Controversies**: Technical challenges, legal issues, and community opposition
    9. **Future Developments**: Plans for operations, data management, and scientific output

    Provide detailed, current information from reliable sources including official TMT websites, scientific publications, and news sources. Include specific technical details, timelines, and quantitative specifications where available.
    """

    try:
        researcher = GPTResearcher(
            query=web_research_query,
            report_type="research_report",
            report_format="markdown",
            tone="Objective"
        )

        print("🌐 Searching web resources...")
        await researcher.conduct_research()

        print("📝 Generating web research report...")
        web_report = await researcher.write_report()

        return web_report

    except Exception as e:
        print(f"❌ Web research error: {e}")
        return "Web research unavailable due to API configuration issues."

async def generate_comprehensive_review():
    """Generate comprehensive TMT review combining local papers and web resources"""

    print("🔬 生成TMT综合文献综述")
    print("=" * 80)
    print("📚 结合本地论文和网络资源")
    print()

    # Get local papers
    paper_paths = get_tmt_paper_paths()

    # Conduct web research
    web_report = await conduct_web_research()

    # Combine findings
    comprehensive_query = f"""
    Create a comprehensive literature review of the Thirty Meter Telescope (TMT) by synthesizing:

    **Local Research Papers ({len(paper_paths)} papers):**
    The provided papers cover technical aspects including thermal management, optical design, structural analysis, simulation tools, and environmental effects.

    **Web Research Findings:**
    {web_report}

    **Synthesis Requirements:**
    1. **Integration**: Combine insights from local papers with current web information
    2. **Current Status**: Include latest TMT project status, timeline, and developments
    3. **Technical Depth**: Provide detailed technical specifications and performance metrics
    4. **Context**: Place the research papers within the broader TMT project context
    5. **Future Outlook**: Discuss implications for telescope development and astronomical research

    **Structure the review with:**
    - Executive summary with current project status
    - Technical specifications and capabilities
    - Analysis of research papers in project context
    - Current challenges and developments
    - Future research directions and opportunities
    - Comprehensive bibliography including both local papers and web sources
    """

    # Configure for final synthesis
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
    os.environ["OPENAI_API_KEY"] = os.getenv("KIMI_API_KEY")
    os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
    os.environ["FAST_LLM"] = "google_genai:gemini-2.0-flash-exp"
    os.environ["SMART_LLM"] = "kimi:kimi-k2"
    os.environ["EMBEDDING"] = "openai:text-embedding-3-small"

    try:
        print("🔄 Synthesizing comprehensive review...")
        researcher = GPTResearcher(
            query=comprehensive_query,
            report_type="research_report",
            report_format="markdown",
            document_urls=paper_paths,
            tone="Objective"
        )

        await researcher.conduct_research()
        final_report = await researcher.write_report()

        # Save comprehensive review
        output_file = "tmt_comprehensive_review.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_report)

        print(f"✅ 综合文献综述已生成: {output_file}")

        # Generate Chinese HTML version
        await generate_chinese_html_comprehensive(final_report, len(paper_paths))

        return final_report

    except Exception as e:
        print(f"❌ Synthesis error: {e}")
        return None

async def generate_chinese_html_comprehensive(markdown_content, local_paper_count):
    """Generate Chinese HTML version of comprehensive review"""

    print("🌐 生成中文HTML版本...")

    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>三十米望远镜(TMT)综合研究文献综述</title>
    <style>
        body {{
            font-family: 'Microsoft YaHei', 'SimSun', Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            border-left: 4px solid #3498db;
            padding-left: 15px;
            margin-top: 30px;
        }}
        h3 {{
            color: #7f8c8d;
            margin-top: 25px;
        }}
        .summary {{
            background: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .highlight {{
            background: #e8f4f8;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
            margin: 20px 0;
        }}
        .stats {{
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
        }}
        .stat-box {{
            background: #3498db;
            color: white;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
            flex: 1;
            margin: 0 10px;
        }}
        .source-badge {{
            display: inline-block;
            background: #27ae60;
            color: white;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.8em;
            margin-left: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>三十米望远镜(TMT)综合研究文献综述</h1>

        <div class="stats">
            <div class="stat-box">
                <h3>本地论文</h3>
                <div style="font-size: 2em; font-weight: bold;">{local_paper_count}</div>
            </div>
            <div class="stat-box">
                <h3>网络资源</h3>
                <div style="font-size: 2em; font-weight: bold;">集成</div>
            </div>
            <div class="stat-box">
                <h3>研究深度</h3>
                <div style="font-size: 2em; font-weight: bold;">全面</div>
            </div>
        </div>

        <div class="summary">
            <h2>综述概述</h2>
            <p>本综合文献综述整合了{local_paper_count}篇本地TMT研究论文与最新的网络资源信息，提供了三十米望远镜项目的完整技术分析和当前发展状况。</p>
            <p>综述结合了详细的技术研究论文与最新的项目进展信息，为理解TMT项目的全貌提供了全面视角。</p>
        </div>

        <div class="highlight">
            <h3>📊 数据来源</h3>
            <p><strong>本地论文：</strong> {local_paper_count}篇技术研究论文，涵盖热管理、光学设计、结构分析等核心领域</p>
            <p><strong>网络资源：</strong> 整合最新的TMT项目进展、官方公告、和科学文献信息</p>
            <p><strong>分析方法：</strong> AI驱动的综合分析，结合多源信息进行深度合成</p>
        </div>

        <h2>综合分析内容</h2>
        <p>本综述基于GPT-Researcher AI系统对本地论文和网络资源的综合分析生成，包含以下主要内容：</p>

        <h3>1. 项目当前状态</h3>
        <p>TMT项目的最新进展、时间表和挑战</p>

        <h3>2. 技术规格与能力</h3>
        <p>详细的技术参数、性能指标和科学能力</p>

        <h3>3. 研究论文分析</h3>
        <p>对{local_paper_count}篇本地论文在项目背景下的深入分析</p>

        <h3>4. 技术挑战与解决方案</h3>
        <p>当前遇到的技术难题和应对策略</p>

        <h3>5. 未来发展展望</h3>
        <p>项目前景、科学研究价值和长期影响</p>

        <div class="highlight">
            <h3>🔬 分析特点</h3>
            <ul>
                <li><strong>多源整合：</strong> 结合本地研究论文与网络最新信息</li>
                <li><strong>技术深度：</strong> 详细的技术参数和性能分析</li>
                <li><strong>项目上下文：</strong> 将研究论文置于TMT项目整体框架中</li>
                <li><strong>前瞻性展望：</strong> 探讨未来发展方向和机遇</li>
            </ul>
        </div>

        <h2>完整报告</h2>
        <p>完整的综合分析报告已保存为Markdown格式文件。如需查看详细内容，请参考项目目录中的综合报告文件。</p>

        <div style="text-align: center; margin: 40px 0; padding: 20px; background: #f8f9fa; border-radius: 5px;">
            <h3>📄 完整报告文件</h3>
            <p><code>tmt_comprehensive_review.md</code></p>
            <p>包含完整的综合分析、所有参考文献和技术细节</p>
        </div>

    </div>
</body>
</html>"""

    # Save HTML file
    html_file = "tmt_comprehensive_review_chinese.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ 中文HTML综合综述已生成: {html_file}")

if __name__ == "__main__":
    asyncio.run(generate_comprehensive_review())
