# Best Practices

The following is a list of guidelines for the development of Prompting

- language agnostic solutions
    - build today, but ensure we can pivot tomorrow
- Iterative algorithims are more robust
    - this is a tool. it needs to be bullet proof.
    - iterative solutions are less risky than recursive ones.
- Write Tests
    - Foundational technology needs to be tested
- Prefer functional solutions over Object Oriented ones.
    - This is simple tool, we don't need complex object oriented abstractions
    - Functional/Declarative code is easier to test when it is stateless
- Prefer stateless solutions over stateful ones
- Get a working prototype early and iterate

Keep is simple. Integrate Early. Test.


# Todos

- Create a design doc for Prompting - shane.au.wade

- Create the prompt composer visualizer (pvc)
    - Create a mockup of the visualization
        - mockups help a ton when developing visualizations
    - Look for appropriate libraries to create visualizations
    - write logic to extract all of the 'nodes' of the graph visual
    - write logic to connect all of the nodes together
    - ensure nodes have a reasonable layout
        - they need to be spaced out and ordered in some way
    - dump a png/jpg image

- Create a modular solution so we can 'Plug in' different LLMs
    - We are developing a system to compose prompts then send those prompts to models
    - we want to support any LLM if possible
    - Different models have different APIs
        - Should we define a simple interface that the user needs to implement?
        - Create a design doc ideally
    - maybe need a seperate piece of software to manage model integrations?
        - if we define an interface, people could implement it and make it avaliable for public use?

- Create deployment strategy
    - how are devs going to access our technology?
        - this is a cli, look at other clis for inspiration
    - We want to ship two things: pc and pcv
        - once installed, users should be able to run 'pc -v or pv --help' and 'pcv -v or pcv --help'
    - Keep it small initially, we don't have to support every package manager
        - A git clone + bootstrap bash/python script could be the way to go.


- create simple syntax validation step before prompt composition
    - one edge case that needs to be caught is "{{[[something]]}}" is invalid syntax
    - perhaps we could check if each [[filename]] points to a real file? easy validation
        - right now, the composer will error with 'file not found' if something doesn't exist
    - Try to break the prompt composer!
        - then we can write more syntax checks.
    - the algorithim itself should just iterate line by line and look for invalid patterns w/regex

- Testing
    - read the code that has been written already, ensure code is tested

- create seperate "Learn Prompting" repo
    - create examples of different prompting stratedys
    - look at twitter, openai docs, and other resources to learn more about prompt engineering techniques

- Syntax highlights for .prmt files
    - create simple syntax highlighting standards
    - implement Language Server: https://en.wikipedia.org/wiki/Language_Server_Protocol
    - with a language server, we can serve syntax highlighting and code completion to IDEs and text editors.



# Dev Infrastrucutre TODOS

- consider using docker as a dev enviroment
- use Black as a code formatter (for python)
- setup pylint
- Integrate Github Actions to perform CI checks
    - Check for black formatting
    - run pylint
    - run tests
    - deploy(?) hold off on this for a bit.
