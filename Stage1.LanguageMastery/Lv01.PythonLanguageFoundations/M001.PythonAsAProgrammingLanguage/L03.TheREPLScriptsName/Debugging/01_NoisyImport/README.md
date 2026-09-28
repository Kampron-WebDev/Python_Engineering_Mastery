# Debugging 01: Noisy Import

`main.py` is a little launch-control tool. Another team wants to **import** its `countdown` function:

```python
countdown(3)   # → should RETURN "3... 2... 1... Liftoff!"
```

But just **importing** the file launches a rocket (it prints the whole launch sequence), and `countdown` gives importers `None`. There are **2 bugs**.

## Your task

1. `python -m pytest` and read which tests fail.
2. Fix both. Running `python main.py` directly must **still** perform the launch (print the countdown).
3. In MY-NOTES.md: why did importing trigger the launch? What's the difference between *printing* a result and *returning* it?
