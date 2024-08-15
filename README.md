# PhoneStress v3.1

PhoneStress is a tool designed to stress test a phone by generating virtual loads through CPU and memory operations. It is intended for research and educational purposes only. Unauthorized use or malicious intent is prohibited.

## Features

- **CPU Stress**: Generates CPU load by performing intensive computations.
- **Memory Stress**: Allocates and holds a large block of memory.
- **Debug Mode**: tells us in a Detailed way why errors or issues are encountered during the execution of worker tasks.
## Requirements

- Python 3.12 or later
- \`numpy\` library

## Installation

1. Clone the repository:
    \`\`\`sh
    git clone https://github.com/Megha-coder1/PhoneStress.git
    \`\`\`

2. Navigate to the directory:
    \`\`\`sh
    cd PhoneStress
    \`\`\`

3. Install the required libraries:
    \`\`\`sh
    pip install numpy
    \`\`\`

## Usage

Run the script with Python:

\`\`\`sh
python phone_stress.py
\`\`\`

### Command-Line Arguments

- \`-w\` or \`--workers\` : Number of worker processes to run (default: 50)
- \`-s\` or \`--size\` : Size of memory to allocate in megabytes (default: 500)
- python phonestress.py -m CPU
- python phonestress.py -m memory

Example:

\`\`\`sh
python phone_stress.py -w 50 -s 500
\`\`\`

## Code Overview

- **\`PhoneStress\` Class**: Manages the overall stress test, including worker management and monitoring.
- **\`StressWorker\` Class**: Performs CPU stress and memory stress in separate methods.

## License

This software is distributed under the GNU General Public License version 3 (GPLv3).

## Legal Notice

THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY! IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY, THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT. BY USING THIS SOFTWARE YOU AGREE WITH THESE TERMS.

## Author

- **K.MEGHADITYA** - [meggha2013@gmail.com](mailto:meggha2013@gmail.com)
  
