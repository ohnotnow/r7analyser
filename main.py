import os
import time
import argparse
from openai import OpenAI
from yaspin import yaspin

default_assistant_instructions = """
    You are a helpful AI assistant who is an expert at analysing Rapid7 CSV exports.  The detail computer hosts and the CVEs
    which are present on them.  YOUR MISSION is to help the user understand the data in the CSV document provided, drill into details and
    answer questions about the data.  You should always refer to the CSV document the user has provided before answering a question.
    Please use markdown to format your answers and be thorough.  This is CRITICAL to the future of the prestigeous and
    highly regarded instituion the user works for.  Failure is not an option.
"""
@yaspin(text="Waiting on GPT")
def get_assistant_response(client, thread, run):
    answer = ""
    while not answer:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run.status == "completed":
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            answer = messages.data[0].content[0].text.value
        else:
            time.sleep(1)
    return answer

@yaspin(text="Creating GPT run")
def create_run(client, thread, assistant_id, file_id, prompt):
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt,
        file_ids=[file_id]
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )
    return run

def main():
    parser = argparse.ArgumentParser(description='Process Rapid7 csv exports.')
    parser.add_argument('csv', type=str, default='', help='The filename of the R7 csv')
    parser.add_argument('--thread', type=str, default='', help='Use an already existing thread ID')
    parser.add_argument('--assistant', type=str, default=os.getenv('R7_ASSISTANT_ID'), help='Use an already existing assistant ID')
    args = parser.parse_args()

    if not args.csv:
        print("You must provide a rapid7 csv file.")
        exit(1)
    client = OpenAI()
    file = client.files.create(
        file=open(args.csv, "rb"),
        purpose="assistants"
    )
    thread = client.beta.threads.create()
    assistant_id = None
    if args.assistant:
        assistant_id = args.assistant
    if not assistant_id:
        print("No R7_ASSISTANT_ID environment variable found or passed via --assistant.")
        create = input("Would you like to create a new assistant (y/n)? ")
        if create.lower() == 'y':
            assistant = client.beta.assistants.create(
                name="Rapid7 CSV Analyser",
                instructions=default_assistant_instructions,
                description="Analyse Rapid7 CSV exports",
                model="gpt-4-turbo-preview",
                tools=[{"type": "code_interpreter"}, {"type": "retrieval"}],
            )
            assistant_id = assistant.id
            print(f"Created assistant with ID {assistant_id}.  Please set the R7_ASSISTANT_ID environment variable to this value so it is used in the future.")
        else:
            print("Cannot run without an assistant.  Exiting.")
            exit(1)
    run = create_run(
        client,
        thread,
        assistant_id,
        file.id,
        "Can you produce a simplified markdown table of the data contained in the csv document?  There are lots of reported CVE's, but many are related (for instance there are many to do just with 'java' or the JRE).  So I would like a simplified table where the java CVE's were all just grouped into 'Java', and similarly for other related CVE's.  Could you do that for me?"
    )
    summary = get_assistant_response(client, thread, run)
    print(f"\n\n## Initial Summary\n\n{summary}\n\n")
    while True:
        question = input("### Ask a further question (control-d to quit)?\n> ")
        if question and question.lower() != 'q' and question.lower() != 'quit' and question.lower() != 'exit' and question.lower() != 'n' and question.lower() != 'no':
            run = create_run(client, thread, assistant_id, file.id, question)
            answer = get_assistant_response(client, thread, run)
            print(f"\n\n## GPT\n\n{answer}\n\n")
        else:
            print("Goodbye!")
            exit(0)

if __name__ == '__main__':
    main()
