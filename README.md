**Real-Time Multi-threaded Application Simulator**
📌 Overview

The Real-Time Multi-threaded Application Simulator is an educational tool designed to demonstrate how modern operating systems handle threading, synchronization, and CPU scheduling.
It provides a real-time console-based visualization of:

Thread lifecycle states

Synchronization using Monitors (Locks) and Semaphores

Execution behavior under three multithreading models

This project helps students understand how threads share CPU time, how concurrency works internally, and why synchronization is necessary to prevent race conditions.

🎯 **Objectives**

This simulator was developed to:

Demonstrate OS-level multithreading models

Visualize thread state transitions

Show how Locks and Semaphores control shared resource access

Provide an intuitive understanding of thread scheduling

Simulate real-world OS thread behavior in a simplified environment

🧵 Thread Lifecycle States

Each simulated thread transitions through the following states:

NEW – Thread is created

READY – Waiting for CPU

RUNNING – Currently executing

BLOCKED – Waiting for Lock or Semaphore

TERMINATED – Finished execution

These states are printed in real-time during execution.

🔒 Synchronization Mechanisms

This simulator demonstrates two essential OS synchronization tools:

1️⃣ Monitor (Lock)

Ensures mutual exclusion

Only one thread can access the critical section at a time

Other threads become BLOCKED until the lock is released

2️⃣ Binary Semaphore

Controls resource access using acquire() and release()

Threads wait in a queue if the semaphore is unavailable

Common in OS kernels for managing process/thread access

Synchronization guarantees that updates to the shared counter remain safe and race-condition–free.

🧠 Threading Models Implemented
1️⃣ Many-to-One

Many user threads → one kernel thread

Executes sequentially

No parallelism

Used in older Java virtual machines

2️⃣ One-to-One

Each user thread → its own kernel thread

Supports true parallel execution

High performance but higher overhead

Used in Linux pthreads and Windows threads

3️⃣ Many-to-Many

Many user threads → limited pool of kernel threads

Balanced performance

Reduced overhead

Simulated using Python’s ThreadPoolExecutor
