""" Prompt Composer """


import re
import argparse

# import os
# import openai
# openai.organization = "personal"
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.Model.list()

VERSION = 0.1

# this regex pattern looks for [[VARIABLE_NAME]] pattern
# and returns VARIABLE_NAME
VARIABLE_PATTERN = "\[\[(.*?)\]\]"

EXECUTION_PATTERN = "\{\{(.*?)\}\}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Prompting Compiler v{}".format(VERSION))

    parser.add_argument('prompts', default=[], type=argparse.FileType("r"), nargs='+',
                    help='a list of paths to the prompts that will be executed in order')

    args = parser.parse_args()

    prompt_texts = []

    for prompt in args.prompts:
        text = prompt.read()
        prompt_texts.append(text)

    # for each prompt text
    # iteratively build the prompt
    # run inference on the prompt and save it to the specified file
    # repeat

    for text in prompt_texts:

        # PROMPT CONSTRUCTION PHASE

        prompt_states = [text]

        check_for_variable_subsitutions = True

        while check_for_variable_subsitutions:

            matchs = re.findall(VARIABLE_PATTERN, prompt_states[-1])

            if not matchs:
                check_for_variable_subsitutions = False
                pass

            for match in matchs:
                with open(match, 'r') as f:
                    # get the text for match
                    match_text = f.read()

                    # substitute the text for the variable
                    match_pattern = "\[\[{}\]\]".format(match)
                    new_prompt_text = re.sub(match_pattern, match_text, prompt_states[-1])

                    # update the text
                    prompt_states.append(new_prompt_text)


        # PROMPT EXECUTION PHASE

        final_prompt_w_possible_executions = prompt_states[-1]

        # find special execution syntax to extract paths to dump inference result
        paths = re.findall(EXECUTION_PATTERN, final_prompt_w_possible_executions)

        final_prompt = re.sub(EXECUTION_PATTERN, "", final_prompt_w_possible_executions)

        # send prompt to user specified model w user api key

        model_response = "THIS IS A SAMPLE RESULT"

        for path in paths:
            with open(path, 'w+') as f:
                f.write(model_response)



