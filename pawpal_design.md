# PawPal+ UML Design

## Class Diagram

```
┌─────────────────────────────┐
│            Pet              │
│  Represents the animal      │
│  being cared for            │
├─────────────────────────────┤
│ - name: str                 │
│ - species: str              │
│ - age: int                  │
└─────────────────────────────┘
          △ has one
          │
┌─────────────────────────────┐
│           Owner             │
│  The person using the app.  │
│  Defines the time budget    │
│  available for care tasks   │
├─────────────────────────────┤
│ - name: str                 │
│ - available_minutes: int    │
└─────────────────────────────┘
          │ passed into
          ▼
┌─────────────────────────────┐       ┌─────────────────────────────┐
│         Scheduler           │ uses  │            Task             │
│  Core logic class.          │──────▶│  A single pet care          │
│  Takes the owner and task   │       │  activity with duration     │
│  list and produces a        │       │  and priority               │
│  filtered, prioritized plan │       ├─────────────────────────────┤
├─────────────────────────────┤       │ - name: str                 │
│ - owner: Owner              │       │ - duration_minutes: int     │
│ - tasks: list[Task]         │       │ - priority: str             │
├─────────────────────────────┤       │   (high / medium / low)     │
│ + generate_plan(): list     │       │ - category: str             │
│   [Task]                    │       │   (walk, feeding, meds,     │
└─────────────────────────────┘       │    grooming, etc.)          │
                                      └─────────────────────────────┘
```

## Relationships

- **Owner has one Pet** — the owner's pet is the subject of all care tasks
- **Scheduler uses Owner** — reads `available_minutes` to constrain the plan
- **Scheduler uses Task[]** — filters and sorts tasks to build the final plan

## Scheduling Logic (generate_plan)

1. Filter out tasks whose `duration_minutes` exceeds remaining time
2. Sort remaining tasks by priority (high → medium → low)
3. Greedily add tasks until `available_minutes` is exhausted
4. Return the selected tasks as an ordered list
