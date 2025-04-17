Efficient Page Replacement Algorithm Simulator

A desktop application built with Python to simulate and compare popular page replacement algorithms such as **FIFO**, **LRU**, and **Optimal**. Designed for students and OS learners, the simulator provides **interactive GUI**, **visual analytics**, and **exportable performance reports** — making operating systems fun and easy to understand.



Project Objective

- Simulate and visualize how different page replacement algorithms work.
- Help users understand memory management in operating systems through graphs and statistics.
- Allow easy input of custom reference strings and frame sizes.
- Provide downloadable results for reports or assignments.


Features
 FIFO, LRU, and Optimal algorithm simulation  
 Beautiful Tkinter GUI  
 Step-by-step algorithm execution  
 Graphs using Matplotlib and Seaborn  
 CSV export of analysis results  
  Comparative statistics: Page faults, hit/miss ratio  



Project Structure


OS-Project/
├── algorithms.py      # Contains FIFO, LRU, and Optimal algorithm logic
├── gui.py             # GUI built with Tkinter for user interaction
├── analysis.py        # Performance visualization and CSV export
├── main.py            # Project entry point and module integration
├── README.md          # You’re reading it :)
```



echnologies Used

| Component   | Technology          |
|------------|---------------------|
| Frontend   | Tkinter (Python)    |
| Backend    | Python              |
| Visualization | Matplotlib, Seaborn |
| Export     | Pandas (CSV export) |



How to Run the Project

 Step 1: Clone the Repository

git clone https://github.com/chirugeek463/OS-Project.git
cd OS-Project


Step 2: Install Required Libraries

pip install matplotlib seaborn pandas


tep 3: Run the Application

python main.py

The GUI window will open — enter your reference string, choose an algorithm, set the number of frames, and click simulate!
 If required create a virtual environment 
 python3 -m venv myenv 
 source myenv/bin/activate - to activate the virtual environment 
 deactivate - to deactivate 


Sample Output

- Bar and line graphs** showing comparative performance
- Page faults** count for each algorithm
- it/Miss ratios**
- Exportable CSV** with results for documentation/report



Future Enhancements


- Add LFU (Least Frequently Used) and MRU algorithms  
- Web version using Flask + React  
- Animation-based visualization of algorithm steps  
- AI-based recommendation of the most efficient algorithm based on input



Educational Use Case

This project is ideal for:

- Operating System coursework demonstrations  
- Assignments and lab evaluations  
- Gaining a deeper understanding of memory management concepts  
- Comparing algorithms in real-time with data

---


 
Created learning and sharing  
GitHub: [github.com/chirugeek463](https://github.com/chirugeek463)

License

This project is licensed under the MIT License**.  
Feel free to use, modify, and share!
# OS-Project
# OS-Project
