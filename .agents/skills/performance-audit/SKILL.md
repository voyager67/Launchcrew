---
name: performance-audit
description: "Investigate latency, throughput, memory, startup time, bundle size, query cost, or resource usage using measurements and bottleneck analysis before proposing optimizations."
license: MIT
---

# Performance audit workflow

1. Define the user-visible performance objective and target environment. Identify an SLO or baseline if one exists.
2. Collect representative measurements with a reproducible workload. Separate cold-start, steady-state, p50/p95/p99, CPU, memory, I/O, network, and cost where relevant.
3. Trace the critical path and inspect profiling/query/network evidence before guessing at bottlenecks.
4. Rank suspected bottlenecks by measured impact and confidence. Note workload shape and sample limitations.
5. Propose a minimal experiment that isolates one optimization. Define success and regression thresholds before changing code.
6. Implement only after baseline evidence exists, unless a clear pathological issue is independently proven.
7. Re-measure under the same workload, environment, and measurement method. Check correctness, resource trade-offs, tail latency, and operational complexity.
8. Document findings even when no optimization is justified.

## Output

- Objective and workload
- Baseline + method
- Bottleneck evidence
- Candidate changes ranked by expected impact / confidence / cost
- Before/after comparison and regression checks
- Recommendation or reason to leave the code unchanged

## Guardrails

Do not invent speedups or infer causality from one noisy run. Avoid premature caching, concurrency, or complexity without evidence. Do not run load tests against production without explicit authorization.
