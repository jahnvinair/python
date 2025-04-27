# python

# AI Lab Experiments

This repository contains Python implementations for 26 Artificial Intelligence lab experiments, designed to run in a Jupyter notebook environment on a college PC without internet access. Each experiment includes a Python script, paper write-up (theory, algorithm, sample output), viva preparation tips, and implementation notes.

## Experiments

Below is the list of all 26 experiments included in this repository:

1. **Breadth_First_Search_Undirected_Unweighted.py**: Implements BFS for an undirected unweighted graph with user input.
2. **Breadth_First_Search_Directed_Weighted.py**: Implements BFS for a directed weighted graph with user input.
3. **Depth_First_Search_Undirected_Unweighted.py**: Implements DFS for an undirected unweighted graph with user input.
4. **Depth_First_Search_Directed_Weighted.py**: Implements DFS for a directed weighted graph with user input.
5. **Depth_Limited_Search.py**: Implements DLS for a graph with user-defined depth limit.
6. **Best_First_Search_Undirected_Unweighted.py**: Implements Best First Search for an undirected unweighted graph with heuristics.
7. **Best_First_Search_Directed_Weighted.py**: Implements Best First Search for a directed weighted graph with heuristics.
8. **A_Star_Directed_Weighted_CSV.py**: Implements A* algorithm for a directed weighted graph using CSV input.
9. **A_Star_Directed_Weighted_User.py**: Implements A* algorithm for a directed weighted graph with user input.
10. **A_Star_Undirected_Weighted_CSV.py**: Implements A* algorithm for an undirected weighted graph using CSV input.
11. **A_Star_Undirected_Weighted_User.py**: Implements A* algorithm for an undirected weighted graph with user input.
12. **Fuzzy_Set_Operations_3_Sets.py**: Implements union, intersection, and complement for three fuzzy sets.
13. **Fuzzy_Set_DeMorgan_Union.py**: Demonstrates De Morgan’s Law for union of two fuzzy sets.
14. **Fuzzy_Set_DeMorgan_Intersection.py**: Demonstrates De Morgan’s Law for intersection of two fuzzy sets.
15. **Tic_Tac_Toe_Minimax.py**: Implements a Tic-Tac-Toe game where the computer wins or draws using minimax.
16. **Tic_Tac_Toe_Minimax_Lose.py**: Implements a Tic-Tac-Toe game where the computer loses or draws using modified minimax.
17. **MLP_N_Inputs_Two_Hidden.py**: Implements an MLP with N inputs, two hidden layers, and random weight updates.
18. **MLP_4_Inputs_One_Hidden.py**: Implements an MLP with 4 inputs, one hidden layer, and two outputs.
19. **MLP_Backprop_Sigmoid.py**: Implements an MLP with backpropagation using sigmoid activation.
20. **MLP_Backprop_ReLU.py**: Implements an MLP with backpropagation using ReLU activation.
21. **MLP_Backprop_Tanh.py**: Implements an MLP with backpropagation using Tanh activation.
22. **Text_Processing_Clean_Tokenize_Spell.py**: Processes text with cleaning, tokenization, stop word removal, and spell correction.
23. **Text_Processing_Stem_Lemmatize.py**: Processes text with stemming, lemmatization, and 3-word sequences.
24. **Text_Processing_One_Hot.py**: Implements one-hot encoding for three text documents.
25. **Text_Processing_BOW.py**: Implements a bag of words model for three text documents.
26. **Text_Processing_TFIDF.py**: Implements a TF-IDF model for three text documents.

## Requirements

- **Python 3.x**
- **Jupyter Notebook**
- **Libraries** (pre-installed):
  - `numpy` (for Experiments 17–21, 26)
  - `pandas` (for Experiments 8, 10)
  - `sklearn` (for Experiments 24–26)
- **No internet access required** (all dependencies must be pre-installed).

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-lab-experiments.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd ai-lab-experiments
   ```
3. Ensure required libraries are installed (offline setup by lab admin):
   ```bash
   pip install numpy pandas scikit-learn
   ```
4. Open Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## Usage

- Each experiment is a standalone `.py` file that can be run directly or copied into a Jupyter notebook cell.
- For Experiments 8 and 10 (and related graph experiments), generate `graph.csv` and `heuristics.csv` using `create_csv_files.py`:
  ```bash
  python create_csv_files.py
  ```
  Place the generated CSV files in the same directory as the experiment scripts.
- For Experiments 22–26, prepare sample text files (e.g., `doc1.txt`, `doc2.txt`, `doc3.txt`) with approximately 150–200 words each.
- Follow the prompts in each script to provide inputs (e.g., graph edges, number of MLP inputs, file paths).
- Refer to the sample outputs in the experiment documentation for expected results.

## Experiment Details

Each experiment includes:
- **Code**: Python script with input validation and clear comments.
- **Paper Write-Up**: Theory, algorithm, and sample output for written submission.
- **Viva Preparation**: Key concepts and questions to prepare for oral examination.
- **Notes**: Implementation considerations and dependencies.

## Notes

- Ensure CSV and text files are in the same directory as the scripts for relevant experiments.
- Test scripts with provided sample inputs to verify correctness.
- For viva, focus on understanding algorithms (e.g., A*, minimax, backpropagation, TF-IDF) and tracing outputs manually.
- Avoid modifying experiment objectives to prevent mark deductions (-2 marks).

## Contributing

This repository is for educational purposes. If you find issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
