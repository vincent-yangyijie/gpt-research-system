#!/usr/bin/env python3
"""
Generate a comprehensive literature review of TMT (Thirty Meter Telescope) papers
using GPT-Researcher with Gemini and KIMI LLMs.
"""

import os
import asyncio
from dotenv import load_dotenv
from gpt_researcher import GPTResearcher

# Load environment variables
load_dotenv()

def get_tmt_paper_paths():
    """Get paths to all TMT papers"""
    tmt_dir = "../TMT"  # Relative path from GPT_Research directory

    if not os.path.exists(tmt_dir):
        print(f"❌ TMT directory not found: {tmt_dir}")
        return []

    paper_paths = []
    for filename in os.listdir(tmt_dir):
        if filename.endswith('.pdf'):
            full_path = os.path.join(tmt_dir, filename)
            paper_paths.append(full_path)
            print(f"📄 Found paper: {filename}")

    print(f"\n📚 Total papers found: {len(paper_paths)}")
    return paper_paths

async def generate_tmt_literature_review():
    """Generate comprehensive literature review of TMT papers"""

    # Configure API keys
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
    os.environ["OPENAI_API_KEY"] = os.getenv("KIMI_API_KEY")
    os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

    # LLM Configuration
    os.environ["FAST_LLM"] = "google_genai:gemini-2.0-flash-exp"
    os.environ["SMART_LLM"] = "kimi:kimi-k2"
    os.environ["EMBEDDING"] = "openai:text-embedding-3-small"

    print("🔬 TMT Literature Review Generation")
    print("=" * 60)
    print("🤖 Using Gemini 2.0 Flash + KIMI k2 for analysis")
    print("📚 Analyzing TMT (Thirty Meter Telescope) research papers")
    print()

    # Get paper paths
    paper_paths = get_tmt_paper_paths()
    if not paper_paths:
        print("❌ No papers found to analyze")
        return

    # Create research query
    research_query = """
    Conduct a comprehensive literature review and analysis of the Thirty Meter Telescope (TMT) research papers provided.
    Focus on the following key areas:

    1. **TMT Design and Architecture**: Optical design, telescope structure, and system integration
    2. **Thermal Management**: Thermal modeling, stability analysis, and environmental effects
    3. **Optical Performance**: Image quality, aberrations, and performance optimization
    4. **Environmental Challenges**: Temperature effects, atmospheric conditions, and mitigation strategies
    5. **Simulation and Analysis Tools**: Modeling approaches, software tools, and validation methods
    6. **Future Developments**: Emerging technologies, improvements, and research directions

    For each paper, extract and summarize:
    - Main objectives and methodology
    - Key findings and results
    - Technical innovations or approaches
    - Limitations and future work
    - Relationships to other TMT research

    Provide a synthesis that identifies:
    - Common themes and research patterns
    - Technological gaps and challenges
    - Interdisciplinary connections
    - Recommendations for future TMT development

    Structure the review with clear sections, citations to specific papers, and comprehensive technical analysis.
    """

    try:
        print("🔍 Initializing GPT-Researcher...")
        print("FAST_LLM: Gemini 2.0 Flash")
        print("SMART_LLM: KIMI k2")
        print()

        # Create researcher with document analysis
        researcher = GPTResearcher(
            query=research_query,
            report_type="research_report",
            report_format="markdown",
            document_urls=paper_paths,  # Analyze local PDF documents
            tone="Objective"
        )

        print("📊 Conducting comprehensive literature analysis...")
        print("This may take several minutes depending on paper complexity...")

        await researcher.conduct_research()

        print("✍️  Generating literature review report...")
        report = await researcher.write_report()

        # Save the report
        output_file = "tmt_literature_review.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"\n✅ Literature review completed and saved to: {output_file}")
        print("\n" + "="*80)
        print("TMT LITERATURE REVIEW")
        print("="*80)
        print(report)
        print("="*80)

    except Exception as e:
        print(f"❌ Error during literature review generation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(generate_tmt_literature_review())
