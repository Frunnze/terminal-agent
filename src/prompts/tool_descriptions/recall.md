## Description
Retrieves relevant memories from past experience based on a query.

## When to use
Use at the start of a task to recall relevant facts, ideas, mistakes, or solutions that may help complete the user's request more effectively.

## Arguments

- `query` (string, required): The search query describing what to recall — typically a summary of the current task or problem.
- `n_results` (integer, optional): Number of results to retrieve per memory type. Defaults to 3.

## Returns

A list of relevant memories grouped by type (fact, idea, mistake, solution), or a message indicating no memories were found.
