# Prompting
The un-offical language of prompt engineering

## Installation
download repo, set path variable, set api key and http endpoint for inferences

```
TODO Create bootstrap script to install the pc and pcv
```


## Quick Start
create a sample prompt and execute it

```bash
touch input & echo "Say hello world" > input
touch hello_world & echo "[[input]]\n{{output}}" > hello_world
pc hello_world
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