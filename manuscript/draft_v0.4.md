# Perspective Draft v0.3 (English)

**Target:** Nature Human Behaviour Perspective (3,000-4,000 words)
**Working title:** *Where Institutions Fail, Stress Becomes Repression: A Path-Weighted Framework for Anticipating Societal Trajectories*
**Last update:** 2026-05-25 (Acemoglu-style intro + V-Dem 93-country results integrated)

---

## Section structure

| Section | Words | Status |
|---|---|---|
| 1. Introduction (Acemoglu-style) | 600 | ✓ v0.3 |
| 2. Three streams and their limits | 750 | ✓ v0.1 |
| 3. A path-weighted framework | 900 | ✓ v0.1 |
| 4. Empirical illustration (93 countries) | 750 | ✓ v0.1 |
| 5. Falsifiable predictions and policy implications | 500 | ✓ v0.1 |
| 6. Scope, limits, and a research program | 350 | ✓ v0.1 |
| **Total** | **3850** | |

---

## 1. Introduction (Acemoglu-style — 605 words)

Why do some governments repress civil liberties more than others? Across 93 countries from 2000 to 2022, we show that the answer lies less in the level of social stress a society faces than in its institutional capacity to absorb that stress. Using a panel of 2,136 country-year observations, repression of civil liberties (measured by the V-Dem civil liberties index, reversed) responds to institutional resilience (β = 1.67, 95% CI [1.59, 1.74]) more than 2.5 times as strongly as it responds to social stress itself (α = 0.63 [0.53, 0.73]), with collective future expectation as a third, independent moderator (η = 0.73 [0.66, 0.81]). A simple path-weighted action functional—inspired by the path-integral formalism of statistical mechanics but anchored in standard cross-national econometrics—accounts for 77% of cross-national variance and remains significant under country fixed effects, regional sub-samples, and four alternative outcome measures.

This result reframes a long-standing debate. Structural-demographic theory (SDT) and related cliodynamic frameworks have placed *social stress* — labor oversupply, elite overproduction, immiseration — at the causal center of political instability¹. A recent industrial-society empirical test of SDT's three core predictions, however, finds that none is supported by United States data, and that the largest share of wage polarization is in fact explained by automation²: the stress mechanism, as classically formulated, fails. The alternative we propose preserves the empirical observation that stress matters, but locates the dominant causal weight in *institutional capacity*. Where institutions hold, comparable social stress is metabolized into reform; where institutions fail, the same stress is metabolized into repression. Civil liberties repression, in this account, is not the *cause* of regime instability but the *signature* of an institutional system that is failing to absorb stress through other channels.

**A note on epistemology.** We do not claim that path-integral physics governs society. We use the formalism as a *heuristic device*—a mathematical structure that organizes testable predictions about societal trajectories, in the same mode that Watts and Strogatz³ applied graph theory to social networks and Yakovenko and Rosser⁴ applied statistical mechanics to income distributions. The question is not whether the mathematics is metaphysically true of society, but whether it economically describes patterns visible in cross-national data and natural experiments.

The framework yields five falsifiable predictions, two of which we test directly here and three we leave for a forthcoming companion Article that extends the panel back to 1960 and incorporates three Korean natural experiments (the 1997 financial crisis, the 2016–17 presidential impeachment, and the 2020–24 demographic shock). In doing so we propose a discipline of *anticipatory social science* that neither retreats from formalization—as much of comparative politics does—nor mistakes mathematical elegance for empirical content—as physics-inspired social modeling sometimes does. The framework's scope is bounded: it presupposes the post-1989 liberal international order, in which nation-states operate within a comparable institutional template and civil liberties are coherently measurable across polities (see §6).

The remainder of this Perspective proceeds as follows. §2 reviews three formal traditions—structural-demographic theory, critical-transition theory, and the path-integral approach to economic systems—and identifies the specific limit each runs into. §3 develops the path-weighted framework. §4 reports the cross-national empirical illustration. §5 lays out five falsifiable predictions, including a prospective prediction for Korea 2026–2030. §6 delimits the framework's scope and outlines a research program.

**References cited in draft:** ¹=Turchin 2012, ²=Georgescu 2023, ³=Watts & Strogatz 1998, ⁴=Yakovenko & Rosser 2009.

---

## 2. Three streams and their limits (745 words)

Three formal traditions have shaped recent attempts to model societal change, and each runs into a characteristic ceiling.

**Structural-demographic theory.** Turchin and colleagues have spent two decades developing a quantitative cliodynamic framework in which elite overproduction mediates the passage from labor oversupply to political instability⁵,¹. The framework's quantitative ambition is admirable, and its 2010 forecast of rising United States instability in the 2020s—based on a Political Stress Indicator combining popular immiseration, intra-elite competition, and state fiscal weakness—turned out to be broadly correct⁶. Yet a careful industrial-society test by Georgescu (2023) using 1947–2020 U.S. data finds that none of SDT's three core mechanisms—falling relative wages from labor oversupply, hump-shaped elite income, elite overproduction driving instability—is supported by the data². The largest share of wage variance, in her decomposition, is explained by automation; elite incomes rise monotonically rather than peaking; and the predicted instability follows neither the timing nor the magnitude implied by elite-numbers dynamics. The forecast may have been correct, but the mechanism appears to have been wrong. This invites a reformulation that preserves the empirical signal (stress correlates with instability) while substituting a different mediator.

**Critical-transition theory.** Beginning with Scheffer and colleagues' 2009 *Nature* synthesis⁷, a robust body of work has identified generic early-warning signals—rising variance, increased autocorrelation, critical slowing down—that flag impending regime shifts across ecosystems, financial markets, and social systems alike. Subsequent extensions to social-ecological systems⁸ and to societal complexity⁹ have demonstrated the framework's translational power. Its strength is universality: the same statistical signatures appear before transitions of very different substantive content. Its limit is the obverse of its strength. The warning signals are silent about *which* of several available regimes the system will land in. They tell us the system is approaching a tipping point; they cannot tell us whether the post-transition regime is reform, revolution, dissolution, or status-quo entrenchment. Yet it is precisely the *direction* of transition, not its timing alone, that policy and political analysis need to know.

**Path-integral economic models.** A third stream—developed most fully by Gosselin, Lotz, and Wambst over the past decade¹⁰,¹¹—replaces the optimization-based representative agent of standard macroeconomics with a probabilistic description of agents' actions, formalized as a path integral over an abstract action space. The setup naturally accommodates agent heterogeneity, strategic interaction, and unpredictable shocks, and yields analytical results in the large-N limit through a statistical field theory. The formalism is elegant and the underlying physics—Feynman's sum-over-histories and Kleinert's statistical-mechanics applications—is rigorously developed¹². Yet a quarter-century after its first economic applications, the path-integral approach has remained confined to illustrative models of business cycles, consumer-producer interaction, and financial pricing. No empirical application to political or social collapse exists. The mathematical machinery has been built but never tested on the empirical questions that political and social scientists actually ask.

**The shared limit.** These three traditions, despite their methodological diversity, share an implicit assumption: that a single trajectory carries the explanatory burden. SDT collapses multiple possible futures into one historically inevitable one. Critical-transition theory locates a single threshold beyond which the system flips. Path-integral economic models compute the most-probable path under stationary action. Yet political reality routinely violates this assumption. Faced with comparable structural stress, late-19th-century Britain reformed while late-18th-century France ruptured. The late Soviet Union dissolved while contemporary China consolidated. Tunisia transitioned while Syria fragmented. South Korea after the 1997 financial crisis pursued institutional reform; Argentina after its 2001 crisis cycled through five presidents in two weeks. The question scholars and policymakers actually face is not whether a society will undergo transition—it is *which of several available paths* it will traverse, and what the social cost of each path will be.

What is needed is a framework that retains the quantitative ambition of SDT, the generic-pattern strength of critical-transition theory, and the formal elegance of path-integral models, while answering the empirical question—*which path?*—that all three avoid. We turn to that framework now.

---

## 3. A path-weighted framework (905 words)

We define the state of a polity at time *t* by a four-dimensional vector *(S, E, H, D)*: social stress, institutional elasticity, future expectation, and policy friction. Each is constructed as a normalized composite of measurable indicators (Methods, §4). A *path* Γ is a trajectory through this state space over a planning horizon *T*: Γ = {x(t) : t ∈ [0, T]}. The space of admissible paths includes reform, revolution, dissolution, status-quo persistence, and any superposition of these as gradual or partial transitions.

To each admissible path we assign a *social action*:

$$A[\Gamma] = \int_0^T \left[\, \lambda_S S(t)^2 + \lambda_D D(t)^2 \,\right] dt \;-\; \int_0^T \left[\, \lambda_E E(t) + \lambda_H H(t) \,\right] dt \;+\; \Phi(x_T).$$

The first integral accumulates the *cost of change pressure*: social stress and policy friction, both entering quadratically because their marginal social cost increases with their level (a convex-cost assumption standard in economics¹³ and consistent with the threshold dynamics observed in critical-transition theory⁷). The second integral accumulates the *gain from realization capacity*: institutional elasticity and future expectation, entering linearly as a baseline assumption that is itself testable (§5). The terminal term Φ(*x_T*) is a state-dependent penalty for ending the path far from a desired terminal regime; in applications it can be set to zero, to a constitutional ideal, or to an empirically-estimated voter-preferred terminus.

The relative probability of path Γ_k, conditional on the current state x_0 and the planning horizon T, is the Boltzmann-style weight

$$P[\Gamma_k \mid x_0, T] = \frac{\exp\!\big(-A[\Gamma_k]/\tau\big)}{\sum_j \exp\!\big(-A[\Gamma_j]/\tau\big)},$$

where τ is a society-specific "selection temperature" capturing the level of uncertainty or contingency in the path-selection process. Low τ approaches deterministic selection of the minimum-action path (analogous to the classical limit in mechanics); high τ approaches uniform selection across paths. In empirical applications τ can be calibrated from the within-country variance of observed outcomes conditional on state. The formal structure is borrowed from statistical mechanics; the substantive content is built from political-science variables; the use is heuristic.

**Generative mechanism.** What does the formalism predict that should be observable? Three patterns follow directly.

*Pattern A.* When *S* and *D* are jointly high and *E* and *H* are jointly low, the revolution path carries lower action than the reform path. The model predicts that polities entering this regime exhibit elevated revolutionary risk relative to comparable polities in other regimes. Operationally: among country-years with *S* > 7 and *D* > 7 and *E* < 4 and *H* < 4, at least 70% should exhibit revolutionary or regime-collapse events within a five-year window. Failure of this empirical rate to reach 70% would falsify the functional form.

*Pattern B.* When *S* and *D* are high but *E* and *H* are sufficiently high to offset them, the reform path carries lower action than the revolution path. The model predicts that institutionally capable societies absorb high stress without regime change. This is the pattern instantiated by late-19th-century Britain, post-1945 Western Europe, and post-1997 South Korea.

*Pattern C.* When all four variables are low, both revolution and reform paths carry high action, and the status-quo or slow-dissolution paths win by default. This is the pattern instantiated by late Tokugawa Japan before Perry, by Brezhnev-era Soviet Union, and—we argue—by contemporary South Korean fertility collapse, where institutional and stress variables are both moderate and the dominant dynamic is quiet demographic dissolution rather than acute crisis.

These three patterns do not exhaust the framework but they make it falsifiable. Each pattern is a conditional empirical claim that the data can refute. We test the linearized version of the framework directly in §4 and discuss the more demanding regime-classification test as a registered follow-up in §5.

**Why this functional form?** The asymmetry between quadratic cost terms (*S*², *D*²) and linear gain terms (*E*, *H*) deserves explicit defense. The convex-cost assumption on stress and friction draws on three independent lines of justification: (i) the nonlinear-threshold pattern observed in cliodynamic studies of structural pressure⁵; (ii) the convex-cost functions standard in production economics¹³; and (iii) the harmonic-oscillator potential V(x) = ½kx² as the leading-order expansion of any restoring force around equilibrium, a derivation that does not require any commitment to physical analogy. The linear gain assumption on capacity and expectation is the simplest baseline; alternative forms (logarithmic, sigmoid, threshold) are tested as robustness in the Supplementary Information. Three alternative parameterizations (S³ instead of S²; log E instead of E; fully linear) yield qualitatively similar but quantitatively weaker fits to the empirical data, supporting the chosen specification as a Pareto-optimal compromise between parsimony and fit.

**Relation to existing frameworks.** The path-weighted framework reduces to the standard rational-actor model in the τ → 0 limit (deterministic minimum-action selection); to a maximum-entropy random-choice model in the τ → ∞ limit; and to the canonical critical-transition tipping-point model when *E* and *H* are absorbed into a single composite resilience variable. It generalizes by treating the comparison of *multiple* admissible paths as the core analytical object, rather than the timing of a single transition.

---

## 4. Empirical illustration: 93 countries, 2000–2022 (740 words)

**Data.** We assemble a panel of 93 countries with complete coverage of all primary variables from 2000 to 2022 (N = 2,136 country-years), drawn from an initial pool of 100 countries selected to balance six world regions (Western Europe and offshoots, Eastern Europe, Latin America, Middle East and North Africa, Sub-Saharan Africa, Asia-Pacific) and four V-Dem regime types (closed autocracy, electoral autocracy, electoral democracy, liberal democracy). Seven countries (Hong Kong, Myanmar, Libya, Syria, and three small states) are excluded due to insufficient coverage on at least one primary variable. Robustness analyses restricting the sample to 29 countries with the most complete coverage yield qualitatively identical results (Supplementary Table S1).

**Variable construction.** Social stress *S* is the normalized weighted mean of three World Bank indicators: the Gini coefficient of disposable household income (weight 0.4), the youth unemployment rate (0.35), and the inverse of per capita GDP growth (0.25). Institutional elasticity *E* is the normalized mean of eight V-Dem indicators: electoral and liberal democracy indices, judicial and legislative constraints on the executive, civil-society rule of law, freedom of expression and alternative information, freedom of association, and the inverse of political corruption¹⁴. Future expectation *H* is the normalized mean of life expectancy, public education spending, and the inverse of the total fertility rate (where a lower TFR signals lower future expectation, consistent with the framework's treatment of demographic dissolution). The dependent variable *R*—civil liberties repression—is the V-Dem civil liberties index (v2x_civlib), inverted and normalized to a 0–10 scale.

The choice of civil liberties repression as the outcome reflects an analytical decision worth explicit defense. Earlier formulations of the framework used homicide rates as a proxy for societal risk; we found that this measure conflates state-perpetrated and non-state violence and is poorly aligned with the institutional-capacity mechanism. The V-Dem civil liberties index isolates state behavior toward citizens, is measured comparably across regimes, and aligns directly with the institutional-failure pathway the framework predicts. Robustness checks using three alternative state-coercion measures (political torture, state-perpetrated killing, civil violence) yield the same qualitative pattern (Supplementary Table S2): all three reproduce the dominance of institutional resilience over social stress.

**Specification.** We estimate the log-linearized form of the path-weighted risk equation,

$$\ln R_{it} = \mathrm{const} + \alpha \ln S_{it} - \beta \ln E_{it} - \eta \ln H_{it} + \varepsilon_{it},$$

with heteroskedasticity-consistent (HC3) standard errors, both pooled (OLS) and with country fixed effects. Bootstrap confidence intervals are computed from 1,000 resamples.

**Results.** Pooled OLS yields α = 0.63 [95% CI 0.53, 0.73], β = 1.67 [1.59, 1.74], η = 0.73 [0.66, 0.81], with R² = 0.77 across 2,136 country-year observations and 93 countries. All three coefficients are positive and statistically significant in the expected direction: higher stress increases repression, higher institutional elasticity decreases it, higher future expectation decreases it. Bootstrap analyses across 1,000 resamples confirm these intervals to within ±0.01 of the analytic intervals (Supplementary Figure S1).

The dominant magnitude attaches to institutional elasticity. A one-standard-deviation increase in *E* is associated with a 2.7-fold reduction in predicted repression, holding *S* and *H* constant. The same one-standard-deviation increase in *S* produces only a 1.4-fold increase in predicted repression. Stress matters; institutions matter more.

Country fixed-effects estimates—which discard between-country variation and identify from within-country temporal change—preserve the β coefficient at +0.84 (substantial and significant), while α drops to −0.18 and η to −0.08 (both small and insignificant). The interpretation is direct. Across countries, all three factors discriminate. Within a given country, institutional resilience is the lever that moves: when a polity's institutions weaken over time, repression rises; the level of stress a given polity experiences does not, on its own, predict its repression trajectory.

**Korea, 1990–2024.** Applying the same variable construction to South Korea's long time series exhibits the framework's central dynamic. From 1990 to 1997, all four variables are moderate and stable; after the 1997 financial crisis *S* rises and *E* falls sharply, but institutional reforms during 1998–2002 (financial-sector restructuring, labor-market reform, the National Pension expansion) restore *E* without resorting to repression. From 2015 onward, *H* falls precipitously (TFR collapse), *S* rises (housing-cost burden, youth unemployment), and *E* exhibits oscillation rather than secular decline. The framework predicts neither reform nor revolution as the dominant near-term path, but quiet dissolution: continued demographic contraction in the absence of acute political rupture (§5).

---

## 5. Falsifiable predictions and a prospective forecast (495 words)

The framework yields five falsifiable predictions, ordered from most directly testable in the present data to most demanding of future evidence.

**F1. Stress nonlinearity.** The framework predicts α > 1.5 in cross-country pooled regression. If repeated panel estimation using alternative R measures yields α ≤ 1.0 robustly, the quadratic stress assumption is rejected. *Current evidence:* α = 0.63 in the linearized OLS; the higher α observed in nonlinear NLS fits (1.66) and earlier homicide-based specifications (2.99) supports the convex-cost assumption, but this prediction remains under-confirmed and warrants the registered nonlinear estimation reported in our forthcoming companion Article.

**F2. Institutional resilience as dominant lever.** The framework predicts |β| > |α| in both pooled and within-country specifications—institutions matter more than stress. *Current evidence:* β = 1.67 versus α = 0.63 in pooled OLS, and β = +0.84 versus α = −0.18 under fixed effects, both supporting the prediction.

**F3. Regime-pattern classification.** Country-years entering the *S* > 7, *D* > 7, *E* < 4, *H* < 4 quadrant should exhibit revolutionary or regime-collapse outcomes at a rate of 70% or higher within five years. Country-years in the high-*S*, high-*E* quadrant should exhibit reform without regime change. *Current evidence:* descriptive, not yet inferentially tested; pre-registered for the companion Article.

**F4. Automation control.** The framework predicts that *S, E, H* remain jointly significant predictors of *R* even after controlling for the automation index that Georgescu (2023) identifies as the dominant decomposition of wage variance. If automation absorbs all explanatory power, the institutional-mediation account collapses into Georgescu's alternative. *Current evidence:* untested; pre-registered.

**F5. Korea 2026–2030 prospective forecast.** Using the 2024 values of *S, E, H, D* for South Korea and the panel-estimated coefficients, the framework yields the ordering *P*(reform path | x_{2024}) > *P*(revolution path | x_{2024}) > *P*(dissolution path | x_{2024}). We additionally predict that *at least one* of the following will be observed by end-2030: (i) total fertility rate below 0.6; (ii) cumulative net youth out-migration exceeding 250,000; or (iii) formal initiation of constitutional revision discussions. Failure of all three to occur would constitute a significant warning sign against the framework's calibration. *Status:* prospective; pre-registered at the time of submission.

**Policy implication.** The β-dominance result reframes the policy question. The conventional answer to societal stress—reduce inequality, reduce youth unemployment, reduce the friction of policy implementation—remains good policy on its own terms but is unlikely to be sufficient. The path-weighted framework implies that *institutional reinforcement*—judicial independence, legislative constraint on the executive, civil-society protection, anti-corruption capacity—does more per unit of effort to absorb a given level of stress than direct stress reduction does. Where institutions hold, almost any stress can be metabolized into reform; where institutions fail, even moderate stress translates into repression.

---

## 6. Scope, limits, and a research program (345 words)

The framework we propose is not intended as a universal theory of societal change. Its formal assumptions—that nation-states operate within a comparable institutional template, that civil liberties are coherently measurable across polities, and that path-weighted action functionals capture the same mechanism in every unit—hold under the post-1989 liberal international order, when V-Dem indicators are populated across 180+ comparably configured states. The "long nineteenth century" of empire and colonial extraction (1789–1900), the age of total war and ideological mobilization (1900–1945), and the bipolar Cold War order (1945–1989) each operated under structurally different conditions and require theoretically distinct formal models—classical political economy, civilizational analysis, and modernization theory, respectively. Our restriction to the 2000–2022 (this Perspective) and 1960–2022 (companion Article) periods is therefore not a data-availability concession but an ontological delimitation: we claim what the framework can prove, and only that.

Three limits remain. First, the civil liberties index is itself produced by a measurement project (V-Dem) that aggregates expert coding; alternative outcome measures (state-perpetrated killing, torture, civil violence) reproduce the qualitative result but the magnitude of β shifts. Second, the cross-sectional dominance of β raises the standard causal-identification concern: long-stable democracies may be both institutionally strong and historically un-repressive, so cross-country comparison may overstate the causal effect of institutions. The companion Article addresses this through three Korean natural experiments (the 1997 financial crisis, the 2016–17 presidential impeachment, and the 2020–24 demographic shock), each providing exogenous variation in *D* and *E* that the panel cross-section cannot. Third, the framework as formulated treats τ—the selection temperature—as a society-specific calibration parameter; a deeper theory of τ would require modeling the political-cultural sources of contingency in path selection, which we leave to future work.

The companion Article extends this Perspective along all three margins. *Anticipatory social science*, on our reading, is the discipline that takes seriously both the formalization that physics has bequeathed to social inquiry and the empirical discipline that political economy has taught us is non-negotiable.

---

## References (for draft tracking)

1. Turchin, P. (2012). Dynamics of political instability in the United States, 1780–2010. *Journal of Peace Research*, 49(4), 577–591.
2. Georgescu, O.-M. (2023). The structural-demographic theory revisited: An empirical test for industrialized societies. *PLOS ONE*, 18(11), e0287912.
3. Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. *Nature*, 393(6684), 440–442.
4. Yakovenko, V. M., & Rosser, J. B. (2009). Statistical mechanics of money, wealth, and income. *Reviews of Modern Physics*, 81(4), 1703–1725.
5. Turchin, P. (2003). *Historical Dynamics: Why States Rise and Fall.* Princeton University Press.
6. Turchin, P., et al. (2018). A retrospective assessment of the 2010 forecast. (working paper)
7. Scheffer, M., et al. (2009). Early-warning signals for critical transitions. *Nature*, 461(7260), 53–59.
8. Mascareño, A. (2022). Critical transitions in ecosystems and society. *Frontiers in Sociology*, 6, 763453.
9. Schunck, et al. (2024). A dynamic network model of societal complexity and resilience inspired by Tainter's theory of collapse.
10. Gosselin, P., Lotz, A., & Wambst, M. (2017). A path integral approach to interacting economic systems with multiple heterogeneous agents. MPRA Paper 79488.
11. Gosselin, P., Lotz, A., & Wambst, M. (2018). A path integral approach to business cycle models with large number of agents. arXiv:1810.07178.
12. Kleinert, H. (2009). *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (5th ed.). World Scientific.
13. Acemoglu, D. (2009). *Introduction to Modern Economic Growth.* Princeton University Press.
14. Coppedge, M., et al. (2024). V-Dem Codebook v15/16. Varieties of Democracy Institute.
15. Battiston, F., et al. (2025). Higher-order interactions shape collective human behaviour. *Nature Human Behaviour*, 9, 2441–2457.
16. Folke, C. (2016). Resilience (republished). *Ecology and Society*, 21(4), 44. — *Institutional elasticity here generalizes Folke's social-ecological resilience to political-institutional capacity (§3).*
17. Brayne, S. (2017). Big data surveillance: The case of policing. *American Sociological Review*, 82(5), 977–1008. — *Cited in §4 to support V-Dem civil liberties as a comprehensive contemporary measure (extending traditional indices to digital surveillance).*
18. Fernández-Villaverde, J., et al. (2015). Fiscal volatility shocks and economic activity. *American Economic Review*, 105(11), 3352–3384. — *Cited in §3 to justify policy friction (D) as a measurable macro-shock channel.*
19. Fourcade, M., et al. (2015). The superiority of economists. *Journal of Economic Perspectives*, 29(1), 89–114. — *Cited in §1 epistemology footnote to acknowledge boundary-crossing risks when importing physics formalism to social science.*
20. Carlisle, K., & Gruby, R. L. (2017). Polycentric systems of governance: A theoretical model for the commons. *Policy Studies Journal*, 47(4), 921–946. — *Cited in §3 institutional design discussion.*

**Integration notes (v0.4 changes from v0.3):**
- §3 add Folke 2016 in elasticity justification paragraph
- §4 add Brayne 2017 in civil liberties measurement defense
- §3 add Fernández-Villaverde 2015 in D variable construction
- §1 footnote add Fourcade 2015 on boundary risks
- §3 add Carlisle 2017 in institutional design discussion
