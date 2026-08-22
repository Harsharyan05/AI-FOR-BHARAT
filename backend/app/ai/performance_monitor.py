"""
Performance Monitor

Measures execution time of the Cognisys pipeline.

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass
from typing import Dict
import time


@dataclass
class PerformanceMetric:
    """
    Represents one performance metric.
    """

    name: str
    elapsed_time: float


class PerformanceMonitor:
    """
    Tracks execution time for different
    stages of the RAG pipeline.

    Features
    --------
    • Start timer
    • Stop timer
    • Report timings
    • Reset metrics
    """

    def __init__(self):

        self._start_times: Dict[str, float] = {}

        self.metrics: Dict[str, PerformanceMetric] = {}
        
            # ---------------------------------------------------------
    # Start Timer
    # ---------------------------------------------------------

    def start(
        self,
        name: str,
    ) -> None:
        """
        Starts a timer for the given stage.
        """

        self._start_times[name] = time.perf_counter()

    # ---------------------------------------------------------
    # Stop Timer
    # ---------------------------------------------------------

    def stop(
        self,
        name: str,
    ) -> float:
        """
        Stops the timer and stores the elapsed time.

        Returns
        -------
        float
            Elapsed time in seconds.
        """

        if name not in self._start_times:

            raise ValueError(
                f"No timer started for '{name}'."
            )

        elapsed = (
            time.perf_counter()
            - self._start_times[name]
        )

        self.metrics[name] = PerformanceMetric(
            name=name,
            elapsed_time=elapsed,
        )

        del self._start_times[name]

        return elapsed

    # ---------------------------------------------------------
    # Get Elapsed Time
    # ---------------------------------------------------------

    def elapsed(
        self,
        name: str,
    ) -> float:
        """
        Returns the elapsed time for a stage.

        Returns 0.0 if the stage has not been recorded.
        """

        metric = self.metrics.get(name)

        if metric is None:

            return 0.0

        return metric.elapsed_time

    # ---------------------------------------------------------
    # Reset Metrics
    # ---------------------------------------------------------

    def reset(
        self,
    ) -> None:
        """
        Clears all recorded metrics.
        """

        self._start_times.clear()

        self.metrics.clear()
        
            # ---------------------------------------------------------
    # Total Execution Time
    # ---------------------------------------------------------

    def total_time(
        self,
    ) -> float:
        """
        Returns the total execution time of all
        recorded stages.
        """

        return sum(
            metric.elapsed_time
            for metric in self.metrics.values()
        )

    # ---------------------------------------------------------
    # Generate Report
    # ---------------------------------------------------------

    def report(
        self,
    ) -> str:
        """
        Generates a formatted performance report.
        """

        if not self.metrics:

            return "No performance metrics recorded."

        lines = []

        lines.append("=" * 70)
        lines.append("Performance Report")
        lines.append("=" * 70)

        for metric in self.metrics.values():

            lines.append(
                f"{metric.name:<25}"
                f": {metric.elapsed_time:.4f} sec"
            )

        lines.append("-" * 70)

        lines.append(
            f"{'Total Time':<25}"
            f": {self.total_time():.4f} sec"
        )

        return "\n".join(lines)

    # ---------------------------------------------------------
    # Display Report
    # ---------------------------------------------------------

    def display(
        self,
    ) -> None:
        """
        Prints the performance report.
        """

        print(
            self.report()
        )

    # ---------------------------------------------------------
    # Performance Statistics
    # ---------------------------------------------------------

    def statistics(
        self,
    ) -> None:
        """
        Displays performance statistics.
        """

        print("\n")
        print("=" * 70)
        print("Performance Statistics")
        print("=" * 70)

        if not self.metrics:

            print("No metrics recorded.")
            return

        fastest = min(
            self.metrics.values(),
            key=lambda metric: metric.elapsed_time,
        )

        slowest = max(
            self.metrics.values(),
            key=lambda metric: metric.elapsed_time,
        )

        print(
            f"Stages Recorded : {len(self.metrics)}"
        )

        print(
            f"Fastest Stage   : "
            f"{fastest.name} "
            f"({fastest.elapsed_time:.4f} sec)"
        )

        print(
            f"Slowest Stage   : "
            f"{slowest.name} "
            f"({slowest.elapsed_time:.4f} sec)"
        )

        print(
            f"Total Time      : "
            f"{self.total_time():.4f} sec"
        )

        print("=" * 70)