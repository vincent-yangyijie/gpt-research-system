#!/usr/bin/env python3
"""
Test script for GPT-Researcher with multiple LLM providers
"""

import os
import asyncio
from dotenv import load_dotenv
from gpt_researcher import GPTResearcher

# Load environment variables
load_dotenv()

def get_available_providers():
    """Check which API keys are available"""
    providers = []

    if os.getenv("GOOGLE_API_KEY"):
        providers.append(("google", "gemini-2.0-flash-exp"))
    if os.getenv("KIMI_API_KEY"):
        providers.append(("openai", "moonshot-v1-8k"))  # KIMI uses OpenAI-compatible API
    if os.getenv("OPENAI_API_KEY"):
        providers.append(("openai", "gpt-4o-mini"))

    return providers

async def test_provider(provider_name, model_name, query):
    """Test a specific LLM provider"""
    try:
        print(f"🔍 Testing {provider_name.upper()} with {model_name}...")
        print(f"Query: {query}")
        print("-" * 60)

        # Set environment variable for the provider
        if provider_name == "google":
            os.environ["OPENAI_API_KEY"] = os.getenv("GOOGLE_API_KEY")
        elif provider_name == "openai" and model_name.startswith("moonshot"):
            os.environ["OPENAI_API_KEY"] = os.getenv("KIMI_API_KEY")
        # For regular OpenAI, it should already be set

        # Create a researcher instance with specific model
        researcher = GPTResearcher(
            query=query,
            report_type="research_report",
            report_format="markdown",
            model=model_name if provider_name == "google" else None
        )

        # Conduct research
        print("📊 Conducting research...")
        await researcher.conduct_research()

        # Write the report
        print("✍️  Generating report...")
        report = await researcher.write_report()

        print(f"\n{'='*60}")
        print(f"RESEARCH REPORT ({provider_name.upper()} - {model_name})")
        print(f"{'='*60}")
        print(report)
        print(f"{'='*60}")

        return True

    except Exception as e:
        print(f"❌ Error with {provider_name} {model_name}: {str(e)}")
        return False

async def main():
    providers = get_available_providers()

    if not providers:
        print("❌ Error: No API keys found!")
        print("Please set at least one of the following environment variables:")
        print("- GOOGLE_API_KEY (for Gemini)")
        print("- KIMI_API_KEY (for Moonshot AI)")
        print("- OPENAI_API_KEY (for OpenAI)")
        print("\nCopy .env.example to .env and add your keys.")
        return

    print(f"🤖 Found {len(providers)} available LLM provider(s):")
    for provider, model in providers:
        print(f"  - {provider.upper()}: {model}")
    print()

    query = "What are the latest developments in AI research?"

    # Test each provider
    for provider_name, model_name in providers:
        success = await test_provider(provider_name, model_name, query)
        if success:
            print(f"✅ {provider_name.upper()} test completed successfully!\n")
        else:
            print(f"❌ {provider_name.upper()} test failed.\n")

        # Add a small delay between tests
        if len(providers) > 1:
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
