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
   Use the following command to run the script. Replace `[path_to_csv_file]` with the name of your Rapid7 CSV export file.
   ```bash
   python main.py [path_to_csv_file]
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

## Example Run

`python3 main.py ~/report.csv ``

### Initial Summary

I've grouped and summarized the vulnerabilities into the following simplified table:

| Category     | Total Vulnerabilities | Unique Vulnerabilities | Average Severity |
|--------------|-----------------------|------------------------|------------------|
| CentOS Linux | 1208                  | 1198                   | 5.14             |
| Java         | 1494                  | 772                    | 6.60             |
| Other        | 134                   | 68                     | 6.76             |

- **Category**: Represents a simplified grouping based on common terms in the vulnerabilities (like "Java" or "CentOS Linux").
- **Total Vulnerabilities**: The total count of vulnerabilities in each category.
- **Unique Vulnerabilities**: The count of unique CVE IDs in each category.
- **Average Severity**: The average severity level of vulnerabilities in each category.

This table provides a simplified view of your data, grouping related vulnerabilities together, which should help in prioritizing and addressing these security concerns efficiently.


### Ask a further question (control-d to quit)?
> can you expand on the CentOS Linux category?


### GPT

For the **CentOS Linux** category, here are more detailed insights:

### Breakdown by Severity Level

| Severity Level | Total Vulnerabilities |
|----------------|-----------------------|
| 1              | 2                     |
| 2              | 82                    |
| 3              | 10                    |
| 4              | 491                   |
| 5              | 224                   |
| 6              | 41                    |
| 7              | 222                   |
| 8              | 103                   |
| 9              | 26                    |
| 10             | 7                     |

This table shows the distribution of vulnerabilities organized by their severity level, with the majority being at severity level 4.

### Top 10 Most Common Vulnerabilities (based on CVE IDs) within CentOS Linux

| CVE ID          | Occurrences |
|-----------------|-------------|
| CVE-2022-25315  | 2           |
| CVE-2018-15688  | 2           |
| CVE-2022-25236  | 2           |
| CVE-2018-0495   | 2           |
| CVE-2019-15903  | 2           |
| CVE-2023-20593  | 2           |
| CVE-2022-1271   | 2           |
| CVE-2022-40674  | 2           |
| CVE-2023-0767   | 2           |
| CVE-2022-25235  | 2           |

These are the top 10 most commonly reported vulnerabilities (based on CVE IDs) for CentOS Linux in the dataset, each occurring twice.

This information indicates the areas of focus and highlights the specific vulnerabilities that have been most common within CentOS Linux assets, which could guide further investigation and remediation efforts.


### Ask a further question (control-d to quit)?
> could you give me that table again, but include the title of the CVE so I can better understand it?


### GPT

Here's the expanded table of the top 10 most common vulnerabilities within CentOS Linux, including their titles for better understanding:

| CVE ID          | Occurrences | Vulnerability Title |
|-----------------|-------------|---------------------|
| CVE-2022-25315  | 2           | CentOS Linux: CVE-2022-25315: Critical: firefox security update |
| CVE-2018-15688  | 2           | CentOS Linux: CVE-2018-15688: Important: Network Manager security update |
| CVE-2022-25236  | 2           | CentOS Linux: CVE-2022-25236: Critical: firefox security update |
| CVE-2018-0495   | 2           | CentOS Linux: CVE-2018-0495: Moderate: openssl security update |
| CVE-2019-15903  | 2           | CentOS Linux: CVE-2019-15903: Critical: firefox security update |
| CVE-2023-20593  | 2           | CentOS Linux: CVE-2023-20593: Important: kernel security update |
| CVE-2022-1271   | 2           | CentOS Linux: CVE-2022-1271: Important: gzip security update |
| CVE-2022-40674  | 2           | CentOS Linux: CVE-2022-40674: Important: expat security update |
| CVE-2023-0767   | 2           | CentOS Linux: CVE-2023-0767: Important: nss security update |
| CVE-2022-25235  | 2           | CentOS Linux: CVE-2022-25235: Critical: firefox security update |

Each entry in this table helps elucidate the nature of the vulnerability based on its title, providing context beyond just the CVE ID. This can assist in understanding the potential impact and area of concern for each listed vulnerability.


### Ask a further question (control-d to quit)?
> based on the CVE's and their severity, what would you categorise as the top 5 CVE areas to patch first?


## GPT

Based on the severity levels and occurrences of the CVEs in your dataset, here are the top 5 CVE areas to prioritize for patching, focusing on CentOS Linux vulnerabilities:

| CVE ID         | Severity Level | Occurrences | Vulnerability Title |
|----------------|----------------|-------------|---------------------|
| CVE-2020-12395 | 10             | 1           | CentOS Linux: CVE-2020-12395: Critical: firefox security update |
| CVE-2018-14618 | 10             | 1           | CentOS Linux: CVE-2018-14618: Low: curl security update |
| CVE-2017-18017 | 10             | 1           | CentOS Linux: CVE-2017-18017: Important: kernel security update |
| CVE-2016-4658  | 10             | 1           | CentOS Linux: CVE-2016-4658: Moderate: libxml2 security update |
| CVE-2019-17006 | 10             | 1           | CentOS Linux: CVE-2019-17006: Moderate: nss and nspr security update |

These vulnerabilities are categorized by the highest severity level (10) and have been identified within the dataset. The severity level indicates the urgency and potential impact of the vulnerability, making these top priorities for patching to ensure system security.

Note that the actual severity classification mentioned in the title (like Critical, Important, Moderate, Low) for CVE-2018-14618 appears to contradict its numerical severity level indicated. It's crucial to verify the severity levels and consider the risk they pose to your organization, alongside other contextual details provided in the titles, to prioritize patching efforts effectively.


### Ask a further question (control-d to quit)?
>
Goodbye!
