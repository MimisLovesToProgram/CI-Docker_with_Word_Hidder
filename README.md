**Word Hidder**

Word Hidder is a very simple project that hides a Greek or English word in a mess of random characters of the word's language, built solely 
with the intention to illustrate the use of CI using GitHub Actions.

The project consists of:
- *WordHidder.py:* The project's word hidding script, performing the actions mentioned above.
- *WordHidder_test.py:* A Python file run using the library 'unittest' to test whether WordHidder.py is actually functional or not, by checking 
  if the example/testing word given is inside the messy string returned, and if the messy string contains capitalized letters.
- *.github/workflows/ci_testing_workflow.yml:* The YAML workflow file that runs the tests in WordHidder_test.py each time the user pushes
  changes to the remote repository. The workflow is set to run on push, since this is not a public repository and no one can make a pull 
  request (the most common workflow trigger), so the tests have to be set to run this way, so that I can see the CI run.