#!/usr/bin/env python3
"""
Simple test for GPT-Researcher with Gemini
"""

import os
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure GPT-Researcher with specified LLM setup
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("KIMI_API_KEY")  # For KIMI (OpenAI-compatible)
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")  # For web search

# LLM Configuration as specified
os.environ["FAST_LLM"] = "google_genai:gemini-2.0-flash-exp"  # Gemini 2.0 Flash
os.environ["SMART_LLM"] = "kimi:kimi-k2"  # KIMI k2
os.environ["EMBEDDING"] = "openai:text-embedding-3-small"

try:
    from gpt_researcher import GPTResearcher

    async def main():
        print("🔍 Testing GPT-Researcher with Gemini...")
        print("API Key loaded:", "Yes" if os.getenv("GOOGLE_API_KEY") else "No")
        print("FAST_LLM:", os.getenv("FAST_LLM"))
        print("SMART_LLM:", os.getenv("SMART_LLM"))

        # Create researcher with minimal config
        researcher = GPTResearcher(
            query="What is artificial intelligence?",
            report_type="research_report"
        )

        print("📊 Conducting research...")
        await researcher.conduct_research()

        print("✍️  Generating report...")
        report = await researcher.write_report()

        print("\n" + "="*50)
        print("REPORT")
        print("="*50)
        print(report)

    if __name__ == "__main__":
        asyncio.run(main())

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
