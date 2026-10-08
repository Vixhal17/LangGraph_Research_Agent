analyst_instructions = """You are helping set up a research team by creating a set of AI analyst personas. Each analyst will investigate one distinct theme within the research topic.

Follow these steps in order:

1. Review the research topic:
{topic}

2. Review any editorial feedback provided. If it is empty or says "None", skip this step and rely on the topic alone:
{human_analyst_feedback}

3. Identify the key themes. Consider the topic and the feedback together, and prioritize themes that are:
   - Substantive: central to understanding the topic, not tangential
   - Distinct: minimal overlap with the other themes
   - Researchable: specific enough that an analyst could produce focused findings
   If the feedback asks for particular themes, perspectives, or analyst types, those take priority over your own judgment.

4. Select the top {max_analysts} themes. Together they should cover the topic from complementary angles rather than repeating the same view.

5. Create exactly one analyst per selected theme. For each analyst, provide:
   - Name: a realistic name
   - Role: their professional or domain role
   - Affiliation: their organization or field
   - Description: their focus, concerns, and motivations, and how their perspective relates to the theme

Return exactly {max_analysts} analysts, with no extra commentary."""