# Advent of Code Solutions

This repository contains my personal solutions to the [Advent of Code](https://adventofcode.com/) puzzles, organized by year and then by day. Each day’s folder holds the code for that specific day’s challenge.

## Repository Structure

A typical folder layout looks like this:

```
.
├── 📂 2024
│   ├── 📂 AOC Day 1
│   │   ├── 📄 input.txt
│   │   ├── 📄 part1.py
│   │   └── 📄 part2.py
│   ├── 📂 AOC Day 2
│   │   ├── 📄 input.txt
│   │   ├── 📄 part1.py
│   │   └── 📄 part2.py
│   └── ...
├── 📂 2023
│   ├── 📂 AOC Day 1
│   │   ├── 📄 input.txt
│   │   ├── 📄 part1.py
│   │   └── part2.py
│   ├── 📂 AOC Day 2
│   │   ├── 📄 input.txt
│   │   ├── 📄 part1.py
│   │   └── 📄 part2.py
│   └── ...
├── 📄 README.md
```

- **`2024/`**  
  Each year has its own folder (e.g. `2024`, `2023`, etc.).
- **`AOC Day X/`**  
  Within each year, there are subfolders for every challenge day. Each day folder contains:
  - **`input.txt`** – The puzzle input for that specific day (if you want to test on your own input, insert the input as input.txt in the directory).
  - **`part1.py`** – The Python solution for Part 1 of the day’s puzzle.
  - **`part2.py`** – The Python solution for Part 2 of the day’s puzzle.

## Usage

1. **Obtain the Puzzle Input**  
   Advent of Code provides a unique puzzle input for each user. Copy your puzzle input into the `input.txt` file in the corresponding day’s folder.

2. **Run the Solutions**  
   From your terminal or command prompt, navigate to the folder for the specific day you want to run. For example, for Day 16 of 2024:

   ```bash
   cd 2024/AOC\ Day\ 16
   ```

   Then execute either Part 1 or Part 2:

   ```bash
   python part1.py
   python part2.py
   ```

   (Adjust the above commands to match your Python environment or script runner.)

3. **Check the Output**  
   The scripts will read from `input.txt` in the same folder and then print the results for that day’s puzzle.

## Contributing

These are my personal solutions for practice and learning. If you find any bugs or have suggestions for alternative approaches, feel free to open an issue or submit a pull request.

---

**Happy Advent of Code!**
