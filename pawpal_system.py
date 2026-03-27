from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration_minutes: int
    priority: str       # "high", "medium", or "low"
    category: str       # e.g. "walk", "feeding", "meds", "grooming"
    frequency: str      # e.g. "daily", "weekly"
    is_complete: bool = False


class Pet:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        pass

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet's task list.
        Raise ValueError if the task is not found."""
        pass

    def edit_task(self, old: Task, updated: Task) -> None:
        """Replace old task with updated task.
        Raise ValueError if old task is not found."""
        pass


class Owner:
    def __init__(self, name: str, available_minutes: int):
        self.name = name
        # used by Scheduler as the time budget — never mutate directly inside generate_plan
        self.available_minutes = available_minutes
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        pass

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's pet list.
        Raise ValueError if the pet is not found."""
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        # reset at the start of each generate_plan call to avoid stale results
        self.skipped_tasks: list[Task] = []
        # stores the last generated plan so explain_plan can reference it
        self.plan: list[Task] = []

    def generate_plan(self) -> list[Task]:
        """
        Aggregate tasks from all owner.pets, filter out completed tasks,
        sort by priority (high → medium → low), then greedily select tasks
        that fit within owner.available_minutes.
        Stores tasks that didn't fit in skipped_tasks.
        Returns the ordered list of selected tasks.

        Note: use a local 'remaining' counter — never mutate owner.available_minutes directly.
        """
        pass

    def explain_plan(self) -> str:
        """
        Returns a human-readable string explaining why each task was
        included or excluded.

        Note: depends on self.plan and self.skipped_tasks being populated.
        Call generate_plan() first, or guard with an early return if self.plan is empty.
        """
        pass
