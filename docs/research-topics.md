# Research topics

Your own idea is welcome: see "Proposing a topic" in [seminar-rules.md](seminar-rules.md). The
projects below are larger research programmes that the supervisor wants to develop with students.
Each one is designed to be **split into several theses** that share data, code and an evaluation
protocol, and to combine into a journal submission.

Whatever the topic, the faculty expects the quantitative method to serve an economic or financial
problem, and the problem should be visible in the title.

The reading lists are starting points. Check every reference yourself before you cite it.

---

## 1. Foundation models for market risk: task-specific heads on Chronos

**Problem.** Banks, funds and insurers need reliable forecasts of volatility and tail risk
(Value-at-Risk, Expected Shortfall) for capital and risk-limit decisions. The workhorses are
GARCH-type and HAR models. Pretrained time-series foundation models such as Chronos promise strong
forecasts with little task-specific training, but they are pretrained mostly on non-financial data
and are not designed for heavy tails or volatility clustering.

**Idea.** Keep the pretrained backbone and train lightweight, task-specific heads on its
representations: a distributional head for realised volatility, quantile heads for VaR, and a joint
VaR and ES head trained with a consistent scoring function. Compare zero-shot use, a frozen backbone
with a new head, and parameter-efficient fine-tuning.

**Research questions**

- Does generic pretraining transfer to financial returns, and for which asset classes and horizons?
- How much of the gain comes from the head, and how much from fine-tuning the backbone?
- Do the forecasts pass regulatory-style backtests, rather than only winning on average loss?
- How stable are the results across calm and crisis periods?

**Benchmarks and evaluation.** GARCH family, HAR-RV, quantile regression and CAViaR; rolling-window
out-of-sample design; coverage and independence tests for VaR; joint VaR and ES scoring functions;
model confidence sets.

**Possible theses.** Volatility forecasting | VaR and ES forecasting | cross-asset and cross-market
transfer | fine-tuning strategies and compute cost.

**Starting literature**

- Ansari, A. F., et al. (2024). Chronos: Learning the language of time series. *Transactions on Machine Learning Research*.
- Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. *Journal of Econometrics*, 31(3), 307-327.
- Corsi, F. (2009). A simple approximate long-memory model of realized volatility. *Journal of Financial Econometrics*, 7(2), 174-196.
- Engle, R. F., & Manganelli, S. (2004). CAViaR: Conditional autoregressive value at risk by regression quantiles. *Journal of Business & Economic Statistics*, 22(4), 367-381.
- Christoffersen, P. F. (1998). Evaluating interval forecasts. *International Economic Review*, 39(4), 841-862.
- Fissler, T., & Ziegel, J. F. (2016). Higher order elicitability and Osband's principle. *The Annals of Statistics*, 44(4), 1680-1707.
- Patton, A. J., Ziegel, J. F., & Chen, R. (2019). Dynamic semiparametric models for expected shortfall (and value-at-risk). *Journal of Econometrics*, 211(2), 388-413.
- Hansen, P. R., Lunde, A., & Nason, J. M. (2011). The model confidence set. *Econometrica*, 79(2), 453-497.

---

## 2. Detrending and deseasonalisation for non-stationary time series: a review and benchmark

**Problem.** Every forecasting pipeline for economic and business series makes a choice about trend
and seasonality: differencing, filtering, decomposing, normalising, or leaving it to the model. The
choice is usually made by habit, and its effect on forecast accuracy, on inference and on economic
interpretation is rarely measured. With machine-learning, deep and foundation models the old advice
may no longer hold.

**Idea.** A systematic review with a clear taxonomy, followed by a controlled benchmark in which
only the treatment of non-stationarity varies.

**Methods to map**

- Differencing, seasonal differencing, variance-stabilising transformations
- Filters: Hodrick-Prescott, Hamilton's regression filter, band-pass filters
- Decompositions: STL and MSTL, X-13ARIMA-SEATS, TRAMO-SEATS
- Fourier and other deterministic terms; wavelets, EMD, VMD
- Learned approaches: reversible instance normalisation, decomposition blocks in neural forecasters

**Research questions**

- When does preprocessing help, and when does it destroy signal or leak future information?
- Do ML, deep and foundation models still benefit from explicit detrending and deseasonalisation?
- How do conclusions differ between macroeconomic, financial and retail demand series?

**Possible theses.** Review and taxonomy | benchmark on public forecasting datasets | an economic
case study (for example business-cycle extraction or demand forecasting).

**Starting literature**

- Cleveland, R. B., Cleveland, W. S., McRae, J. E., & Terpenning, I. (1990). STL: A seasonal-trend decomposition procedure based on loess. *Journal of Official Statistics*, 6(1), 3-73.
- Hodrick, R. J., & Prescott, E. C. (1997). Postwar U.S. business cycles: An empirical investigation. *Journal of Money, Credit and Banking*, 29(1), 1-16.
- Hamilton, J. D. (2018). Why you should never use the Hodrick-Prescott filter. *The Review of Economics and Statistics*, 100(5), 831-843.
- Kim, T., Kim, J., Tae, Y., Park, C., Choi, J.-H., & Choo, J. (2022). Reversible instance normalization for accurate time-series forecasting against distribution shift. *ICLR*.
- Zeng, A., Chen, M., Zhang, L., & Xu, Q. (2023). Are transformers effective for time series forecasting? *AAAI*.
- Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2020). The M4 Competition: 100,000 time series and 61 forecasting methods. *International Journal of Forecasting*, 36(1), 54-74.
- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and practice* (3rd ed.). OTexts.

---

## 3. Foundation models for tabular data: a review with economic applications

**Problem.** Credit scoring, insurance pricing, churn and customer-value models all run on tabular
data, where gradient-boosted trees have dominated for a decade. Pretrained tabular foundation
models, in particular in-context learners in the TabPFN line and approaches built on large language
models or cross-table pretraining, now claim to match or beat them, especially on small samples.
Practitioners in regulated industries need to know whether the claims hold where it matters.

**Idea.** A structured review of tabular foundation models, followed by an evaluation on economic
and financial prediction tasks that looks beyond accuracy.

**Research questions**

- In which regimes do these models win: small samples, many categorical features, distribution shift?
- Are predicted probabilities calibrated well enough for pricing and credit decisions?
- What are the costs: inference time, data-size limits, interpretability, regulatory acceptance?

**Possible theses.** Literature review and taxonomy | benchmark against gradient boosting on
financial datasets | calibration and interpretability study | a sector case study (credit, insurance, e-commerce).

**Starting literature**

- Hollmann, N., Müller, S., Eggensperger, K., & Hutter, F. (2023). TabPFN: A transformer that solves small tabular classification problems in a second. *ICLR*.
- Hollmann, N., et al. (2025). Accurate predictions on small data with a tabular foundation model. *Nature*, 637, 319-326.
- Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). Why do tree-based models still outperform deep learning on typical tabular data? *NeurIPS Datasets and Benchmarks*.
- Shwartz-Ziv, R., & Armon, A. (2022). Tabular data: Deep learning is not all you need. *Information Fusion*, 81, 84-90.
- Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. *KDD*.
- van Breugel, B., & van der Schaar, M. (2024). Why tabular foundation models should be a research priority. *ICML* (position paper).

---

## Other directions

From the course syllabus; all are open for your own proposals:

- Comparing quantitative methods on a chosen financial or business problem, with emphasis on
  validation rigour and robustness of conclusions
- Case studies from finance, insurance, e-commerce or logistics using modern machine learning
- Probabilistic modelling and forecasting of economic, market or operational phenomena
- Risk measurement and uncertainty modelling
- Causal inference for business decisions and policy evaluation
- Machine learning beyond classic analytics: behavioural economics, public policy, social phenomena
