# Evidence

---

## Activity 1 – Project Initiation, Planning and Stakeholder Alignment

This activity covers the early phase of the project where the team was formed, initial structure was defined, and alignment with Canon stakeholders was established. The focus was on understanding the project scope, defining communication channels, and producing the first formal project documentation.

* **Week 1 – Project selection and team formation**
  No formal artefacts were produced during this stage, but the decision to select the Canon project reflects early-stage organisational planning and team alignment.
  Evidence: [Week 1 Log](weekly-logs/2026-02-11-week1.md)

* **Week 2 – Stakeholder setup and team structuring**
  Establishment of communication with Canon representatives and initial team agreements. This phase focused on defining expectations and preparing for structured collaboration.
  Evidence: [Week 2 Log](weekly-logs/2026-02-25-week2.md)

* **Week 3 – Project Plan and initial dataset introduction**
  The first formal planning document was created after stakeholder clarification. Early dataset access enabled the transition from planning to exploratory preparation.
  Evidence:

  * [Project Plan](evidence/2026-03-09-project-plan.md)
  * [Week 3 Log](weekly-logs/2026-03-05-week3.md)

* **Week 4 – Structuring workflow and domain understanding**
  Creation of a data dictionary and GitHub Project Board introduced structured workflow management. Initial dataset exploration began, grounding the project in real data.
  Evidence:

  * [Data Dictionary](evidence/2026-03-11-data-dictionary.md)
  * [GitHub Project Board](https://github.com/orgs/FontysVenlo/projects/787)
  * [Initial Dataset Exploration](evidence/2026-03-16-initial-data-exploration.md)
  * [Retrospective](evidence/2026-03-11-retrospective1.md)

---

## Activity 2 – Data Analysis and Investigation

This activity includes all analytical work performed to understand the dataset, identify structural patterns, and validate assumptions before modelling. It covers exploratory analysis, feature interpretation, spatial reasoning, and noise investigation.

* **Week 8 – Noise structure analysis**
  Investigation into variance structure across repeated measurements. The work identified inconsistencies in grouping completeness and motivated further data validation.
  Evidence: [Noise Threshold Calculation Notebook](evidence/notebooks/4-EDA-noise.pdf)

* **Week 9 – Spatial layout exploration**
  Visual analysis of the printer’s physical structure, mapping logical data features to hardware layout. This revealed spatial patterns in missing data across chip indices.
  Evidence: [Physical Layout Exploration Notebook](evidence/notebooks/4.5-EDA-physical-layout.pdf)

* **Week 10 – Data reduction and aggregation validation**
  Construction of a Polars-based pipeline to collapse repeated measurements into structured datasets. This ensured consistent aggregation across parameter combinations.
  Evidence: [Dataset Reduction Notebook](evidence/notebooks/5-dataset-reduction.pdf)

* **Week 11 – Feature space and model readiness analysis**
  Preprocessing design and PCA evaluation revealed that the feature space is dominated by a single variable (`dt2`), significantly influencing modelling strategy.
  Evidence: [Core Model Exploration Notebook](evidence/notebooks/6-core-model.pdf)

* **Week 12 – Feature-level structural investigation**
  Deep analysis of feature relationships, identifying composite relationships (`V` and `F_r`) and spatial structure in `HeadIdx#`. This redefined the dataset as a spatial system rather than independent variables.
  Evidence:

  * [Feature Analysis](../evidence/notebooks/1.5-feature-analysis.pdf)
  * [Spatial Autoregressive Models Notes](spatial-autoregressive-models.md)

---

## Activity 3 – System Modelling and Conceptual Design

This activity covers the transition from data analysis to system-level modelling thinking. It includes mathematical formulation attempts, spatial modelling considerations, and abstraction of the printer system into a formal function.

* **Week 13 – Initial system formulation**
  Development of a first mathematical function describing the printer response system. The work also included research into spatial modelling approaches and team-level reflection on collaboration structure.
  Evidence:

  * [First Function Definition](evidence/physical-notes/1-function-definition.pdf)
  * [Spatial Modelling Research](notes/research/spatial-autoregressive-models)

* **Week 14 – Continuous system formulation and field-based modelling**
  Extension of the system definition into a continuous spatial response field. This introduced the idea of modelling nozzle behaviour using spatial kernels instead of discrete independent outputs.
  Evidence:

  * [Dimensionality Definition](evidence/physical-notes/2-dimensionality-definition.pdf)
  * [Function Definition (digital)](evidence/function-definition)
  * [System Definition Summary](notes/system-definition-summary.md)
  * [Physics-Informed Neural Networks Research](notes/research/physics-informed-neural-networks.md)

---

## Skill Area 1 – Future-Oriented Organisation

This skill area covers planning, structuring, and adapting the project over time in response to evolving insights and constraints.

Evidence:

* [Project Plan](evidence/2026-03-09-project-plan.md) – initial project structuring and phase definition
* [GitHub Project Board](https://github.com/orgs/FontysVenlo/projects/787) – sprint-style task organisation
* [Week 4 Retrospective](evidence/2026-03-11-retrospective1.md) – introduction of iterative planning cycles
* [Final Project Plan](evidence/2026-03-26-project-plan.pdf) – refined planning after stakeholder feedback and dataset access
* Weekly logs (Weeks 1–14) – continuous adaptation of planning based on technical findings

Explanation:
The planning evolved from a static initial roadmap into an adaptive system driven by data findings. Decisions such as prioritising exploratory analysis over immediate modelling demonstrate controlled adjustment of direction rather than rigid execution.

---

## Skill Area 2 – Investigative Ability

This skill area focuses on how unknown system behaviour was explored, validated, and interpreted through data analysis and research.

Evidence:

* [Noise Analysis](evidence/notebooks/4-EDA-noise.pdf) – variance structure and measurement consistency investigation
* [Physical Layout Analysis](evidence/notebooks/4.5-EDA-physical-layout.pdf) – mapping dataset structure to hardware layout
* [Feature Analysis](../evidence/notebooks/1.5-feature-analysis.pdf) – identification of composite and spatial feature relationships
* [Core Model PCA Analysis](evidence/notebooks/6-core-model.pdf) – dimensionality investigation and feature dominance discovery
* [Spatial Autoregressive Research](spatial-autoregressive-models.md) – exploration of advanced modelling approaches

Explanation:
Investigative work progressively shifted from statistical exploration to structural interpretation of the system. The most significant outcome was the redefinition of `HeadIdx#` as a spatial variable and the recognition that the dataset represents a physical system rather than independent samples.

---

## Skill Area 3 – Personal Leadership

This skill area includes initiative-taking, responsibility management, and adaptive behaviour during uncertainty or reduced capacity.

Evidence:

* [Week 2 Log](weekly-logs/2026-02-25-week2.md) – establishment of team expectations and collaboration structure
* [Week 4 Retrospective](evidence/2026-03-11-retrospective1.md) – active contribution to workflow improvement
* [Final Project Plan](evidence/2026-03-26-project-plan.pdf) – completion and consolidation during medical leave
* [Week 7 Log](weekly-logs/2026-04-02-week7.md) – reintegration after absence and initiation of skills coach intervention

Explanation:
Leadership was demonstrated through maintaining project continuity during absence, proactively addressing team dysfunction, and ensuring structural alignment of documentation even under reduced availability.

---

## Skill Area 4 – Targeted Interaction

This skill area covers communication with stakeholders, team coordination, and structured external engagement.

Evidence:

* [Week 2 Log](weekly-logs/2026-02-25-week2.md) – initial stakeholder contact and communication setup with Canon
* [Week 3 Log](weekly-logs/2026-03-05-week3.md) – structured stakeholder meeting and requirement clarification
* [Week 6 Log](weekly-logs/2026-03-26-week6.md) – communication during reduced capacity and presentation of project plan
* [Week 13 Log](weekly-logs/2026-05-21-week13.md) – skills coach session addressing team dynamics

Explanation:
Communication evolved from formal stakeholder onboarding to active negotiation of understanding during technical uncertainty. Interaction with Canon and internal coaching sessions ensured alignment between technical development and external expectations.