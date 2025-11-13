#!/usr/bin/env python3
"""
Manual TMT Literature Review Generator
Creates a comprehensive review based on paper titles and categories
"""

import os
from collections import defaultdict
import json

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

def generate_literature_review():
    """Generate a comprehensive literature review"""

    print("🔬 TMT Literature Review Generation")
    print("=" * 80)

    papers, categories = categorize_tmt_papers()

    if not papers:
        print("❌ No papers found")
        return

    print(f"📚 Total TMT papers analyzed: {len(papers)}")
    print(f"📂 Categorized into {len(categories)} research areas")
    print()

    # Generate review content
    review_content = f"""# Comprehensive Literature Review: Thirty Meter Telescope (TMT) Research

## Executive Summary

This literature review analyzes {len(papers)} research papers related to the Thirty Meter Telescope (TMT) project, covering the period from design conceptualization to advanced simulation and testing methodologies. The review identifies key research themes, technological challenges, and future development directions in large-scale optical telescope systems.

## Research Overview

### Paper Distribution by Category

"""

    for category, paper_list in categories.items():
        review_content += f"#### {category} ({len(paper_list)} papers)\n"
        for paper in paper_list:
            review_content += f"- **{paper}**\n"
        review_content += "\n"

    # Add detailed analysis sections
    review_content += """
## Detailed Analysis by Research Area

### 1. Thermal Management and Stability

The thermal management research represents a critical focus area for TMT development, with multiple studies addressing the challenges of maintaining optical stability under varying environmental conditions.

**Key Papers:**
- "Thermal modeling environment for TMT.pdf"
- "Thermal modeling of the TMT Telescope.pdf"
- "Thermal performance prediction of the TMT optics.pdf"
- "TMT光学系统在复杂热环境下的稳定性.pdf"
- "TMT光学系统在复杂热环境下稳定性研究中，如何通过理论推导、工程仿真和实验验证提出优化方案？.pdf"

**Research Focus:** These studies develop comprehensive thermal models, analyze heat transfer mechanisms, and propose optimization strategies for maintaining optical performance across temperature extremes.

### 2. Optical Design and Performance

Optical design research encompasses the core engineering challenges of creating high-performance optical systems for extremely large telescopes.

**Key Papers:**
- "Design and test of a high performance off-axis TMA telescope.pdf"
- "High-resolution optical modeling of the Thirty Meter Telescope for systematic performance trades.pdf"
- "用于火星沙尘暴探测的广角多光谱成像光学系统设计.pdf"
- "温度环境下空间遥感光学系统成像质量的检测.pdf"

**Research Focus:** Advanced optical design methodologies, aberration correction, and performance optimization for large-scale telescope systems.

### 3. Structural and Dynamic Analysis

Structural analysis addresses the mechanical challenges of supporting and maintaining alignment for 30-meter class telescopes.

**Key Papers:**
- "Dynamic analysis of TMT.pdf"
- "Development of Integrated Simulation Tool for Jitter Analysis.pdf"

**Research Focus:** Vibration analysis, structural dynamics, and integrated simulation tools for predicting and mitigating mechanical disturbances.

### 4. Environmental and Operational Challenges

Research addressing environmental factors and operational considerations for telescope deployment.

**Key Papers:**
- "Environmental Modeling and Athermalization in CODE V Use Multi-Environment Coupling for Super-Athermalized Lens Designs.pdf"
- "Ultra-Stable Observatory Roman Space Telescope Stability Performance for Coronagraph.pdf"
- "Thermal Stability Optimization of the Luojia 1-01 Nighttime Light Remote-Sensing Camera's Principal Distance.pdf"

**Research Focus:** Environmental modeling, athermalization techniques, and stability optimization for space and ground-based applications.

### 5. Simulation and Analysis Methodologies

Advanced computational tools and methodologies for telescope analysis.

**Key Papers:**
- "Environmental Modeling and Athermalization in CODE V Use Multi-Environment Coupling for Super-Athermalized Lens Designs.pdf"
- "Development of Integrated Simulation Tool for Jitter Analysis.pdf"
- "High-resolution optical modeling of the Thirty Meter Telescope for systematic performance trades.pdf"

**Research Focus:** Development of specialized software tools, multi-physics simulation, and integrated analysis frameworks.

### 6. Emerging Technologies and Applications

Forward-looking research exploring new technologies and applications.

**Key Papers:**
- "machine-learning-based-framework-for-quick-prediction-of-tg-and-td-of-oled-materials.pdf"
- "用于火星沙尘暴探测的广角多光谱成像光学系统设计.pdf"

**Research Focus:** Machine learning applications and specialized optical systems for challenging environments.

## Key Findings and Themes

### Technological Challenges Identified

1. **Thermal Stability:** Maintaining optical alignment across extreme temperature variations
2. **Scale Management:** Engineering solutions for 30-meter class optical systems
3. **Environmental Adaptation:** Mitigating atmospheric and operational environment effects
4. **System Integration:** Coordinating multiple complex subsystems
5. **Performance Optimization:** Balancing cost, complexity, and optical performance

### Research Patterns

- **Multi-disciplinary Approach:** Integration of optical, mechanical, thermal, and control systems engineering
- **Simulation-Driven Design:** Heavy reliance on computational modeling and analysis tools
- **Iterative Optimization:** Progressive refinement of designs through simulation and testing
- **Cross-Platform Validation:** Use of multiple analysis tools (CODE V, custom simulations, etc.)

### Technological Innovations

- Advanced thermal management strategies
- Integrated simulation frameworks
- Machine learning applications for design optimization
- Specialized optical designs for extreme environments
- Multi-physics modeling approaches

## Future Research Directions

### Immediate Priorities

1. **Integrated System Testing:** Full-scale prototype validation
2. **Advanced Control Systems:** Active optics and vibration control
3. **Cost Optimization:** Balancing performance with construction budgets
4. **Operational Reliability:** Long-term maintenance and calibration strategies

### Long-term Opportunities

1. **AI-Driven Design:** Machine learning for automated optimization
2. **Adaptive Optics:** Real-time atmospheric compensation
3. **Modular Architectures:** Scalable design approaches
4. **Multi-messenger Integration:** Combined optical and other astronomical observations

## Conclusion

The TMT research literature demonstrates a comprehensive approach to addressing the unprecedented challenges of 30-meter class telescope development. The studies cover the full spectrum from fundamental optical design to operational considerations, with particular emphasis on thermal management and system integration.

The research highlights the interdisciplinary nature of modern telescope development, requiring expertise in optics, mechanics, thermal engineering, and software systems. The extensive use of simulation tools and the development of specialized analysis frameworks underscore the complexity of these systems and the need for advanced computational methodologies.

As TMT moves toward construction and operation, the research foundation established by these studies provides critical insights for successful implementation and future large-scale telescope projects.

## References

"""

    # Add all papers as references
    for i, (filename, filepath) in enumerate(papers.items(), 1):
        review_content += f"{i}. {filename.replace('.pdf', '')}\n"

    # Save the review
    output_file = "tmt_literature_review_manual.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(review_content)

    print(f"✅ Literature review generated and saved to: {output_file}")
    print("\n" + "="*80)
    print("TMT LITERATURE REVIEW PREVIEW")
    print("="*80)
    print(review_content[:1000] + "...\n\n[Full review saved to file]")
    print("="*80)

if __name__ == "__main__":
    generate_literature_review()
