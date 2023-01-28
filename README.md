
![prmt_lang_logo](.github/prompting_logo_50.jpg?raw=true)

# Prompting
The un-offical language of prompt engineering

## Installation
download repo, set path variable, set api key and http endpoint for inferences

Run the following command in the root directory of the project.  This command will add the prompting/src folder to your path which will allow you to run the PC anywhere.

RUN THIS IN ~/YOUR/PATH/prompting
```
export PATH=$(pwd)/src:$PATH
```

If you want to automatically load the prompt composed each time, update the path in your .bashrc file to other profile file.
```
export PATH=/YOUR/PATH/TO/prompting/src:$PATH
```

## Quick Start
create a sample prompt and execute it

```bash
touch input & echo "Say hello world" > input.prmt
touch hello_world & echo "[[input]]\n{{output}}" > hello_world.prmt
pc hello_world.prmt
```

## Help

```
pc --help
pcv --help
```

## Syntax
Reference other plain text files using the [[FILE_NAME]] syntax.

The prompt composer will substitute the [[FILE_NAME]] variable with the text in the specified file.

Execute a api call to an LLM and pipe the output into a specified file using the {{FILE_NAME}} syntax or to STD_OUT.

Using this simple syntax, complex prompts can be decomposed into chunks.

Compose/execute one prompt at a time or specify a series of prompts that are executed serially.

```
pc prompt_1
pc prompt_1 prompt_2
```

## What is it?
Prompting is a prompt composition framework.  The framework aims to provide a modern, unintrusive dev experience that is easy to learn.

## Why?
Using files and folders means engineers can use standard version control to share, collobrate, read and write prompts.

This framework will help us accelerate our understanding of prompt engineering.

## Brief History
Prompting is inspired by a visual coding tool call MultiFlow. The visual experience is excellent, but it was difficult to intergate into a standard software engieering workflow and it is less time efficient.  Prompting intends to capture the 'feeling' of Multiflow with folders and files.