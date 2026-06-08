# Project Planning

The project planning was not a static pre-defined roadmap, but an evolving structure that was continuously updated based on stakeholder input, technical findings, and limitations discovered during analysis. Although an initial plan was established at the start of the project, most meaningful planning decisions were made iteratively as understanding of the dataset and system deepened.

To reflect this, the planning process can be divided into distinct phases aligned with weekly progression.

---

## Weeks 1–2: Team formation and initial project framing

The first phase focused on setting up the team and establishing the initial scope of the project. During this stage, the Canon project was selected as the team assignment based on its perceived complexity and relevance to data-driven modelling.

Initial planning activities were primarily organisational rather than technical. The team defined basic working agreements, communication expectations, and individual responsibility awareness. A shared repository was established, alongside version control conventions and a preliminary Project Development Plan (PDP).

At this stage, the project was still framed in broad terms: the objective was understood as analysing Canon’s dataset to derive insights and potentially build a predictive model. However, the technical constraints and structure of the dataset were not yet known, meaning that planning remained high-level and assumption-driven.

---

## Week 3: Stakeholder alignment and early structure definition

Once initial contact with Canon stakeholders was established, planning shifted toward alignment with external expectations. A structured communication rhythm was defined, including weekly meetings with Canon representatives.

At this stage, planning became more grounded. The dataset was introduced, and initial exploratory work was planned as the first technical phase of the project. The focus was placed on understanding data structure, expected outputs, and business context.

The Project Plan was drafted during this period, defining:

* high-level project phases (exploration → analysis → modelling → evaluation)
* initial assumptions about deliverables
* preliminary timeline expectations
* early identification of risks related to data complexity

---

## Week 4: Transition to structured experimentation

With initial dataset access and early exploration, planning shifted from conceptual structuring to execution planning. A more concrete workflow was introduced, including:

* structured data exploration tasks
* definition of a data dictionary to formalise feature meanings
* introduction of a sprint-like weekly cycle with retrospectives
* setup of a GitHub Project Board for task tracking

At this stage, planning became more operational. Instead of defining only phases, the team began planning specific weekly outputs such as exploratory notebooks, documentation updates, and early hypothesis formation.

Importantly, this is also when the planning process started to incorporate feedback loops. Retrospectives were used to adjust upcoming weekly goals, making planning explicitly adaptive.

---

## Week 5: Formalisation of methodology and scope control

During this phase, planning focused on consolidating the project structure and ensuring that scope remained manageable. Multiple versions of the project plan were merged into a single coherent methodology.

Planning activities included:

* defining preprocessing strategy at a high level
* outlining expected modelling approaches (initially still open-ended)
* refining timeline feasibility based on team capacity
* clarifying dataset exploration priorities before modelling attempts

A key planning insight during this phase was that implementation without a stable understanding of the dataset structure would likely lead to inefficient or incorrect modelling decisions. As a result, planning explicitly prioritised structured exploration over premature model development.

---

## Week 6: Partial capacity and continuity planning

During a period of reduced availability (medical leave), planning shifted toward continuity management. The focus was on maintaining alignment with the project despite limited technical contribution.

This required:

* prioritisation of high-impact tasks (finalising project plan)
* delegation of technical responsibilities within the team
* ensuring documentation remained consistent and usable
* maintaining awareness of overall project direction through meetings

---

## Week 7: Re-integration and workflow restructuring

After returning to active participation, planning was adjusted to reflect both team progress and existing workflow inefficiencies.

Key planning developments included:

* re-establishing personal task ownership within the dataset exploration phase
* identifying gaps in team workflow and communication structure
* planning intervention via skills coach to improve collaboration
* reassessing individual contribution areas based on project status

---

## Weeks 8–9: Analytical direction shift and problem redefinition

At this stage, planning began to diverge from the initial expectation of straightforward modelling. Early analytical findings revealed inconsistencies in data structure and limitations in aggregation assumptions.

This led to a revised planning direction:

* focus shifted toward validating data consistency before modelling
* additional exploratory analysis of noise and variance structure was planned
* introduction of spatial interpretation of the dataset (chip/nozzle structure)
* reconsideration of whether the problem should be treated as purely statistical

Planning here became more investigative than procedural.

---

## Week 10–11: Data engineering and modelling preparation

Once structural understanding improved, planning shifted toward formal preparation for modelling.

This included:

* defining aggregation strategy for repeated measurements
* implementing a reproducible data reduction pipeline
* planning feature encoding strategy (OHE, scaling decisions, structural retention of spatial variables)
* evaluating suitability of dimensionality reduction techniques (PCA planning and interpretation)

At this stage, planning became more technically precise, focusing on how to transform raw data into a modelling-ready dataset while preserving meaningful structure.

However, PCA results introduced a major planning correction: the feature space was not suitable for standard reduction techniques due to dominance of a single variable (`dt2`). This forced a re-evaluation of subsequent modelling plans.

---

## Week 12–14: Structural redefinition and model strategy exploration

The final phase of planning moved beyond traditional pipeline design and into system-level modelling strategy.

Key planning directions included:

* treating `V` and `F_r` as a coupled system rather than independent variables
* identifying `HeadIdx#` as a spatial variable rather than categorical noise
* incorporating chip-level missing data patterns into modelling assumptions
* evaluating spatially aware modelling approaches
* introducing the idea of a continuous response field representation of the printer system
* exploring physics-informed and spatial kernel-based modelling approaches

At this stage, planning became increasingly conceptual. Instead of deciding “what to implement next,” planning focused on how the system should be mathematically represented before implementation could even be meaningfully defined.

---

## Overall Summary of Planning Evolution

Across the project, planning evolved through four distinct modes:

1. **Initial structuring** – defining team workflow and broad objectives
2. **Operational planning** – weekly task breakdown and data exploration cycles
3. **Adaptive planning** – iterative adjustment based on findings and retrospectives
4. **Formulation-level planning** – redefining the problem based on system understanding

The planning process functioned as a feedback-driven system, where each analytical insight directly influenced future direction. This was especially important given the complexity of the dataset and the dependence of modelling decisions on physical interpretation of the underlying printing system.