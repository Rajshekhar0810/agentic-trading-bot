from setuptools import setup, find_packages    #setuptools: A Python module used to package and distribute your code.
                                               #setup: The main function that defines your project's metadata and dependencies
                                               #find_packages(): Automatically finds all the Python packages (i.e., folders with __init__.py) in your project

setup(name = "agentic-trading-system",
      version=0.0.1,
      author_email= "rajshekhar0810@gmail.com",
      author= "Raj Shekhar",
      description= "A trading system that uses agentic AI to trade in the stock market",
      packages=find_packages(),
      install_requires=['lancedb','langchain','langgraph','tavily-python','polygon','langchain']
      )