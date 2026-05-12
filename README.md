# Sampling Profiler (Experimental)

## Overview

This project is a simple **sampling profiler** I experimented with while learning how performance profiling works in Python.

A sampling profiler periodically checks what a program is doing (its call stack or execution state) instead of tracing every single line of code. This makes it lightweight and useful for observing long-running or CPU-heavy loops.

---

## What this project does

* Runs a Python program normally
* At regular time intervals, takes a snapshot of what the program is executing
* Aggregates these snapshots to estimate where time is being spent
* Prints or logs sampled stacks for analysis

---

## Why sampling instead of tracing?

* **Lower overhead** than line-by-line tracing
* Works better for performance analysis in loops or real-time programs
* Provides a statistical view instead of exact execution timing

---

## Example use case

For example, if you run a loop like:

```python
import random

while True:
    n = [random.randint(1, 100) for _ in range(100)]
    n.sort()
```

A sampling profiler might repeatedly capture that the program is often inside:

* `random.randint`
* `list comprehension`
* `sort()`

This helps identify bottlenecks.

---

## How it works (simple version)

Most sampling profilers do something like:

1. Start your program in a separate thread or process
2. Every X milliseconds:

   * Interrupt or inspect the running program
   * Record the current stack trace
3. After a period of time:

   * Count how often each function appears
   * Display results as a “hot path” summary

---

## Limitations

* Not exact (it’s statistical)
* May miss very short function calls
* Resolution depends on sampling frequency

---

## Running it (example idea)

Depending on your setup:

```bash
python sampling_profiler.py your_script.py
```

Or if integrated into a toolchain:

```bash
python -m profiling.sampling -p <PID>
```

---

## Learning outcome

This experiment helped me understand:

* How profilers observe programs without fully instrumenting them
* Why performance analysis is often statistical
* How CPU time is distributed in real programs

---

## Future improvements

* Better visualization (flame graphs)
* GUI dashboard
* Lower overhead sampling with OS-level hooks
* Support for async programs

---

## Notes

This is just an experimental learning project and not intended for production use.
