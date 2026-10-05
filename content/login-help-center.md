---
title: Designing for Problems, Not Pages: Login.gov Support
short: Login.gov Help Center
slug: login-help-center
years: 2024–2025
order: 1
featured: true
tags: Product, Content, Research
hero: CDN/68dc3f61e93b92e3999704df_login-5.svg
card: CDN/68dc3f61e93b92e3999704df_login-5.svg
summary: Redesigning the Login.gov Help Center and phone support around the problems people actually have, so they get unstuck without waiting on an agent.
role: Lead designer for interaction, content and prototyping
team: Team Annie, Login.gov, with researcher Shqiponja Hoxha Ocumarez and the Login.gov Contact Center
teaser: Calls resolved by the phone system rose from 55% to 83%, and misdirected cases fell from 44% to 21%.
stats: 10 of 12 | participants did better with the new prototypes ;; 55% → 83% | calls resolved by the IVR ;; 44% → 21% | misdirected cases
---

## Background

In late 2024, I joined Team Annie at Login.gov with the goal of redesigning the Login.gov Help Center. At the time, user satisfaction with help articles was low (averaging 48%), leading to an increased burden on the contact center team due to a higher volume of calls.

## My Role

I led the overhaul of the Help Center, leading the interaction, content, and prototyping efforts. This initiative aimed to improve support for users struggling with authentication and identity verification. I collaborated with our researcher, Shqiponja Hoxha Ocumarez, to conduct usability testing.

## The Challenge

Prior internal research indicated structural issues within the Login.gov Help Center. A tree-testing study conducted by the team revealed that users frequently struggled to locate information for common account and identity-related issues, even when the correct content existed.

The study showed a low overall success rate and repeated patterns of users navigating to the “right” section initially, then stepping back after encountering unclear labels or ambiguous article groupings. This suggested a mismatch between how the Help Center was organized and how users framed their problems.

> The study reported an overall task success rate of roughly one-third, indicating that most users could not confidently predict where to find help.
> — Shqiponja Hoxha Ocumarez, User Researcher

These findings established that the core challenge was not content coverage, but information architecture, labeling, and navigation that failed to align with users’ problem-first mental models.

![Tree-test results diagram](CDN/697038e4799e6f411a34ec12_Screenshot%202026-01-20%20at%2021.23.09.png "Most users failed to find the correct help section for ID card upload issues.")

### How might we ensure Login.gov users can easily and quickly get the right information to successfully complete tasks without needing additional support?

Here's why it matters:

- Login.gov is a critical gateway to government services. Any delay in access can cause profound damage to people's lives.
- Users have varying levels of technical familiarity. Relevant troubleshooting guidance should be straightforward and easy to find.
- Existing help articles were not effectively meeting user needs, reflected by a user satisfaction rate of only 48%.

![Help article satisfaction statistics](CDN/68dc446ba6e824b6ecb66ffb_login-help-stats.png)

### The Help Center of 2024

The Help Center's design remained unchanged since its 2021 launch, with additions only to help articles. The video below illustrates the issues users would face when coming to the original help center:

- Users have to navigate five main categories to locate their specific topic.
- If they select the wrong topic or article, they would have to scan through the less prominent right-side navigation.
- Once they're in an article, they often have to scroll through long pages of content before finding relevant troubleshooting information.

@video 68dc9298a7d6185ab8781f59_login-help-OG-transcode.mp4 68dc9298a7d6185ab8781f59_login-help-OG-poster-00001.jpg

## Comparative Analysis

To generate some initial ideas, I performed a comparative analysis to identify common design and content approaches across a range of industry-leading help centers.

This included Google, Apple, PayPal, ID.me, Microsoft, Amazon, FedEx, Wealthfront, Dyson, and Samsung. Below are some best practices I identified in my analysis.

#### 1. Popular questions and FAQs are displayed upfront

![Examples of help centers featuring popular topics](CDN/68dd29f36bb52091f8de2bae_login-comp-analysis-1.png)

9/10 help sites featured popular issues or FAQs prominently at the top of the page. 5/10 framed these as “Popular topics”, “FAQ”, “Common questions”, or “Trending Topics”.

#### 2. Question-based article titles over technical titles

![Examples of question-based article titles](CDN/68dd2a0423f045de4b4e4565_login-comp-analysis-3.png)

7/10 help sites framed user issues through first-person questions like "What do I do if..." or "I can't sign in..."

The original Login.gov help center used second-person language like "Add or change your authentication method" or impersonal titles like "Help with agencies".

#### 3. Progressive disclosure reduced cognitive overload

![Examples of accordions and step-by-step troubleshooting](CDN/68dd2a131ea51bfdbb0179c7_login-comp-analysis-4.png)

6/10 help sites utilized the principle of progressive disclosure through collapsible accordions or paginated, step-by-step processes to diagnose user issues.

This makes it easier for users to process information and make decisions to find solutions on their troubleshooting journey.

#### 4. Left side navigation was standard

![Examples of left side navigation in help articles](CDN/68dd2a22d2bbd91f1dbb6304_login-comp-analysis-5.png)

8/10 help sites featured a persistent left side navigation or related articles section within the context of a help article.

It was doubly important that we switched over to a left side navigation since it was a U.S. Web Design System standard.

## Designing Prototype B

Using Figma, I designed this prototype to prioritize speed and scannability by highlighting the most likely issues on the landing page, nesting detailed information within accordions, and creating navigation subsection links.

**Popular topics on the landing page:** By using first-person question framing, the user should have an easier time finding the specific help article related to their issue.

@video 68dd31fcfd81419560bd6e8d_login-help-b-accordion-1-transcode.mp4 68dd31fcfd81419560bd6e8d_login-help-b-accordion-1-poster-00001.jpg

**Accordions contain additional detailed information:** Longer help articles could be broken up into smaller sections using accordions to help with scanning.

@video 68dd3748730d8d1cb0deb606_login-help-b-ID-transcode.mp4 68dd3748730d8d1cb0deb606_login-help-b-ID-poster-00001.jpg

**Left side navigation with anchor links to subsections:** Users can easily scan and quickly navigate to the relevant section of the article by clicking on the subsection titles in the navigation.

@video 68dd3bd5c0687ba565cfd028_login-help-b-nav-transcode.mp4 68dd3bd5c0687ba565cfd028_login-help-b-nav-poster-00001.jpg

## Designing Prototype C

This design emphasized granularity by segmenting troubleshooting into a step-by-step diagnostic process. Users would be asked a series of questions and be given simple instructions before being taken to a longer form help article.

This approach was inspired by Dyson and Amazon's conversational approach to troubleshooting, segmenting information to make it less overwhelming for users.

@video 68dd3c299c3e8b0f80149d36_login-help-c_mp4.mp4 68dd3c299c3e8b0f80149d36_login-help-c_poster.0000000.jpg

## Testing Scenarios

We conducted a remote moderated A/B/C usability test with 12 participants on desktops, comparing the existing help center (A) against the two prototypes (B and C). Participants were split into four groups: A/B, B/A, A/C, and C/A. This was done to reduce potential recency bias.

We walked participants through two tasks:

![Task 1 illustration](CDN/6971a0cb8a3ffbfef0e97f4d_login-help-task-1.svg)

#### Task 1: Authentication

You are trying to sign in and authenticate to access healthcare benefits for the first time. You are having issues authenticating with your iCloud account for face or touch unlock so you go to the Help Center to solve your issue.

![Task 2 illustration](CDN/6971a223aaba75a1d7816a3a_login-help-task-2.svg)

#### Task 2: Identity Verification

You are trying to verify your identity with the Trusted Traveler Program to get TSA PreCheck. You are having issues taking photos of your ID so you go to the Help Center to solve your issue.

## Usability Testing Findings

10 out of 12 participants were more successful with either Prototype B or C over the current live help site. They experienced quicker task resolution and improved ease of use as evidenced by the findings below.

> It was easier. You're taking me through the steps to solve my problem instead of leaving me to figure it out.

#### Finding #1: Framing articles from the perspective of the user improved clarity and speed

> I feel like I’m on the right page because I see that this is my question.

![Finding 1 comparison](CDN/68dd3e4cb57015e3041f3988_login-help-finding-1.svg)

Problem-focused, natural language article titles (e.g., "I'm having trouble with face or touch unlock") improved solution-finding success compared to technical terms ("Authentication method issues").

Prototype B, which framed article titles from the user's perspective, helped 5 out of 6 participants identify relevant help content faster and more accurately.

#### Finding #2: Accordion layouts improved scannability

> I like the ability to collapse... looking through 5 or 6 dropdowns makes it easier. Long pages are overwhelming—I just scroll and hope something jumps out.

![Finding 2 comparison](CDN/68dd3ec8cd353d5a03ff2ede_login-help-finding-2.svg)

Excessive page length overloaded users, hindered self-service and increased support reliance.

10 of 12 participants found the current long articles on the live help center overwhelming. Breaking content into collapsible accordions in Prototype B reduced cognitive overload, allowing participants to quickly find solutions without scanning the full article.

#### Finding #3: Users wanted step-by-step troubleshooting, not just definitions

> What action do I take if I’m having trouble logging in? It just says what it is, not how to fix it.

![Finding 3 comparison](CDN/68dd3ed54e118d1093771553_login-help-finding-3.svg)

Participants would mistakenly land on definitional articles or get lost in paragraphs of irrelevant content before finding troubleshooting info.

Prototype C was more effective, with 5 out of 6 participants locating the correct help content faster and feeling more confident, compared to the live site. This was achieved by distinguishing troubleshooting pages and modules from purely informational content.

#### Finding #4: Left side navigation matched user expectations

> It seems funny that all of these topics are on the right side. I’m used to seeing them on the left.

5 out of 12 participants missed the right-side navigation on the live site until we prompted them to use it. They overlooked links to relevant articles and consequently took longer to find their solution.

All 6 participants who used Prototype B used the left-side navigation unprompted and found solutions quicker using parent links to switch articles and child links to navigate within an article. By moving the navigation left and upgrading its links we aligned with user mental models, web conventions, and the USWDS design system.

#### Finding #5: Visual aids increased comprehension

> The green ‘do’ and red ‘don’t’ made it super obvious what to do.

![Do and don't ID photo examples](CDN/6971980b2733f3f15d4d97c5_login-id.png)

Participants preferred the "Do" or "Don't" labeling of images in the prototypes since it made it abundantly clear how to solve their ID verification issue. In addition, visual communication is especially helpful for users with limited English or digital literacy.

## Outcomes & Impact

After the usability study, the team decided to implement Prototype B's design due to the following factors:

- **Clearer navigability:** by presenting issues as first-person questions and nesting granular content within accordions, we reduced scrolling and allowed participants to locate their solution more quickly.
- **Easier troubleshooting:** participants could follow simple numbered steps punctuated by illustrations and relevant links to more quickly solve their issue.
- **Faster implementation:** since Prototype B preserved most of the existing Help Center structure while adding improvements, it offered a solution that could be immediately moved into design and development.

This redesign let me lead deeply across content strategy, interaction design, and user research. Our comparative analysis and usability testing enabled us to make targeted improvements that helped users get to their answers faster, feel more confident, and reduce the burden on support teams.

# Extending from Web to Phone Support

As part of the Help Center redesign, I examined the broader Login.gov support ecosystem, including self-service content, interactive voice response (IVR), and live agents. These channels function as a single service, but were optimized independently.

Login.gov Contact Center data revealed that nearly half of incoming calls bypassed automated support and required live agents. This created failure demand: situations where users reached human support not because their issue was complex, but because earlier service touchpoints failed to guide them correctly.

We collaborated with the Login.gov Contact Center to test whether aligning the IVR to the new Help Center's user problem framing and progressive disclosure principles could rebalance the service.

## Issues with the Original IVR

To begin, we called the Login.gov Contact Center and listened to the IVR to put ourselves in the shoes of a user looking for help. Each of us took notes on our experience and found overlapping problem areas to highlight.

The first major issue we noted was the long-winded intro and outro disclaimers. The intro took nearly 30 seconds to get through before the caller was given the list of help topics to choose from. If we could shave off unnecessary content from these disclaimers we could get callers to their solution quicker.

![Original IVR intro flow](CDN/698e2a0ba735aca13e215c1f_login-help-IVR-1-a.svg)

We pulled data from the Contact Center that showed that the popularity of topics did not reflect the order in which they were listed.

- Identity verification was the most popular topic, yet it was listed second.
- Third was Security & Privacy information, which, being an informational topic, needed less priority as people were more likely to call for troubleshooting.
- Fraud activity had the smallest amount of engagement yet it sat high as the fourth topic listed, before more relevant partner topics like the Social Security Administration (SSA) or Office of Personnel Management (OPM).

![Contact Center topic data](CDN/698e1d5b86522916075bb3f4_login-help-IVR-data.png)

The original IVR's help topic structure (shown below) reflected internal categorizations and was not ordered by the popularity of user-reported issues. As a result, callers had to listen through irrelevant topics and frequently selected incorrect paths, increasing misdirected cases and agent workload.

![Original IVR topic structure](CDN/698e2a0cb3cafb4d3a53471f_login-help-IVR-1-b.svg)

## Applying Data & New Design Principles

Using the data we gathered from the Contact Center, we outlined a new information structure that reflected topic popularity, and nested more granular troubleshooting options into subtopics, much like we had in the new Help Center.

We also made the intro disclaimer as concise as we possibly could and included a last attempt to get users back to the Help Center for self-service support like changing their password or updating their email address.

![Redesigned IVR intro flow](CDN/698e307527065e99122e3b52_login-help-IVR-2-a.svg)

To make the IVR even more robust, we added additional subtopic options with troubleshooting content sourced directly from our new Help Center articles. This gives callers a potential solution to their problem before having to speak with an agent.

![Redesigned IVR topic structure](CDN/698e2a0b2ce3897b4b8933b4_login-help-IVR-2-b.svg)

## Phone Support Outcomes

Following a week-long sprint of UX workshops with researchers and support staff to redesign the phone tree, we reduced IVR options from 8 down to the 5 most frequent issues with nested subtopics (much like in the new Help Center).

After implementation, the percentage of calls handled by the IVR increased from 55% to 83%, while misdirected cases dropped from 44% to 21%, reducing call volume and allowing agents to focus on more complex, high-touch support needs.
