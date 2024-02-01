# Rapid7 CSV Analysis Tool

## Overview
This Python script is designed to assist users in analyzing Rapid7 CSV exports by leveraging the OpenAI API. It helps in understanding and querying the data in these CSV documents, focusing on computer hosts and the CVEs (Common Vulnerabilities and Exposures) present on them. The script uses an AI assistant to provide detailed, markdown-formatted responses to user queries about the data.

## Requirements
- Python 3.x
- An OpenAI API key (OPENAI_API_KEY environment variable must be set)
- Rapid7 CSV export file

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ohnotnow/r7analyser.git
   cd r7analyser
   ```

2. **Install Dependencies:**
   Use pip to install the required Python libraries.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Setting the OPENAI_API_KEY Environment Variable:**
   Ensure that the OPENAI_API_KEY environment variable is set with your OpenAI API key.
   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```

2. **Running the Script:**
   Use the following command to run the script. Replace `[csv_file_name]` with the name of your Rapid7 CSV export file.
   ```bash
   python main.py [full_path_to_csv_file]
   ```

### Flags
- `--thread`: Use an existing thread ID.
- `--assistant`: Use an existing assistant ID or set through the R7_ASSISTANT_ID environment variable.

### API Keys Required
- **OpenAI API Key:** Set as an environment variable (OPENAI_API_KEY). This is crucial for accessing the OpenAI API services.

## How it Works
The script processes the Rapid7 CSV export file and uses the OpenAI API to generate responses. It first creates a file object for the CSV file and then a thread in OpenAI. If an assistant ID is not provided, it offers to create a new assistant with specified parameters.

Once set up, the script can take user queries in natural language and pass them to the AI assistant. The assistant then provides detailed, markdown-formatted responses based on the data in the CSV file.

## Contributing
Contributions to the project are welcome. Please ensure that you update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
