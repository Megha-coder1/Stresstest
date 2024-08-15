# PhoneStress v3.1

**PhoneStress** is a tool designed for stress testing CPUs and memory of a phone or computer. It provides a graphical interface to configure and start stress tests. This tool is meant for research and educational purposes only.

## Features

- **Graphical User Interface (GUI)**: A simple \`tkinter\` GUI for easy configuration and execution.
- **Stress Methods**: Two methods available - CPU stress and memory stress.
- **User Configuration**: Set the number of workers and select the stress method through the GUI.
- **Timed Execution**: Stress test starts after a 10-second delay.

## Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/yourusername/PhoneStress.git
   \`\`\`
2. Navigate to the project directory:
   \`\`\`bash
   cd PhoneStress
   \`\`\`
3. Install the required dependencies:
   \`\`\`bash
   pip install numpy
   \`\`\`

## Usage

1. Run the application:
   \`\`\`bash
   python phonestress.py
   \`\`\`
2. **Welcome Window**: A welcome window will appear with the following options:
   - **Next**: Enter the number of workers and choose the stress method. The stress test will commence in 10 seconds.
   - **Cancel**: Exit the application.
   - **Skip**: Switch between CPU and memory stress methods, set workers to 1, and start the test in 10 seconds.

3. **Input**:
   - **Number of Workers**: Enter the number of concurrent workers for the stress test.
   - **Stress Method**: Choose between \`cpu\` (CPU stress) and \`memory\` (Memory stress).

4. The stress test will begin after a 10-second countdown.

## Code Overview

- **PhoneStress Class**: Manages the stress test, including starting and monitoring workers.
- **StressWorker Class**: Executes the stress tasks based on the selected method.
- **GUI**: Uses \`tkinter\` to provide a user-friendly interface for configuration and execution.

## License

This software is distributed under the GNU General Public License version 3 (GPLv3).

## Legal Notice

**THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY!** If you engage in any illegal activity, the author does not take any responsibility for it. By using this software, you agree with these terms.

## Author

**K. MEGHADITYA**  
Email: [meggha2013@gmail.com](mailto:meggha2013@gmail.com)
